list_ = ['a',1,3,5,7]
for number in range(0,5):
	print(number)

for item in list_:
	print(item)

for index, item in enumerate(list_):
	print(str(index+1)+'th item is '+str(item))

n = 0
while n < 10:
	print(n)
	n = n + 1