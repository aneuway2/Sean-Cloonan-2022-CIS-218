class Person:
    '''It takes two private attributes name and age. It has setters and getters method implemented for both the private attributes.
    The class has metods _str_  and _repr_ implemented. Further, methods__eq__ and _lt_ are implemented
     for sorting purpose based on age.'''
    # Constructor of the class
    def __init__(self, name, age):
        # Private attributes
        self.__name = name
        self.__age = age
     # Getters  for name
    def get_name(self):
        return self.__name

    # Setters  for name
    def set_name(self, p_name):
        self.__name = p_name

    # Getters  for age
    def get_age(self):
        return self.__age

    # Setters  for name
    def set_age(self, p_age):
        self.__age = p_age

    def __str__(self):
        return f"Name of Person is {self.__name} and  he is {self.__age} years old."

    def __repr__(self):
        return f'Person({self.__name}, {self.__age})'

    def __eq__(self, other):
        '''
        Parameters
        ----------
        Two instance of the class.
        ----------
        Equality of the objects are compared on age.
        '''
        return self.__age == other.__age

    def __lt__(self, other):
        '''
        Parameters
        ----------
        Two instance of the class.
        ----------
        Two objects are compared on age.
        '''
        return self.__age < other.__age


class Student(Person):
    '''It is subclass of Person class. It takes additional two private attributes point earned and credit taken.
    The subclass has method calc_gps implemented to caculate gps. The subclass has metods _str_  and _repr_ implemented. Further, methods__eq__ and _lt_ and _ge_ are implemented
     for comparison purpose based on gpa.'''
    def __init__(self, name, age, point, credit):
        self.__point = point
        self.__credit = credit
        super().__init__(name, age)

    def calc_gpa(self):
        return self.__point/self.__credit

    def __str__(self):
        return f"Name of Student is {self.get_name()} and  his gpa is {self.calc_gpa()}."

    def __repr__(self):
        return f'Person({self.get_name()}, {self.get_age()}, {self.__point}, {self.__credit})'

    def __eq__(self, other):
        '''
        Parameters
        ----------
        Two instance of the class.
        ----------
        Equality of the objects are compared on gpa.
        '''
        return self.calc_gpa() == other.calc_gpa()

    def __lt__(self, other):
        '''
        Parameters
        ----------
        Two instance of the class.
        ----------
        Two objects are compared on gpa.
        '''
        return self.calc_gpa() < other.calc_gpa()

    def __ge__(self, other):
        '''
        Parameters
        ----------
        Two instance of the class.
        ----------
        Two objects are compared on gpa.
        '''
        return self.calc_gpa() >= other.calc_gpa()

# test cases for testing all implemented methods in Person class.
person1 = Person("Sean", 18)
person2 = Person("Jennifer", 20)
persons = [person2, person1]
sorted(persons)

# test cases for testing all implemented methods in Student class a subclass of Person class.
student1 = Student("Sean", 22, 19, 5)
student2 = Student("Andrew", 24, 18, 6)
