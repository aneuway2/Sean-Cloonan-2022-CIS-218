def egg_size():
    """Sean Cloonan, https://foodchannel.com/2010/how-large-is-a-large-egg"""
    gram_to_ounce_factor = 1/28.35 # 1 ounce = 28.34952 gram (Approximating 28.34952 to 28.35)
    while True:   
        scale = input("Scale for weight of Eggs-\nGrams- g \nOunce - oz\n")
        if scale.lower() in["g","oz"]:
            break
        print("Please enter appropriate scale.")
    while True:
        x = float(input("Enter weight of egg in the scale as selected: "))
        if scale == "g":
            x = float(x) * gram_to_ounce_factor
        if x <= 0:
            print('Egg must weigh more than zero')
        elif x <= 15:
             print('Your egg size is Pee Wee')
        elif x <= 18:
            print('Your egg size is Small')
        elif x <= 21:
            print('Your egg size is Medium')
        elif x <= 24:
            print('Your egg size is Large') 
        elif x <= 27:
            print('Your egg size is Extra Large')
        else:
            print('Your egg size is Jumbo')

# Added by Andrew Bowman to enable running this lab with the terminal command:
#   python lab2.py
egg_size()
