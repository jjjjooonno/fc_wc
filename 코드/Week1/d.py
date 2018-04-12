n = 7
if n > 5:
	print('n is bigger than 5')
else:
	print('n is smaller than or equal to 5')

for number in range(0,10):
	if (number >= 0) and (number < 4):
		print(number,'   ','0 <= number < 4')
	elif (number >= 4) and (number < 7):
		print(number,'   ','4 <= number < 7')
	else:
		print(number,'   ','7 <= number')

for number in range(10,20):
	if number > 15:
		continue
	print(number,'   ','number <= 15')
