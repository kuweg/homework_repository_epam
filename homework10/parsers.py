import datetime
from functools import lru_cache
from abc import ABCMeta, abstractclassmethod, abstractstaticmethod

import requests
from bs4 import BeautifulSoup, element
from requests.exceptions import RequestException


class BaseParser(metaclass=ABCMeta):

    @abstractstaticmethod
    def find(self, tag: str, **kwargs):
        pass

    @abstractstaticmethod
    def find_previous_element(self):
        pass

    @abstractstaticmethod
    def find_next_element(self):
        pass

    @abstractstaticmethod
    def extract_info(self):
        pass

    @abstractstaticmethod
    def find_all(self):
        pass

    @abstractstaticmethod
    def get_by_tag(self):
        pass


class BeautifulSoupParser(BaseParser):

    def __init__(self, content, parser_mode: str = 'html.parser') -> None:
        self.content = BeautifulSoup(content, parser_mode)

    @staticmethod
    def get_contents_list(responces: list) -> list:
        return [BeautifulSoupParser(response).content for response in responces]

    @staticmethod
    def find(soup: BeautifulSoup, tag: str, **kwargs) ->BeautifulSoup:
        if tag:
            return soup.find(tag, kwargs)
        return soup.find(**kwargs)

    @staticmethod
    def find_previous_element(soup_element: BeautifulSoup):
        element = soup_element.previous_element
        return element
        
    @staticmethod
    def find_next_element(soup_element: BeautifulSoup):
        element = soup_element.next_element
        return element

    @staticmethod
    def find_all(soup: BeautifulSoup, tag: str):
        elements = soup.find_all(tag)
        return elements

    @staticmethod
    def get_by_tag(soup: BeautifulSoup, tag: str):
        return soup.get(tag)

    @staticmethod
    def extract_info(*args):
        return args[0].text

