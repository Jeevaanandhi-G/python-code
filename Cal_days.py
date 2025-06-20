from datetime import date ,timedelta
a = input('enter your DOB')
s = a.split('-')
birth_date= int(s[0])
birth_mon= int(s[1])
birth_year= int(s[2])
today= date.today()
current_date= today.day
current_mon = today.month
current_year = today.year
def days():
    if(current_mon < birth_mon) or (current_mon==birth_mon and current_date < birth_date):
        print("still comming")
        birthday=date(current_year,birth_mon,birth_date)
        k = birthday - today
        print(k.days)
    elif(current_mon ==birth_mon and current_date == birth_date):
        print('this is your birthday')
    else:
        print("your birthday passed")    
days()