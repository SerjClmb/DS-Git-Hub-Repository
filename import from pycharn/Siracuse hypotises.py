n = 1000
t = 0
while True:
    if n % 2 == 0:
        n = n // 2
        t += 1
        if n == 1:
            print('Syracuse hypotesis holds')
            break
        else:
            print(t)
    else:
        n = (n * 3 + 1) // 2
        t += 1
        if n == 1:
            print('Syracuse hypotesis holds')
            break
        else:
            print(t)
