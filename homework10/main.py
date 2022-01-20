"""
1. get request(s) from webpage (webpages)
2. parse pages with ParserClass and store result 

3. Somewhow form dict of all company's required data
4. sort dict and dump result accroding task


``
list of tags
MainPagePArser
Business parser
``
#done
urls = await urls

contents = [paser(url).content for url in urls]
#done
MainPAgeParser(.....)
#done
main_pages_info = main_page_parser.get_info()

companies_urls = [company.pop('url')]
companies_content = [parser(url).content for url in companies_url]
business_insider = BusinessParser(....)
business_info = business_insoder.get_info()

for main_page, company_page in zip(main_pages_info, business_info):
    general_infoa.append(main_page | company_page)


top_dumper_json = TopNDumper(.....)

# done
top_dumper_json(top_n = 10,
                name = 'top_growth',
                filter = 'growth,
                asceding = False)
"""
import asyncio
import datetime
from utils import merge_two_list_dicts
from parsers import BeautifulSoupParser
from tags_builder import (name, url_, growth, code, low_52, high_52, price, p_e)
from company import MainPageParser, ParseCompanyPage
from currency import UsdConverter

from dumper import TopDictDumper
from client import AiohttpClient


async def main():
    pages_amonont = 11
    URL_BASE = (
            "https://markets.businessinsider.com/index/components/s&p_500?p="
        )
    COMPANY_URL_BASE = 'https://markets.businessinsider.com'
    urls = [URL_BASE + str(page) for page in range(1, pages_amonont + 1)]
    print(f'Get {len(urls)} pages')

    today = datetime.date.today().strftime("%d/%m/%Y")
    rate_url = f'https://www.cbr.ru/scripts/XML_daily.asp?date_req={today}'

    client = AiohttpClient()
    parser = BeautifulSoupParser
    usd_rate = UsdConverter(source=rate_url, parser=parser).get_rate_to_rub()

    print('Starting responces')
    main_pages_responses = await client.fetch_all_pages(urls)
    print(f'Get {len(main_pages_responses)} pages')
    main_pages_content = parser.get_contents_list(main_pages_responses)
    print(f'Recivied content from pages')

    main_pages_parser = MainPageParser(pages=main_pages_content,
                                       table_tag='tbody',
                                       line_tag='tr',
                                       parser=parser,
                                       text_attrs=[name.get_attrs_list(), url_.get_attrs_list()],
                                       order_attrs=[growth.get_attrs_list()])
    print(f'Start parsing')
    main_pages_parser.parse_info()
    main_pages_data = main_pages_parser.format_raw_data()
    print('Parsing was done!')
    
    companies_urls = [
        COMPANY_URL_BASE + company.pop('url')
        for company in main_pages_data
        ]
    print("Formed companie's urls")
    print(companies_urls[0])
    print("Getting companie's urls")
    companies_pages_responses = await client.fetch_all_pages(companies_urls)
    companies_pages = parser.get_contents_list(companies_pages_responses)
    print(f'Urls .. OK! Contents was formed : {len(companies_pages)}')

    tags_dict = {'price': price, 'low_52': low_52, 'high_52': high_52, 'code': code}
    company_page_parser = ParseCompanyPage(parser=parser,
                                           tags=tags_dict)
    print('Company parser object was set')
    print(company_page_parser.tags)
    companies_pages_data = []
    for page in companies_pages[:2]:
        page_data = company_page_parser.parse_page(page, usd_rate)
        companies_pages_data.append(page_data)

    # general_companies_data = merge_two_list_dicts(
    #     main_pages_data, companies_pages_data
    # )

    return companies_pages_data


if __name__ == '__main__':

    asyncio.run(main())