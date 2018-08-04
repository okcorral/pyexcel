# this script is meant to calculate age
# i/o: input - DOB (Y/M/D)
# i/o: output - age in days

def calculate_age():

    # request user input birthdate 
    year = int(input("What year were you born?  "))
    month = int(input("What month (1-12) were you born?  "))
    day = int(input("What day (1-31) were you born?  "))

    # save to datetime and ordinal types    
    birthdate = dt.date(year, month, day)
    ord_birthdate = birthdate.toordinal()
    
    # def get_today():
    todaydate = dt.date.today()
    ord_todaydate = todaydate.toordinal()
    
    # get_today()
    age_days = ord_todaydate - ord_birthdate
#     year = datetime
    age =  (age_days / 365.25) 
    age_yrs = '{:.2f}'.format(age)
    print("You are", age_days, "days old or", age_yrs, "years old!")  