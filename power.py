# -*- coding: utf-8 -*-

class Power:
    '''It takes four attributes name, megawatts, age and lifespan has default value of 60 years.
   The class has method capacity, available to calculate capacity of the Power plant and to know availability of power plant respectively.
   It has implemented str and repr method as well'''
    def __init__(self, name, megawatts, age, lifespan = 60):
        self.name = name
        self.megawatts = megawatts
        self.age = age
        self.lifespan = lifespan

    def capacity(self):
        '''
        It calculates capacity of the power plant based on age.

        Returns
        -------
        actual_electricity_amount : int
            DESCRIPTION.

        '''
        actual_electricity_amount = self.megawatts - (self.megawatts / self.lifespan * self.age)
        if actual_electricity_amount > 0:
    actual_electricity_amount = round(actual_electricity_amount)
        else:
            actual_electricity_amount = 0
        return actual_electricity_amount

    def available(self):
        '''
        It returns True if the power plant capacity is positive else it returns False.

        Returns
        -------
        bool
            DESCRIPTION.

        '''
        if self.capacity() > 0:
            return True
        else:
            return False

    def __str__(self):
        return f"{self.name} ({self.capacity()}MW)"

    def __repr__(self):
        return f'Power(name="{self.name}", megawatts={self.megawatts}, age={self.age}, lifespan= {self.lifespan})'



class Wind(Power):
    '''It is subclass of Power class. The default value of lifespan attribute is 25 years.'''
    def __init__(self, name, megawatts, age, lifespan = 25):
        super().__init__(name, megawatts, age, lifespan)


class Nuclear(Power):
    '''It is subclass of Power class. It takes additional one private attribute cooling_towers.
   The subclass has method available implemented to know availability of power plant.'''
    def __init__(self, name, megawatts, age, cooling_towers, lifespan = 60):
        self.__cooling_towers = cooling_towers
        super().__init__(name, megawatts, age, lifespan)


    def available(self):
        '''
        It returns True if capacity is greater then the 100 times cooling towers.

        Returns
        -------
        bool
            DESCRIPTION.

        '''
        if self.capacity() > self.__cooling_towers * 100:
            return True
        else:
            return False

# test function for testing capacity method in Wind class a subclass of Power class.
def test_wind_capacity():
    wind_plant = Wind("Test Wind Plant", 100, 10)
    return wind_plant.capacity() == 60

# test function for testing available method in Wind class a subclass of Power class.
def test_wind_availability():
    wind_plant = Wind("Test Wind Plant", 100, 10)
    return wind_plant.available() == True

# test function for testing capacity method in Nuclear class a subclass of Power class.
def test_nuclear_capacity():
    nuclear_plant = Nuclear("Test Nuclear Plant", 600, 10, 10)
    return nuclear_plant.capacity() == 500

# test function for testing available method in Nuclear class a subclass of Power class.
def test_nuclear_availability():
    nuclear_plant = Nuclear("Test Nuclear Plant", 600, 10, 10)
    return nuclear_plant.available() == False

# test function for testing str() method in Wind class a subclass of Power class.
def tests_str():
    wind_plant = Wind("Test Wind Plant", 100, 0)
    return wind_plant.__str__() == 'Test Wind Plant (100 MW)'


# test function for testing repr method in Nuclear class a subclass of Power class.
def tests_repr():
    nuclear_plant = Nuclear("Test Nuclear Plant", 100, 0, 10)
    return nuclear_plant.__repr__() == 'Power(name="Test Nuclear Plant", megawatts=100, age=0, lifespan=60)'


#Already implemented method
if __name__ == "__main__":
    power_plants = [
        Wind(name="Alta Wind Energy", megawatts=1320, age=12),
        Wind(name="Roscoe Wind Farm", megawatts=781, age=10),
        Wind(name="Shepherds Flat Wind Farm", megawatts=845, age=13),
        Nuclear(name="Palo Verde", megawatts=3942, age=36, cooling_towers=3),
        Nuclear(name="Browns Ferry", megawatts=3300, age=48, cooling_towers=6),
        Nuclear(name="South Texas", megawatts=2560, age=34, cooling_towers=0),
    ]
    available = [_ for _ in power_plants if _.available()]
    order = sorted(available, reverse=True, key=lambda plant: plant.capacity())
    named_list = [str(_) for _ in order]
    print(named_list)
