This Python code implements a simple bilingual dictionary application that allows users to translate words between English and Persian, manage the dictionary by adding, searching, and removing entries. Here’s a breakdown of the code:

▎Functions:

1. writeindatabase(new):

   • Prompts the user for a Persian translation of the English word passed as new.

   • Appends both the English word and its Persian translation to a file called my_file-4-1.txt.

   • Reads the entire content of the file and returns it.

2. readfromdatabase():

   • Reads all entries from my_file-4-1.txt.

   • Splits the content into lines and organizes it into a list of dictionaries, where each dictionary contains an English word and its corresponding Persian translation.

   • Returns this list.

3. engtopersian(user_string, words):

   • Takes an English string input from the user and translates it to Persian using the words from the database.

   • If a word is not found, it prompts the user to add it to the database by calling write_in_database().

   • Returns the translated Persian string.

4. persiantoeng(user_string, words):

   • Similar to eng_to_persian, but translates from Persian to English.

   • Also adds any missing words to the database.

5. searchfromdatabase(user_string, words):

   • Searches for each word in user_string in both English and Persian dictionaries.

   • Prints the translations if found; otherwise, it informs the user that the word was not found.

6. removefromdatabase(user_string, words):

   • Removes specified words from the database.

   • Reads all lines from the file and rewrites only those that are not in user_string.

   • Prints a message for each entry that is removed.

▎Main Program Logic:

• Welcomes the user and presents options for translating, writing, searching, or removing entries.

• Prompts the user to enter a string for translation or management.

• Calls the appropriate function based on the user's choice:

  • 1: Translate from English to Persian.

  • 2: Translate from Persian to English.

  • 3: Add new entries to the database.

  • 4: Search for translations in the database.

  • 5: Remove entries from the database.

▎Usage Example:

1. If a user inputs "hello" and selects option 1, they will be prompted for its Persian translation. Once provided, both "hello" and its translation will be saved in the file.

2. If they later input "hello" again with option 2, they'll receive its Persian translation if it exists; otherwise, they can add it.

▎Note:

• Ensure that my_file-4-1.txt exists in the same directory as this script before running it, or handle file creation within the script.

• The code does not handle potential exceptions (e.g., file not found) which could be added for robustness.
