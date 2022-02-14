def fib_number(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        num = 0
        num1 = 1
        n = n -1
        while True:
            numn = num1 + num
            num = num1
            num1 = numn

            n = n-1
            if n == 0:
                break
        return numn









print(fib_number(15))
print(fib_number(1))
print(fib_number(2))
