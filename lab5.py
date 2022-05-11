>>> facts_temperature_celcius = {0: "Freezing point of water.", 100: "Boiling point of water."}


def convert_to_fahrenheit(celcius):
    ''' The function converts temperature in degree Celsius  into temperature in
    degree Fahrenheit. It also returns facts about the temperature.'''
    fahrenheit = (celcius * 9/5) + 32
    return fahrenheit, facts_temperature_celcius.get(celcius, "")


def test():
    celcius_temp = float(input("Enter temperature in celsius: "))
    data = convert_to_fahrenheit(celcius_temp)
    if data[1]:
        print(f'{celcius_temp} degree Celcius = {data[0]} degree Fahrenheit.')
    else:
        print(f'{celcius_temp} degree Celcius = {data[0]} degree Fahrenheit.')

test()
