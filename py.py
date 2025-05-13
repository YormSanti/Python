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




def main():
    while True:
        print("1.Enter your name")
        print("2.Enter your age")
        print("3.Enter your id")
        print("4.Exit")
        choice = get_int_input("Enter your choice: ")
        if choice == 1:
           name()
        elif choice == 2:
            age()
        elif choice == 3:
            id()
        elif choice == 4:
            print("Goodbye")
            break
        
            
        else:
            print("Invalid choice")

def name():
    print("Enter your name")
    name = input("Enter Your Name: ")
    print(f"Your name is {name}")
def age():
    print("Enter your age")
    age = input("Enter Your Age: ")
    print(f"Your age is {age}")
def id():    
    print("Enter your id")
    id = input("Enter Your ID: ")
    print(f"Your ID is {id  }")    
        
main()        