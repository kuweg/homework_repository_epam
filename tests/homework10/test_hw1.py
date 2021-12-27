import pytest

from homework10.utils import parse_company_page, parse_main_page


@pytest.fixture
def company_page_object():
    """
    Archive webpage for company page.
    """
    file = "tests/homework10/ZBRA_Stock.html"
    with open(file, encoding="utf8") as html:
        return html.read()


@pytest.fixture
def website_page():
    """
    Last page with 5 companies.
    """
    file = "tests/homework10/page.html"
    with open(file, encoding="utf8") as html:
        return html.read()


def test_company_page_p_e(company_page_object):
    """Checking that P/E parsed correctly."""
    company = parse_company_page(company_page_object)
    assert company["P_E"] == 29.35


def test_company_page_code(company_page_object):
    """Checking that company code parsed correctly."""
    company = parse_company_page(company_page_object)
    assert company["code"] == "Zebra Technologies Corp."


def test_company_page_profit(company_page_object):
    """Checking that profit calculated correctly."""
    company = parse_company_page(company_page_object)
    assert company["profit"] == 242.46


def test_count_companies_on_last_page(website_page):
    """
    Checking that function returns corret amount of companies
    at the last page.
    """
    page = parse_main_page(website_page)
    assert len(page) == 5
