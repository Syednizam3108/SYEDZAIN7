class Node:
    def __init__(self, data):
       self.data = data
       self.next = None
 
 
class LinkedList:
    def __init__(self):
        self.head = None
        self.last_node = None
 
    def append(self, data):
        if self.last_node is None:
            self.head = Node(data)
            self.last_node = self.head
        else:
            self.last_node.next = Node(data)
            self.last_node = self.last_node.next
 
def is_equal(lilist1, lilist2):
    current1 = lilist1.head
    current2 = lilist2.head
    while (current1 and current2):
        if current1.data != current2.data:
            return False
        current1 = current1.next
        current2 = current2.next
    if current1 is None and current2 is None:
        return True
    else:
        return False
 
def is_greater(lilist1, lilist2):
    current1 = lilist1.head
    current2 = lilist2.head
    while (current1 and current2):
        if current1.data > current2.data:
            return True
        else:
            return False
        current1 = current1.next
        current2 = current2.next
    if current1 is None and current2 is None:
        return True
    else:
        return False

 
lilist1 = LinkedList()
lilist2 = LinkedList()
 
data_list = input('Please enter the elements in the first linked list: ').split()
for data in data_list:
    lilist1.append(int(data))
 
data_list = input('Please enter the elements in the second linked list: ').split()
for data in data_list:
    lilist2.append(int(data))
 
if is_equal(lilist1,lilist2):
    print('The lilist1 is equal to lilist2')
elif is_greater(lilist1, lilist2):
    print('The lilist1 is greater than lilist2.')
else:
    print('The lilist1 is not greater than lilist2', end = '')
    

