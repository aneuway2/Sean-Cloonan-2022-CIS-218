my_string =  input("Type xxx here: ")
vowels = ["a","e","i", "o", "u"]
upper_case_letters,lower_case_letters,spaces,digit,punctuation,vowel =(0,0,0,0,0,0)
for char in my_string:
    if(char.isalpha()):
        if(char.isupper()):
            upper_case_letters +=1
            if char.lower() in vowels:
                vowel += 1
        elif (char.islower()):
            lower_case_letters += 1
            if char in vowels:
                vowel += 1
    elif (char.isdigit()):
        digit += 1
    elif char == " ":
        spaces += 1
    else:
        punctuation += 1
print(f"Upper Case letters: {upper_case_letters}\nLower case letters: {lower_case_letters}\nSpaces: {spaces}\nDigits: {digit}\nPunctuation: {punctuation}\nVoels: {vowel}")