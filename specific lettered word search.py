'''list=[str(x) for x in input().split()]
list1=[]
for i in list:                     #1
    for j in range(len(i)):
        if(i[j]=='s'):
            list1.append(i)
print(list1)'''

z=input('enter string')
for i in z.split():    #perfect without loophole
    if 's' in i.lower():
        print(i,end=' ')
        
'''user=input("enter a string")
print([word for word in user.split() if 's' in word])

x=input('enter string').split()
y=[i for i in o if 's' in i]              #perfect2
print(str(y))'''


