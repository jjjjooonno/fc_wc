list_ = ['a',3,5]
print(list_[0])
list_.append(7)
print(list_[3])


dic = {'a' : 1, 'b' : 2}
print(dic['a'])
dic.update({'c' : 3})
print(dic['c'])


for item in list_:
	print(item)

for index, item in enumerate(list_):
	print(str(index)+'th item is'+str(item))