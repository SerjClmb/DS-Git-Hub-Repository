def check_date(day, month, year):

    def check_int():
        if type(day) is int and type(month) is int and type(year) is int:
            return True

    def check_range(d, m, y):
        if 1900 <= y <= 2022 and \
                1 <= m <= 12 and \
                1 <= d <= 31:
            return True

    def day_in_month(m):
        if m == 4 or m == 6 or m == 9 or m == 11:
            global month_sum
            month_sum = range(1, 31)
        if m != 4 or m != 6 or m != 9 or m != 11 or m != 2:
            month_sum = range(1, 32)
        if is_leap(year) is True and m == 2:
            month_sum = range(1, 29)
        if is_leap(year) is False and m == 2:
            month_sum = range(1, 30)
            return month_sum

    def check_day_in_month(d):
        if d in day_in_month(month):
                #day_in_month(month).count(d) is True:
            return True

    def is_leap(year):
        if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
            return True
        else:
            return False

    if check_int() is True and check_range(day, month, year) is True and check_day_in_month(day) is True:
        return True
    else:
        return False


month_sum = 0

print(check_date(18, 9, 1999))
print(check_date(29, 2, 2000))
print(check_date(29, 2, 2021))
print(check_date(13, 13, 2021))
print(check_date(13.5, 12, 2021))
