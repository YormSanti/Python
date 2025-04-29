import json

data = {
    "name": "John Doe",
    "age": 30,
    "city": "New York",
    "is_student": False,
    "courses":["python", "java", "c++"],
    
}

json_file = "data.json"

try:
    with open(json_file, 'w') as f:
        json.dump(data, json_file, indent =2)
except PermissionError as e:
    print(f"Permission denied to write to{json_file}")
    
print("Reading data from JSON file")
try:
    with open(json_file,'r') as json_file:
        data = json.load(json_file)
        print('Data from JSON file:')
        print(data)
except FileNotFoundError:
    print(f"File {json_file} not found.")
except json.JSONDecodeError:
    print(f"Error decoding JSON from file {json_file}.")
except PermissionError:
    print(f"Permission denied to read from {json_file}.")