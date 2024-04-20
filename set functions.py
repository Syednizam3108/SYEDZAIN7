my_set = {10, 20, 30, 40, 50}
my_set.add(60)
my_set.remove(30)
my_set.discard(70) 
popped_element=my_set.pop()

another_set = {40, 50, 60, 70, 80}

copied_set = another_set.copy()

my_set.update(another_set)

intersection_set = my_set.intersection(another_set)

union_set = my_set.union(another_set)

difference_set = my_set.difference(another_set)
clear_set=my_set.clear()

print("Modified Set:", my_set)
print("Popped Element:", popped_element)
print("Copied Set:", copied_set)
print("Intersection Set:", intersection_set)
print("Union Set:", union_set)
print("Clear Set:",clear_set)
print("Difference Set:", difference_set)