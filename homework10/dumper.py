import json
from abc import abstractmethod, ABCMeta


class BaseDumper(metaclass=ABCMeta):

    @staticmethod
    @abstractmethod
    def dump(self):
        pass


class TopDictDumper(BaseDumper):

    @staticmethod
    def dump(data: list,
             top_n: int,
             name: str,
             filter_key: str,
             asceding: bool,
             indent: int = 4):
        with open(f'{name}.json', 'w') as file:
            top_elements = sorted(data,
                                   key=lambda x: x[filter_key],
                                   reverse=asceding)[:top_n]
            json.dump(top_elements, file, indent=indent)


    