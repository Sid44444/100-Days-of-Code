

#year =int(input("Which year would you like to check to see if it is a leap year?def is_leap_year(year):
def is_leap_year(year):

    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

print(is_leap_year(int(2000)))#returns True
