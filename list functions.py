my_list = [11, 22, 33, 44, 55]

my_list.append(66)
print(my_list)

my_list.extend([77, 88, 99])
print(my_list)  

my_list.insert(2, 10)
print(my_list)

my_list.remove(22)
print(my_list)

popped_element = my_list.pop()
print(popped_element)  
print(my_list)


index = my_list.index(33)
print(index)  

count = my_list.count(10)
print(count)  

my_list.sort()
print(my_list)

my_list.clear()
print(my_list)  



