
import datetime
from calendar import isleap
def get_month_days(month,year):
    if month in [n for n in range(1,13)]:
        if month in [1,3,5,7,8,10,12]:
            return 31
        elif month in [4,6,9,11]:
            return 30
        elif month==2 and isleap(year):
            return 29
        else:
            return 28
    else:
        return -1


def get_week_day(date):
    if type(date)==type(" "):
        L=date.split("-")
        date=int(L[0])
        month=int(L[1])
        year=int(L[2])
        days=get_month_days(month,year)

        if date<=days:
            week_days=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
            week_num=datetime.date(year,month,date).weekday()
            day=week_days[week_num]
            return day
        else:
            print("Given day or month is not in the range")
    else:
        raise TypeError("Date must be string format")

if __name__=="__main__":
    date=input("Enter the date(DD-MM-YYYY)")
    day=get_week_day(date)
    print("Week day is : ",day)




