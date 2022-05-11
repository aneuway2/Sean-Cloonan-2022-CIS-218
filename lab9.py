class Goods:
    def __init__(self, baseprice, percentsalestax):
        self.basePrice = baseprice
        self.percentSalesTax = percentsalestax
def __str__(self):
        return "Base price is "+str(self.basePrice)+ " and percentage sales tax is "+str(self.percentSalesTax)

    def getTaxAmount(self):
        taxamount = self.basePrice * self.percentSalesTax/100
        print(f'Base price is ${self.basePrice} and Tax amount is ${taxamount:.2f}')

class Toys(Goods):
    def __init__(self, baseprice, percentsalestax):
        super().__init__(baseprice, percentsalestax)

    def __str__(self):
        return "Base price of Toy is"+str(self.basePrice)+ " and  percentage sales tax on toys is "+str(self.percentSalesTax)
