a = int(input('a '))
b = int(input('b '))
c = int(input('c '))
res_a = 1 if a < 45 < b and 45 < c else 0
res_b = 1 if b < 45 < a and 45 < c else 0
res_c = 1 if c < 45 < a and 45 < b else 0
if res_a + res_b + res_c == 1:
	print('True')
else:
	print('False')
