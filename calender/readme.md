---

The Date class you created is designed for managing dates. Below, I will explain each of the methods and functionalities of this class in detail:

▎1. __init__ Method

This method is the constructor of the class, which is called when a new object of the Date class is created. The default parameters for year, month, and day are set to 2024, 7, and 6, respectively.

▎2. show Method

This method displays the current date in the format year/month/day.

▎3. add Method

This method is used to add years, months, and days to the current date.

• It first prints the current date and the new values to be added.

• Then, it calculates the new year, month, and day.

• If the new day exceeds 30, it rolls over to the next month and adjusts the day.

• If the new month exceeds 12, it rolls over to the next year and adjusts the month.

• Finally, it prints and returns the new date.

▎4. get_month_name Method

This method returns the name of the current month in Persian. It uses a dictionary to map month numbers to their corresponding names.

▎5. is_leap_year Method

This method checks whether the current year is a leap year or not.

• A year is considered a leap year if it is divisible by 4 but not divisible by 100, or if it is divisible by 400.

▎6. sub Method

This method is used to subtract years, months, and days from the current date.

• Similar to the add method, it first prints the current date and the values to be subtracted.

• Then, it calculates the new year, month, and day.

• If the new day is less than 1, it rolls back to the previous month and adjusts the day.

• If the new month is less than 1, it rolls back to the previous year and adjusts the month.

• Finally, it prints and returns the new date.

▎7. is_valid_date Method

This method checks whether the current date is valid or not.

• The year must be between 1 and 9999, the month between 1 and 12, and the day between 1 and 30 (which has been simplified here).

• If all conditions are met, it prints and returns "True"; otherwise, it prints and returns "False".

▎Example Usage

At the end of the code, an object of the Date class is created, and several of its methods are called:

• Displaying the current date

• Adding 1 year and 5 days

• Subtracting 1 month and 6 days

• Displaying the name of the current month

• Checking if the year is a leap year

• Checking if the date is valid

This class provides a simple way to manage dates, and you can extend or modify it further as needed.

--- 

\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

---

This code is an interactive menu for using the Date class, allowing the user to perform various operations on dates. Below is an explanation of the different components of the code:

▎Code Explanation

1. Importing the Date Class:
      from c_n_m import Date
   
   This line imports the Date class from the c_n_m module.

2. Defining the get_date_input Function:
      def get_date_input():
       year = int(input("Enter year number: "))
       month = int(input("Enter month number: "))
       day = int(input("Enter day number: "))
       return year, month, day
   
   This function prompts the user for the year, month, and day, and returns them as a tuple.

3. Displaying the Menu:
      print("1 : Show date.") 
   print("2 : Sum of two dates.") 
   print("3 : Get the name of the month.") 
   print("4 : Leap year.") 
   print("5 : Subtract two dates.") 
   print("6 : Date validation.")
   
   This section displays various options for the user.

4. Getting User Input:
      try:
       n = int(input("Enter your choice: ")) 
   except ValueError:
       print("Invalid input. Please enter a number.")
       exit()
   
   This part receives user input and displays an error message if the input is invalid, terminating the program.

5. Creating an Instance of the Date Class:
      A = Date()
   
   An instance of the Date class named A is created.

6. Operations Based on User Selection:
   The next section includes several conditions (if, elif) that perform different operations based on the user's selection:

   
   • Option 1: Display the current date.

   
   • Option 2: Sum two dates.

   
   • Option 3: Get the name of a specific month.

   
   • Option 4: Check if the current year is a leap year.

   
   • Option 5: Subtract two dates.

   
   • Option 6: Validate a date.

7. Handling Invalid Selections:
      else:
       print("Invalid choice. Please select a valid option.")
   
   If the user selects an option outside the available range, an error message is displayed.


▎Overall, this code serves as a useful tool for working with dates and can achieve better functionality with some improvements.

--- 
