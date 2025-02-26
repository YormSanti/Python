def get_int_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid integer")
def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid float")





def main_menu():
    print("1.Simples Calculator")
    print("2.String Manipulation")
    print("3.Exit")
    choice = get_int_input("Enter your choice: ")
    if choice == 1:
        simple_calculator()
    elif choice == 2:
        string_manipulation()
    elif choice == 3:
        return
    main_menu()
    
    
    
    
    
def simple_calculator():
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Exit")
    choice = get_int_input("Enter your choice: ")
    if choice == 5:
        return
    num1 = get_float_input("Enter first number: ")
    num2 = get_float_input("Enter second number: ")
    if choice == 1:
        print(f"Result: {num1 + num2}")
    elif choice == 2:
        print(f"Result: {num1 - num2}")
    elif choice == 3:
        print(f"Result: {num1 * num2}")
    elif choice == 4:
        try:
            print(f"Result: {num1 / num2}")
        except ZeroDivisionError as e:
            print("Can not divide by zero")
    simple_calculator()


def string_manipulation():
    print("1.Concatenation")
    print("2.Repetition")
    print("3.Slice")
    print("4.Exit")
    choice = get_int_input("Enter your choice: ")
    if choice == 4:
        return
    if choice == 1:
        str1 = input("Enter first string: ")
        str2 = input("Enter second string: ")
        print(f"Result: {str1 + str2}")
    elif choice == 2:
        str1 = input("Enter string: ")
        num = get_int_input("Enter number of repetitions: ")
        print(f"Result: {str1 * num}")
    elif choice == 3:
        str1 = input("Enter string: ")
        start = get_int_input("Enter start index: ")
        end = get_int_input("Enter end index: ")
        print(f"Result: {str1[start:end]}")
    string_manipulation()
       
    
main_menu()    
   