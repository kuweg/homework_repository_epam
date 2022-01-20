from concurrent.futures import process
import datetime
from functools import lru_cache
from typing import Any

import requests
from bs4 import BeautifulSoup
from requests.exceptions import RequestException


@lru_cache(1)
def get_usd_exchange_rate():
    """
    Get current usd to rub exchange rate.

    :return: either usd exchange rate if request was successful
             either 1
    :rtype: float
    """
    today = datetime.date.today().strftime("%d/%m/%Y")
    try:
        req = f"http://www.cbr.ru/scripts/XML_daily.asp?date_req={today}"
        valutes = requests.get(req)
    except RequestException:
        return 1.0
    valutes = valutes.text.split("</Valute>")
    for index, elem in enumerate(valutes):
        if '<Valute ID="R01235">' in elem:
            usd = valutes[index]
    usd = usd.split("<Value>")[1].split("</Value>")[0].replace(",", ".")
    return float(usd)


def parse_main_page(content: str) -> list[dict]:
    """
    Parsing main page and forming list of dicts
    with common information:

    Example:
        [{'name' : ... , 'growth' ... , 'url': ...},
          ...]

    :param content: a webpage content from request object
    :type content: str
    :return: list of dicts with companies information
    :rtype: list[dict]
    """
    soup = BeautifulSoup(content, "html.parser")
    table = soup.find("tbody")
    _growth_orded = 8

    comp = dict()
    comp["name"] = [elem.get("title") for elem in table.find_all("a")]
    comp["growth"] = [
        float(elem.text.split()[0].replace(",", ""))
        for order, elem in enumerate(table.find_all("td"), 1)
        if order % _growth_orded == 0
    ]
    comp["url"] = [
        f"https://markets.businessinsider.com{link.get('href')}"
        for link in table.find_all("a")
    ]

    page_data = [
        {"name": name, "growth": growth, "url": url}
        for name, growth, url in zip(*comp.values())
    ]
    return page_data


def parse_company_page(content: str) -> dict:
    """
    Parsing company page for following information:
    company code, price, P/E, potential profit.

    :param content: a webpage content from request object
    :type content: str
    :return: dict with company information
    :rtype: dict
    """
    company_data = dict()
    company_page = BeautifulSoup(content, "html.parser")
    company_data["code"] = parse_company_code(company_page)
    company_data["price"] = parse_company_price(company_page)
    company_data["P_E"] = parse_company_pe(company_page)
    company_data["profit"] = parse_company_potential_profit(company_page)
    return company_data


def parse_company_code(company_data: BeautifulSoup):
    """
    Parsing page for company code.

    :param company_data: a bs4 object with page content
    :type company_data: BeautifulSoup
    :raise: AttributeError if element does not exist
    :return: company code
    :rtype: str
    """
    try:
        code = company_data.find(
            "span", class_="price-section__label"
            ).text.rstrip()
        return code
    except AttributeError:
        return "Not stated"


def parse_company_potential_profit(company_data: BeautifulSoup):
    """
    Parses company page for low_52 and high_52 criterias
    and calculates potential profit.

    :param company_data: a bs4 object with page content
    :type company_data: BeautifulSoup
    :raise: AttributeError if element does not exist
    :return: potential profit
    :rtype: float
    """
    try:
        low_52 = float(
            company_data.find("div", text="52 Week Low")
            .previous_element.strip()
            .replace(",", "")
        )
    except AttributeError:
        low_52 = 0

    try:
        high_52 = float(
            company_data.find("div", text="52 Week High")
            .previous_element.strip()
            .replace(",", "")
        )
    except AttributeError:
        high_52 = 0

    return round(high_52 - low_52, 3)


def parse_company_pe(company_data: BeautifulSoup):
    """
    Parses page for company P/E.

    :param company_data: a bs4 object with page content
    :type company_data: BeautifulSoup
    :raise: AttributeError if element does not exist
    :return: company P/E
    :rtype: float
    """
    try:
        pe = (
            company_data.find("div", text="P/E Ratio")
            .previous_element.strip()
            .replace(",", "")
        )
        return float(pe)
    except AttributeError:
        return 0.0


def parse_company_price(company_data: BeautifulSoup):
    """
    Parses page for company price and converts it to rub.

    :param company_data: a bs4 object with page content
    :type company_data: BeautifulSoup
    :raise: AttributeError if element does not exist
    :return: company price in rubles
    :rtype: float
    """
    try:
        price = company_data.find(
            "span", class_="price-section__current-value"
        ).text.replace(",", "")
        return round(float(price) * get_usd_exchange_rate(), 3)
    except AttributeError:
        return 0.0


def _main_page_content_filter(content: str):
    """
    Parsing webpage to check that it's valid.

    :param content: content of passed webpage
    :type pages: str
    :return: True if valid, else False
    :rtype: bool
    """
    soup = BeautifulSoup(content, "html.parser")
    compaies_table = soup.find("div", class_="table-responsive")

    return compaies_table is not None


def check_main_pages_content(pages: list):
    """
    Check pages with in-built filter()

    :param pages: list of webpages content
    :type pages: list
    :return: list of validated pages
    :rtype: list
    """
    check = filter(_main_page_content_filter, pages)
    return list(check)


def _company_page_filter(content: str):
    """
    Parsing webpage to check that it's valid.

    :param content: content of passed webpage
    :type pages: str
    :return: True if valid, else False
    :rtype: bool
    """
    soup = BeautifulSoup(content, "html.parser")
    error_msg = soup.find("h1", class_="grid__col--12 header-underline")
    return error_msg is None


def check_company_pages(pages: list):
    """
    Check pages with in-built filter()

    :param pages: list of webpages content
    :type pages: list
    :return: list of validated pages
    :rtype: list
    """
    check = filter(_company_page_filter, pages)
    return list(check)


def _reshape(lst, fill_missing):
    max_length = len(max(lst, key = len))
    new_list = []
    for order in range(max_length):
        buffer = []
        for sublist in lst:
            try:
                buffer.append(sublist[order])
            except:
                buffer.append(fill_missing)
        new_list.append(buffer)
    return new_list


def format_data(raw_data: list, missing_filler: Any = None) -> list[dict]:
    processed_data = []
    for lst in raw_data:
        keys = list(map(lambda x: [*x], lst))
        keys = [value for col in keys for value in col]
        dict_values = list(map(lambda x: list(*x.values()), lst))
        reshaped_values = _reshape(dict_values, missing_filler)

        res = []
        for lst_ in reshaped_values:
            res.append({key: value for key, value in zip(keys, lst_)})
        processed_data.append(res)
    processed_data = [value for col in processed_data for value in col]  
    return processed_data


def merge_two_list_dicts(list_a: list[dict], list_b: list[dict]) -> list[dict]:
    for dict_a, dict_b in zip(list_a, list_b):
        dict_a |= dict_b

    return list_a

