'''This package has one Goods class used to calculate tax amount.
   It has a Toys subclass of Goods class which sets the toy type. '''


class Goods:

    '''This is subclass of Goods. It takes three attributes of the toy - base price, perecnt sales tax and type of toy.
    It is used to calculate the tax amount on different type of toys using its super class method get_tax_amount.
    The toy could be used by a boy or a girl , default toy is used by boys.'''

    def __init__(self, base_price, percent_sales_tax):
        """
      Parameters
      ----------
      base_price : float
          The base price of the item
     percent_sales_tax : float
          Percentage sales tax on the item
       """
        self.base_price = base_price
        self.percent_sales_tax = percent_sales_tax

    def __str__(self):
        return f"Base price is {self.base_price} and  percentage sales tax is {self.percent_sales_tax}"

    def __repr__(self):
        return f'Goods({self.base_price}, {self.percent_sales_tax})'

    def __eq__(self, other):
        '''
        Parameters
        ----------
        Two instance of the class.
        ----------
        Equality of the objects are compared on base price.
        '''
        return self.base_price == other.base_price

    def __lt__(self, other):
        '''
        Parameters
        ----------
        Two instance of the class.
        ----------
        Two objects are compared on base price.
        '''
        return self.base_price < other.base_price

    def __ge__(self, other):
        '''
        Parameters
        ----------
        Two instance of the class.
        ----------
        Two objects are compared on base price.
        '''
        return self.base_price >= other.base_price

    def get_tax_amount(self):
        '''It calculates tax amount of an item if given base price and percentage tax on the item.'''
        tax_amount = self.base_price * self.percent_sales_tax/100
        print(f'Base price is ${self.base_price} and Tax amount is ${tax_amount:.2f}')



class Toys(Goods):
    '''This is subclass of Goods. It takes three attributes of the toy - base price, perecnt sales tax and type of toy.
    It is used to calculate the tax amount on different type of toys using its super class method get_tax_amount.
    The toy could be used by a boy or a girl , default toy is used by boys.'''

    def __init__(self, base_price, percent_sales_tax, toy_type="boys"):
        """
      Parameters
      ----------
     base_price : float
          The base price of the item
     percent_sales_tax : float
          Percentage sales tax on the item
     toy_type : str
         The toy used for girls or boys.
       """
        super().__init__(base_price, percent_sales_tax)
        self.toy_type = toy_type

    def __str__(self):
        return f"Base price of Toy is {self.base_price} and  percentage sales tax on toys is {self.percent_sales_tax}. It is a {self.toy_type}'s toy."
