import json

def load_dictionary(filename):
    try:
        with open(filename,'r') as file:
            dictionary = json.load(file)
            return dictionary
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        print("Error: Invalid JSON format")
        return {}
    
def save_dictionary(dictionary, filename):
    try:
        with open(filename,'w') as file:
            json.dump(dictionary, file, indent=2)
    except PermissionError:
        print(f"Error: Permission denied to write to {filename}")

def add_word(dictionary, word, meaning):
    dictionary[word.lower()] = meaning

def lookup_word(dictionary, word):
    word = word.lower()
    # using get method to return a default value if word is not found
    return dictionary.get(word, f"Word '{word}' not found in dictionary")

def display_dictionary(dictionary):
    print("\nDictionary:")
    for word, meaning in dictionary.items():
        print(f"{word}: {meaning}")

def main():
    filename = "dictionary.json"
    dictionary = load_dictionary(filename)
    while True:
        print("\n1. Add word")
        print("2. Lookup word")
        print("3. Display dictionary")
        print("4. Save and exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            word = input("Enter word: ")
            meaning = input("Enter meaning: ")
            add_word(dictionary, word, meaning)
        elif choice == '2':
            word = input("Enter word: ")
            print(lookup_word(dictionary, word))
        elif choice == '3':
            display_dictionary(dictionary)
        elif choice == '4':
            save_dictionary(dictionary, filename)
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()