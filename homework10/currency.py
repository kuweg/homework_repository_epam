from abc import ABCMeta ,abstractmethod

import requests
from parsers import BeautifulSoupParser
import datetime 
from typing import Callable
from functools import lru_cache


class BaseCurrency(metaclass=ABCMeta):
    def __init__(self, source: str,
                 date: str = None) -> None:
        if date is not None:    
            self.url = source + date
        else:
            self.url = source
        self.date = date

    @property    
    @abstractmethod
    def _CURRENCY_CODE(self):
        pass

    @abstractmethod
    def _get_content(self):
        pass
    
    @abstractmethod 
    def get_rate_to_rub(self):
        pass


class UsdConverter(BaseCurrency):
    
    _CURRENCY_CODE = "R01235"

    def __init__(self, source: str, parser: Callable, date: str = None) -> None:
        BaseCurrency.__init__(self, source, date)
        self.content = self._get_content()
        self.parser = parser(self.content)
        self.soup = self.parser.content

    @lru_cache(1)    
    def _get_content(self):
        response = requests.get(self.url)
        return response.content


    def get_rate_to_rub(self):
        valute = self.parser.find(self.soup, 'valute', id = self._CURRENCY_CODE)
        valute_value = self.parser.find(valute, 'value')
        valute_value = self.parser.extract_info(valute_value)
        return float(valute_value.replace(',','.'))


# today = datetime.date.today().strftime("%d/%m/%Y")
# rate_url = f'https://www.cbr.ru/scripts/XML_daily.asp?date_req={today}'
# a = UsdConverter(source = rate_url,
#                  parser = BeautifulSoupParser)

# b = a.get_rate_to_rub()
# print(b)
