def is_leap(year):
    if year % 4 == 0:
        if year % 100 ==0:
            if year % 400 == 0: #4000 amended to 400
                return True
            else:
                return False
        else:
            return True
    else:
        return False

print(is_leap(2000))