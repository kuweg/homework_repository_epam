from __future__ import annotations
from cgi import print_directory
from typing import Callable, Any
from parsers import BeautifulSoupParser
from utils import format_data
import requests
from bs4 import BeautifulSoup
from tags_builder import TagBuilder


class Company:
    pass

class BaseCompaniesListParser:
    # parse main pges anf rom dict of companies with stats than filter and choose what needed
    def __init__(self) -> None:
        raise NotImplementedError('Required __init__() method')

    
class BaseCompanyBusinessInsider:
    #pase company page and took what we need
    pass


class MainPageParser:

    def __init__(self, pages, table_tag, line_tag,
                 parser, text_attrs, order_attrs) -> list[dict]:
        self.pages_list = pages
        print(len(self.pages_list))
        self.table_tag = table_tag
        self.line_tag = line_tag
        self.parser = parser
        self.attrs = text_attrs
        self.attrs_with_order = order_attrs
        self.raw_info = []

    def get_table(self, page):
        companies_table = self.parser.find(
            page, self.table_tag
            )
        return companies_table

    def parse_companies_list(self, page):
        main_table = self.get_table(page)
        companies_lines = [
            company_line for company_line
            in self.parser.find_all(main_table, self.line_tag) 
        ]
        return companies_lines


    def extract_info(self, companies_lines, name, tag, get_tag):
        if not companies_lines:
            raise AttributeError('You may miss some preprocessing steps.')
        comp = {}
        tag_info = [
            self.parser.find(line, tag) for line
            in companies_lines 
        ]
        
        comp[name] = list(
            map(
                lambda x: self.parser.get_by_tag(x, get_tag),
                tag_info
                )
            )
        return comp

    def extract_numeric_info(self, companies_lines, name, tag, order):
        
        if not companies_lines:
            raise AttributeError('You may miss some preprocessing steps.')
        comp = {}
        tag_info = [
            self.parser.find_all(line, tag)[order] for line
            in companies_lines 
        ]
        
        comp[name] = list(
            map(
                lambda x: float(x.text.replace(',','')),
                tag_info
                )
            )
        return comp

    def parse_info(self):
        for page in self.pages_list:
            companies_list = self.parse_companies_list(page)
            page_buffer = []
            for task in self.attrs:
                key = task[0]
                tags = task[1:]
                company_info = self.extract_info(companies_list, key, *tags)
                page_buffer.append(company_info)
            
            for task in self.attrs_with_order:
                key = task[0]
                tags = task[1:]
                company_info = self.extract_numeric_info(companies_list, key, *tags)
                page_buffer.append(company_info)
            self.raw_info.append(page_buffer)

    def format_raw_data(self):
        return format_data(self.raw_info)



class ParseCompanyPage:

    def __init__(self, parser: Callable, tags: dict) -> None:
        self.parser = parser
        self.tags = tags
        self.company_data = {}

    def get_element_by_tag(self,page, tag: TagBuilder, none_case: Any = .0):
        try:
            element = self.parser.find(page, None ,**tag.get_attrs_dict())
            element = element.text.strip().replace(',','.')
            return element
        except AttributeError:
            return none_case

    def get_previous_element_by_tag(self, page, tag: TagBuilder, none_case: Any = .0):
        try:
            element = self.parser.find(page, None, **tag.get_attrs_dict())
            element = self.parser.find_previous_element(element).strip()
            return element
        except AttributeError:
            return none_case

    def get_company_potential_profit(self, page, min_tag, max_tag):
        min_profit = float(self.get_previous_element_by_tag(
            page, min_tag
            )
        )
        max_profit = float(self.get_previous_element_by_tag(
            page, max_tag
            )
        )
        return round(max_profit - min_profit)

    def parse_page(self, page, rate: float):
        self.company_data['code'] = self.get_element_by_tag(page, self.tags['code']).split()[-1]
        self.company_data['price'] = float(
            self.get_element_by_tag(page, self.tags['price'])
            ) * rate
        self.company_data['profit'] = self.get_company_potential_profit(
            page, self.tags['low_52'], self.tags['high_52']
            )

