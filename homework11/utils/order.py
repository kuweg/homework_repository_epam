from abc import abstractmethod


class OrderObj:
    """Parent class for forward declaration."""
    @abstractmethod
    def final_price(self):
        pass
