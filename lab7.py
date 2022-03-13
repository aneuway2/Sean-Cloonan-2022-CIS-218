# Function 1
def bmi_calculator(height, weight):
    ''' BMI is calculated using formula as below-
    BMI = (weight (lb) ÷ height2 (in)) * 703 '''
    bmi = (weight / height** 2) * 703
    return bmi

# Function 2
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

# Function 3
def test_bmi_calculator():
    ''' Function tests BMI based on height and weight of the person.
    Person height is in inches and weight in pounds'''
    person_height_width = [(74, 200), (70, 220), (76, 170), (69, 240), (68, 160)]
    for person_detail in person_height_width:
        height = person_detail[0]
        weight = person_detail[1]
        bmi = bmi_calculator(height, weight)
        height_ft = height // 12
        height_inch = height % 12
        print(f'A {height_ft:.0f}\'{height_inch:.0f}" person with a weight of {weight} pound has a BMI of {bmi:.2f}.')

# Function 4
def test_weight_category():
    ''' Function tests weight category based on BMI of the person'''
    bmi_list = [16, 17, 18, 18.5, 19, 19.8, 20.6, 24.9, 25, 26, 27, 29.9, 30, 31.2, 32, 34.6]
    for bmi in bmi_list:
        weight_cat = weight_category(bmi)
        print(f'You are in {weight_cat} category with BMI of {bmi:.2f}.')

test_bmi_calculator()
test_weight_category()
