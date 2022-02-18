Python 3.9.7 (v3.9.7:1016ef3790, Aug 30 2021, 16:39:15) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> my_dict = {"HTML":"Hyper Text Markup Language", "CSS": "Cascading Style Sheet", "URL": "Uniform Resource Locator"}
while True:
    term = input("Please enter a term: ")
    if term in my_dict:
        print(my_dict[term])
    else:
        print(f"The term '{term}' you typed is not in the dictionary.")
        option = input("Do you want to add the term in the dictionary? (Y/N): ")
        if option.lower() =="y":
            full_form = input("Please enter the full form: ")
            my_dict[term] = full_form