'''This package has one Goods class used to calculate tax amount.
   It has a Toys subclass of Goods class which sets the toy type. It is also testing
   the different functions implemented in the class.'''

class Goods:

    '''It takes two attributes of the Goods - base price, perecnt sales tax .
    It is used to calculate the tax amount on different type of goods.
    '''

    def __init__(self, base_price, percent_sales_tax):
        """
      Parameters
      ----------
      base_price : float
          The base price of the item
     percent_sales_tax : float
          Percentage sales tax on the item
       """
        self.__base_price = base_price
        self.__percent_sales_tax = percent_sales_tax

    def __str__(self):
        return f"Base price is {self.__base_price} and  percentage sales tax is {self.__percent_sales_tax}"

    def __repr__(self):
        return f'Goods({self.__base_price}, {self.__percent_sales_tax})'

    def __eq__(self, other):
        '''
        Parameters
        ----------
        Two instance of the class.
        ----------
        Equality of the objects are compared on base price.
        '''
        return self.__base_price == other.__base_price

    def __lt__(self, other):
        '''
        Parameters
        ----------
        Two instance of the class.
        ----------
        Two objects are compared on base price.
        '''
        return self.__base_price < other.__base_price

    def __ge__(self, other):
        '''
        Parameters
        ----------
        Two instance of the class.
        ----------
        Two objects are compared on base price.
        '''
        return self.__base_price >= other.__base_price

    def get_tax_amount(self):
        '''It calculates tax amount of an item if given base price and percentage tax on the item.'''
        tax_amount = self.__base_price * self.__percent_sales_tax/100
        return tax_amount



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

good1 = Goods(50, 5)


def test_get_tax_amount():
    """
    For testing of calculation tax amount based on the private variables.
    """
    tax_amount = good1.get_tax_amount()
    assert tax_amount == 2.5


def test_str():
    '''For testing __str__ function'''
    string = good1.__str__()
    assert string == "Base price is 50 and  percentage sales tax is 5"

def test_repr():
    '''For testing __str__ function'''
    string = good1.__repr__()
    assert string == "Goods(50, 5)"

def test_eq():
    ''' for testing __eq__ function'''
    good2 = Goods(50, 5)
    assert good1 == good2

def test_ge():
    ''' for testing __ge__ function'''
    good3 = Goods(45, 5)
    assert good1 >= good3

def test_lt():
    ''' for testing __lt__ function'''
    good4 = Goods(60, 5)
assert good1 < good4
