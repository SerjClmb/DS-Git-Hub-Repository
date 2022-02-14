def is_leap(year):
    if year % 400 == 0 or year % 4 ==0 and year % 100 !=0:
        return True
    else:
        return False


print(is_leap(2000))
print(is_leap(1900))
print(is_leap(2020))