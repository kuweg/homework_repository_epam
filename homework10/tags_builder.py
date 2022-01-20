

class TagBuilder:

    def __init__(self, key, **kwargs):
        self.key = key
        self.kwargs = kwargs

    def get_element(self):
        raise NotImplementedError

    def get_attrs_list(self):
        return [self.key] + list(self.kwargs.values())

    def get_attrs_dict(self, key: bool=False):
        if key:
            return (self.key, self.kwargs)
        return self.kwargs
    

name = TagBuilder(key='name',
                     tag='a',
                     get_tag ='title')

url_ = TagBuilder(key='url',
                   tag='a',
                   get_tag ='href')

growth = TagBuilder(key='growth',
                         tag='span',
                         column_order=8)

code = TagBuilder(key='code',
                  name = 'span',
                  class_ = 'price-section__category')

low_52 = TagBuilder(key='low_52',
                    name = 'div',
                    text="52 Week Low")

high_52 = TagBuilder(key='high_52',
                     name = 'div',
                     text="52 Week High")

p_e = TagBuilder(key='P_E',
                 name='div',
                 text='P/E Ratio')

price = TagBuilder(key='price',
                   name = 'span',
                   class_='price-section__current-value')


