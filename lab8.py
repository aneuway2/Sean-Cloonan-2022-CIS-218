class Goods:
    def __init__(self, baseprice, percentsalestax):
        self.__basePrice = baseprice
        self.__percentSalesTax = percentsalestax

    def getTaxAmount(self):
        taxamount = self.__basePrice * self.__percentSalesTax/100
    print(f'Base price is ${self.__basePrice} and Tax amount is ${taxamount:.2f}')
