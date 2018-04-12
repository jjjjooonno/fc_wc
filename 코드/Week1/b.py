list_ = ['a',3,5]
list_[0]
list_.append(7)
list_[3]


dic = {'a' : 1, 'b' : 2}
dic['a']
dic.update({'c' : 3})
dic['c']


for item in list_:
	print(item)

for index, item in enumerate(list_):
	print(str(index)+'th item is'+str(item))