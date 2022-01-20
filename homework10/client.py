from abc import ABCMeta, abstractmethod
import requests
import aiohttp
import asyncio


class BaseClient(metaclass=ABCMeta):
    @abstractmethod
    def fetch_response(self):
        pass


class RequestCline(BaseClient):

    def fetch_response(self, url: str):
        response = requests.get(url)
        return response

    
class AiohttpClient(BaseClient):
        
    async def fetch_response(self, url: str) -> str:
        """
        Fetch conenction for single page.

        :param url: page url
        :type url: str
        :return: webpage text
        :rtype: str
        """
        async with aiohttp.ClientSession(trust_env=True) as session:
            async with session.get(url) as response:
                if response.status == 200:
                    try:
                        return await response.text()
                    except ValueError:
                        pass
                return None


    async def fetch_all_pages(self, urls: list[str]) -> list[str]:
        """
        Fetching all requests.

        :param urls: list of pages urls
        :type urls: list
        :return: list of responce objects
        :rtype: list
        """
        tasks = [asyncio.create_task(self.fetch_response(url)) for url in urls]
        await asyncio.gather(*tasks)
        pages = [task.result() for task in tasks]
        return pages
