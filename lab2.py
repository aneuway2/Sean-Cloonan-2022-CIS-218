Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def egg_size():
    """Sean Cloonan, https://foodchannel.com/2010/how-large-is-a-large-egg"""
    x = float(input("Please enter an integer: "))
    if x <= 0:
        print('Egg must weigh more than zero')
    elif  x > 0 and x <= 15:
        print('Your egg size is Pee Wee')
    elif  x > 15 and  x <= 18:
            print('Your egg size is Small')
    elif  x > 18 and x <= 21:
            print('Your egg size is Medium')
    elif  x > 21 and x <= 24:
            print('Your egg size is Large') 
    elif  x > 24 and x <= 27:
            print('Your egg size is Extra Large')
    elif  x > 27:
            print('Your egg size is Jumbo')
    else:
        print('Please use a number')
