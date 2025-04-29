import json

def dictionary_load(filename):
    try:
        with open(filename, 'r') as file:
            dictionary = json.load(file)
            return dictionary
    except FileNotFoundError:
        print(f"")