class Date:
    def __init_(self,day,month,year):
        self.day = day
        self.month = month
        self.year = year

        
    def show(self):
        print(self.year,"/",self.month,"/",self.day)
        break


    def add(self):
        s = int(input("year num 1"))
        f = int(input("month num 1"))
        g = int(input("day num 1 "))
        print(s,"/",f,"/",g)
        t = int(input("year num 2"))
        u = int(input("month num 2"))
        o = int(input("day num 2"))
        print(t,"/",u,"/",o)
        year_new = s + t
        month_new = f + u
        day_new = g + o
        if day_new > 30 :
           m_new = month_new + 1
        elif month_new > 12 :
           y_new = year_new  + 1
           print(y_new,"/",m_new,"/",day_new)
        else :
            print(year_new_new,"/",month_new_new,"/",day_new)
            break


    def get_month_name(self,b):
        b =int(input("enter month number:  "))
        if   b == 1 :
            print("January")
        elif b == 2 :
            print("Fesbruary")
        elif b == 3 :
            print("march")
        elif b == 4 :
            print("April")
        elif b == 5 : 
            print("May")
        elif b == 6 :
            print("June")
        elif b == 7 :
            print("July")
        elif b == 8 :
            print("August")
        elif b == 9 :
            print("September")
        elif b == 10 :
            print("October")
        elif b == 11 :
            print("November")
        elif b == 12 :
            print("December")
        else :
            print("not found")
            break


    def is_leep_year():
        year_one = int(input("enter year  "))
        leep_one = year_one / 30
        l = [2,5,7,10,13,16,18,21,24,26,29]
        if leep_one == l :
            print("true")
        else :
            print("false")         
            break 


    def sub():
        s = int(input("year num 1"))
        f = int(input("month num 1"))
        g = int(input("day num 1 "))
        print(s,"/",f,"/",g)
        t = int(input("year num 2"))
        u = int(input("month num 2"))
        o = int(input("day num 2"))
        print(t,"/",u,"/",o)
        year_new = s - t
        month_new = f - u
        day_new = g - o
        if day_new < 1 :
           m_new = month_new - 1
        elif month_new < 1 :
           y_new = year_new  - 1
           print(y_new,"/",m_new,"/",day_new)
        
        
    def is_valid_date():
        A = int(input(" enter year "))
        B = int(input("enter month "))
        C = int(input("enter day "))
        if  1<A>9999:
            ...
        elif 1<B>12:
            print("True")
        elif 1<C>30:
            print("True")
        else:
            print("False")
            break              


a = Date
z = a.get_month_name
# a.add()