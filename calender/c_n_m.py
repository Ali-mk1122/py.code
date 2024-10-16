class Date:
    def __init__(self, year=2024, month=7, day=6):
        self.year = year
        self.month = month
        self.day = day

    def show(self):
        print(f"{self.year}/{self.month}/{self.day}")

    def add(self, t, u, o):
        print(f"Current Date: {self.year}/{self.month}/{self.day}")
        print(f"Adding: {t}/{u}/{o}")

        year_new = self.year + t
        month_new = self.month + u
        day_new = self.day + o

        
        if day_new > 30:
            day_new -= 30
            month_new += 1

        
        if month_new > 12:
            month_new -= 12
            year_new += 1

        print(f"New Date: {year_new}/{month_new}/{day_new}")
        return year_new, month_new, day_new

    def get_month_name(self):
        month_names = {
            1: 'فروردین', 2: 'اردیبهشت', 3: 'خرداد', 4: 'تیر',
            5: 'مرداد', 6: 'شهریور', 7: 'مهر', 8: 'آبان',
            9: 'آذر', 10: 'دی', 11: 'بهمن', 12: 'اسفند'
        }
        return month_names.get(self.month, "Not found")

    def is_leap_year(self):
        if (self.year % 4 == 0 and self.year % 100 != 0) or (self.year % 400 == 0):
            print(f"{self.year} is a leap year")
            return True
        else:
            print(f"{self.year} is not a leap year")
            return False

    def sub(self, t, u, o):
        print(f"Current Date: {self.year}/{self.month}/{self.day}")
        print(f"Subtracting: {t}/{u}/{o}")

        year_new = self.year - t
        month_new = self.month - u
        day_new = self.day - o

        
        if day_new < 1:
            day_new += 30
            month_new -= 1

        
        if month_new < 1:
            month_new += 12
            year_new -= 1

        print(f"New Date: {year_new}/{month_new}/{day_new}")
        return year_new, month_new, day_new

    def is_valid_date(self):
        valid_year = 1 <= self.year <= 9999
        valid_month = 1 <= self.month <= 12
        valid_day = 1 <= self.day <= 30  

        if valid_year and valid_month and valid_day:
            print("True")
            return True
        else:
            print("False")
            return False


# date = Date()
# date.show()
# date.add(1, 0, 5)
# date.sub(0, 1, 6)
# print(date.get_month_name())
# date.is_leap_year()
# date.is_valid_date()
