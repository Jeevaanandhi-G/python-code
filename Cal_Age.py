from datetime import datetime 
a= input("enter the DOB (dd-mm-yyyy):")
s= a.split('-')
birth_day = int(s[0])
birth_mon = int(s[1])
birth_year = int(s[2])
today = datetime.today()
current_day = today.day
current_mon = today.month
current_year = today.year
def date():
    age = current_year - birth_year
    if (current_mon < birth_mon) or ( current_mon== birth_mon and current_day < birth_day):
        age -=1
    return age  

final_age=date()
print("The age is :",final_age)
