Python 3.9.7 (v3.9.7:1016ef3790, Aug 30 2021, 16:39:15)
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> facts_temperature_celcius =  {0: "Freezing point of water.", 100: "Boiling point of water."}
def convert_to_fahrenheit(celcius):
    ''' The function converts temperature in degree Celsius  into temperature in
    degree Fahrenheit. It also returns facts about the temperature.'''
    fahrenheit = (celcius * 9/5) + 32
    return fahrenheit, facts_temperature_celcius.get(celcius, "")

def test():
    celcius_temp = float(input("Enter temperature in celsius: "))
    data = convert_to_fahrenheit(celcius_temp)
    if data[1]:
        print(f'{celcius_temp} degree Celcius = {data[0]} degree Fahrenheit.\n{celcius_temp} degrees Celsius is {data[1]}')
    else:
        print(f'{celcius_temp} degree Celcius = {data[0]} degree Fahrenheit.')

test()