# Yorm Santi B20240789

# list
#1.1 creating and Modifying a list.
fruits = ['apple', 'banana', 'cherry']
fruits[1] = 'orange'
print("Modified list:", fruits)
#1.2 Accessing Elements using Indexing and Slicing.
numbers = [10, 20, 30, 40, 50]
first = numbers[0]
last = numbers[-1]
sub_list = numbers[1:4]
print("first:", first,"last:", last,"Sublist:", sub_list)
#1.3 List Comprehension.
cubes = [num**3 for num in range(1, 6)]
print("Cubes:", cubes)
#1.4 concatenating and repeating list.
list_a = [1, 2, 3]
list_b = ['a', 'b', 'c']
combined = list_a + list_b
reperted = combined *2
print("Combined:", combined)
print("Reperted:", reperted)
#1.5 Using List Methods.
animals = ['cat', 'dog', 'rabbit']
animals.append('hamster')
animals.insert(1, 'parrot')
animals.remove('cat')
print("Final animals list:", animals)

# tuple
#2.1 creating and unpacking a Tuple.
person = ("Alice", 25,"Wonderland")
name , age, city = person
print("Name:", name, "Age:", age, "City:", city)
#2.2 Tuple concatenation.
fruits = ('apple', 'banana', 'cherry')
colors = ('red', 'green', 'blue')
combined = fruits + colors
print("Combined Tuple:", combined)
#2.3 Reoeat a tuple 
items = ("book","pen")
reperted = items * 3
print("Reperted Tuple:", reperted)
#2.4 Nested Tuples.

nested = (1,(2,3),4)
inner_value = nested[1][0]
print("Inner Value:", inner_value)
#2.5 Returning Multiple Values.

def calculate(a,b):
    return a+b, a*b,a-b
sum_val, product, diff = calculate(8,3)
print("Sum:", sum_val, "Product:", product, "Difference:", diff)

# dictionary
#3.1 Creating and Modifying a Dictionary.
student = {
    'name': 'Bob',
    'age': 20,
    'courses': ['Math', 'Science']
    
}
student['age'] = 21
print("Updated Student:", student)

#3.2 Looping through a Dictionary.
for key , value in student.items():
    print(f"{key}:{value}")
#3.3 Dictionary Comprehension.   
squares = {num: num**2 for num in range(1, 6)}
print("Squares Dictionary:", squares)
#3.4 Merging Dictionaries.
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
merged = {**dict1, **dict2}
print("Merged Dictionary:", merged)
#3.5 Accessing with get() Method.

grade = student.get('grade', 'Not Assigned')
print("Grade:", grade)


# set

#4.1 Creating a Set to remove Deplicates.
numbers = {1, 2,2, 3,4, 4, 5}    
unique_numbers = set(numbers)
print("Unique Numbers:", unique_numbers)
#4.2 Set Operations.
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
print("Union:", set_a.union(set_b))
print("Intersection:", set_a.intersection(set_b))
#4.3 Set Comprehension.
even_numbers = {num for num in range(1, 11) if num % 2 == 0}
print("Even Numbers:", even_numbers)
#4.4 Adding and Removing Elements.
colors = {'red', 'green', 'blue'}
colors.add('yellow')
colors.remove('green')
print("Colors Set:", colors)

#4.5 Checking for Subset and Superset.
set_small ={1,2}
set_large ={1,2,3,4}
print("Is subset:", set_small.issubset(set_large))
print("Is superset:" , set_large.issubset(set_small))

# String
#5.1 Escaping Characters.
message = "Hello, \"World\"!\nNew line here."
print(message)

#5.2 Concatenating and Repeating Strings.
greeting = "Hi"

name = "Alice"
full_greeting = greeting + " " + name
reperted = full_greeting * 2
print("Full Greeting: ", full_greeting)
print("Repeated: ", reperted)
#5.3 slicing a string.
sentence = "I love Python programming"
substring = sentence[7:13]
print ("Substring:",substring)

#5.4 String Methods.
text = "Hello, Python!"
print("Lowercse:", text.lower())
print("Uppercase:",text.upper())
print("Replaced:",text.replace("Python","world"))
print("Find index:",text.find("Python"))

#5.5 String Formatting.
name = "Charlie"
age = 28
city = "Los Angeles"
formatted = f"My name is {name}, I'm {age} years old and I live in {city}."
print(formatted)