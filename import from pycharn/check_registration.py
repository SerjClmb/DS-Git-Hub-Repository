def register(surname, name, date, middle_name=None, registry=None):

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

    if check_date(date[0], date[1], date[2]) is True:
        registry = (surname, name, middle_name, date[0], date[1], date[2])
        registry_sum.append(registry)
        return registry_sum
    else:
        raise ValueError("Invalid Date!")

registry_sum = list()









reg = register('Petrova', 'Maria', (13, 3, 2003), 'Ivanovna')
reg = register('Ivanov', 'Sergej', (24, 9, 1995), registry=reg)
reg = register('Smith', 'John', (13, 2, 2003), registry=reg)
#reg = register('Ivanov', 'Sergej', (24, 13, 1995), registry=reg)
print(reg)
