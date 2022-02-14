def check_date(day, month, year):
    month_of_30 = [4, 6, 9, 11]
    month_sum = 0

    def is_leap(year):
        if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
            return True
        else:
            return False

    if type(day) is int and type(month) is int and type(year) is int:
        if 1900 <= year <= 2022:
            if 1 <= month <= 12:
                if 1 <= day <= 31:
                    if month_of_30.count(month) > 0:
                        month_sum = range(1, 31)
                    else:
                        month_sum = range(1, 32)
                        if is_leap(year) is True and month == 2:
                            month_sum = range(1, 30)
                        elif is_leap(year) is False and month == 2:
                            month_sum = range(1, 29)
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False

    if day in month_sum:
        return True
    else:
        return False


print(check_date(18, 9, 1999))
print(check_date(29, 2, 2000))
print(check_date(29, 2, 2021))
print(check_date(13, 13, 2021))
print(check_date(13.5, 12, 2021))
