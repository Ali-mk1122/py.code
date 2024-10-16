from c_n_m import Date 

def get_date_input():
    year = int(input("Enter year number: "))
    month = int(input("Enter month number: "))
    day = int(input("Enter day number: "))
    return year, month, day

print("1 : Show date.") 
print("2 : Sum of two dates.") 
print("3 : Get the name of the month.") 
print("4 : Leap year.") 
print("5 : Subtract two dates.") 
print("6 : Date validation.")

try:
    n = int(input("Enter your choice: ")) 
except ValueError:
    print("Invalid input. Please enter a number.")
    exit()

A = Date() 

if n == 1: 
    A.show() 
elif n == 2: 
    t, u, o = get_date_input()
    A.add(t, u, o) 
elif n == 3: 
    b = int(input("Enter month number: ")) 
    print(A.get_month_name(b)) 
elif n == 4: 
    print("Is leap year:", A.is_leap_year()) 
elif n == 5: 
    t, u, o = get_date_input()
    A.sub(t, u, o) 
elif n == 6: 
    print("Is valid date:", A.is_valid_date())
else:
    print("Invalid choice. Please select a valid option.")
