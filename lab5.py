Python 3.9.7 (v3.9.7:1016ef3790, Aug 30 2021, 16:39:15) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> facts_temperature_celcius =  {0: "Freezing point of water.", 100: "Boiling point of water."}
def convert_to_fahrenheit(celcius):
    fahrenheit = ( celcius * 9/5) + 32
    if celcius in facts_temperature_celcius:
        return fahrenheit, facts_temperature_celcius[celcius]
    else:
        return fahrenheit
    
        
def test():
        celcius_list = [0, 25, 50, 100]
        for celcius in celcius_list:
            data = convert_to_fahrenheit(celcius)
            if isinstance(data, tuple):
                print(f'{celcius} degree Celcius = {data[0]} degree Fahrenheit.\n{celcius} degree Celsius is {data[1]}')
            else:
                print(f'{celcius} degree Celcius = {data} degree Fahrenheit.')
            print()
                
test()