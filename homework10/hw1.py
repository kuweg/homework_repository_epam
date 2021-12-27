import asyncio
import json
from concurrent.futures import ProcessPoolExecutor
from itertools import chain

import aiohttp
from utils import parse_company_page, parse_main_page

_workers = 40


async def fetch_page(url: str) -> str:
    """
    Fetch conenction for single page.

    :param url: page url
    :type url: str
    :return: webpage text
    :rtype: str
    """
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()


async def fetch_all_pages(urls: list[str]) -> list[str]:
    """
    Fetching all requests.

    :param urls: list of pages urls
    :type urls: list
    :return: list of responce objects
    :rtype: list
    """
    tasks = [asyncio.create_task(fetch_page(url)) for url in urls]
    await asyncio.gather(*tasks)
    return [task.result() for task in tasks]


async def parse_companies_data(urls) -> list[dict]:
    """
    Parses list of companies from list of url.
    Forms dict with company inforamtion.

    :param urls: list of webpages urls
    :type urls: str
    :return: list of dicts with companies information
    :rtype: list[dict]
    """
    companies_list = await fetch_all_pages(urls)
    with ProcessPoolExecutor(max_workers=_workers) as pool:
        companies_data = list(pool.map(parse_main_page, companies_list))
        companies_data = list(chain.from_iterable(list(companies_data)))
        return companies_data


async def combine_companies_data(urls: str) -> list[dict]:
    """
    Parses information form company page and merge it with
    existing dict with same company.

    :param urls: list of webpages urls
    :type urls: str
    :return: list of dicts with companies information
    :rtype: list[dict]
    """
    companies_list = await parse_companies_data(urls)
    companies_urls = [company.pop("url") for company in companies_list]
    companies_pages = await fetch_all_pages(companies_urls)
    with ProcessPoolExecutor(max_workers=_workers) as pool:
        companies_data = list(pool.map(parse_company_page, companies_pages))

    for comp_main_info, comp_page_info in zip(companies_list, companies_data):
        comp_main_info |= comp_page_info
    return companies_list


def get_top_10(companies_dict, key: str, reverse: bool = False) -> list[dict]:
    """
    Finding top 10 companies sorted by passed key.

    :param companies_dict: list of cicts of companies parsed info
    :type companies: list[dict]
    :param key: a key for sorting
    :type key: str
    :param reverse: bool flag for sorted()
    :type reverse: bool
    :return: sorted list by key with top 10 dicts
    :rtype: list[dict]
    """
    return sorted(companies_dict,
                  key=lambda company: company[key],
                  reverse=reverse)[:10]


async def main(urls: list):
    """
    Creating json files with top 10 companies.
    Top 10 companies formed by task.

    :param urls: list of urls for parsing data
    :type urls: list
    """
    max_keys = ["price", "growth", "profit"]
    min_keys = ["P_E"]
    companies_data = await combine_companies_data(urls)
    for key in max_keys:
        with open(f"top_{key}.json", "w") as file:
            top_companies = get_top_10(companies_data, key, reverse=True)
            json.dump(top_companies, file, indent=4)

    for key in min_keys:
        with open(f"top_{key}.json", "w") as file:
            top_companies = get_top_10(companies_data, key)
            json.dump(top_companies, file, indent=4)


if __name__ == "__main__":
    PAGES_AMOUNT = 11
    url_template = (
        "https://markets.businessinsider.com/" + "index/components/s&p_500?p="
    )
    URLS = [url_template + str(page) for page in range(1, PAGES_AMOUNT + 1)]
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(URLS))
    loop.close()
