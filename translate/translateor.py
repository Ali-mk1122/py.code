import os

def write_in_database(new):
    new_persian = input(f"Enter translation for '{new}': ")
    with open("my_file-4-1.txt", "a") as f:
        f.write(f"{new}\n{new_persian}\n")
    
    with open("my_file-4-1.txt", "r") as f:
        big_text = f.read()
    
    return big_text


def read_from_database():
    print("Loading...")

    with open("my_file-4-1.txt", "r") as f:
        big_text = f.read()

    parts = big_text.split("\n")
    words = []
    
    for i in range(0, len(parts) - 1, 2):
        my_dict = {"english": parts[i], "persian": parts[i + 1]}
        words.append(my_dict)

    return words


def eng_to_persian(user_string, words):
    user_words = user_string.split(" ")
    output_text = ''
    for user_word in user_words:
        for word in words:
            if word["english"] == user_word:  # word found
                output_text += word["persian"] + ' '
                break
        else:
            output_text += user_word + ' '
            write_in_database(user_word)
    
    return output_text.strip()


def persian_to_eng(user_string, words):
    user_words = user_string.split(" ")
    output_text = ''
    for user_word in user_words:
        for word in words:
            if word["persian"] == user_word:  # word found
                output_text += word["english"] + ' '
                break
        else:
            output_text += user_word + ' '
            write_in_database(user_word)
    
    return output_text.strip()


def search_from_database(user_string, words):
    user_words = user_string.split(" ")
    for user_word in user_words:
        found = False
        for word in words:
            if user_word == word["english"] or user_word == word["persian"]:
                print(word["english"], word["persian"])
                found = True
                break
        if not found:
            print(f"'{user_word}' not found.")


def remove_from_database(user_string, words):
    user_words = user_string.split(" ")
    with open("my_file-4-1.txt", "r") as f:
        lines = f.readlines()

    with open("my_file-4-1.txt", "w") as f:
        for i in range(0, len(lines) - 1, 2):
            if lines[i].strip() not in user_words and lines[i + 1].strip() not in user_words:
                f.write(lines[i])
                f.write(lines[i + 1])
            else:
                print(f"Removing '{lines[i].strip()}' - '{lines[i + 1].strip()}'")


# Main program
print("Welcome dear user, please enter your text:")

options = """
1 = English to Persian
2 = Persian to English
3 = Write in database
4 = Search from database
5 = Remove from database
"""
print(options)

user_string = input("Enter your string: ")
words = read_from_database()

d = input("Enter your choice: ")

if d == "1":
    result = eng_to_persian(user_string, words)
    print(result)
elif d == "2":
    result = persian_to_eng(user_string, words)
    print(result)
elif d == "3":
    result = write_in_database(user_string)
    print(result)
elif d == "4":
    search_from_database(user_string, words)
elif d == "5":
    remove_from_database(user_string, words)
else:
    print("Invalid option!")