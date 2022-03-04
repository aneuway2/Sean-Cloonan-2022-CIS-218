Python 3.9.7 (v3.9.7:1016ef3790, Aug 30 2021, 16:39:15) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Function 1
def bmi_calculator(height, weight):
    ''' BMI is calculated using formula as below-
    BMI = (weight (lb) ÷ height2 (in)) * 703 '''
    bmi = (weight / height** 2) * 703
    return bmi

#Fucntion 2
def weight_category(bmi):
    ''' Weight Category is calculated as per below chart-
    BMI Categories:
    Underweight = <18.5
    Normal weight = 18.5–24.9
    Overweight = 25–29.9
    Obesity = BMI of 30 or greater '''
    if bmi < 18.5:
        weight_cat = "Underweight"
    elif bmi >= 18.5 and bmi < 25:
        weight_cat = "Normal"
    elif bmi >= 25 and bmi < 30:
        weight_cat = "Overweight"
    else:
        weight_cat = "Obese"
    return weight_cat

#Function 3
def test_bmi_calculator(height, weight):
    bmi =  bmi_calculator(height, weight)
    height_ft = height // 12
    height_inch =  height % 12
    print(f'A {height_ft:.0f}\'{height_inch:.0f}" person with a weight of {weight} pound has a BMI of {bmi:.2f}.' )
    
#Function 4
def test_weight_category(height, weight):
    bmi =  bmi_calculator(height, weight)
    weight_cat = weight_category(bmi)
    print(f'You are in {weight_cat} category with BMI of {bmi:.2f}.')
    
height = float(input("height (in inches)? "))
weight = float(input("weight (in pounds)? "))
test_bmi_calculator(height, weight)
test_weight_category(height, weight)