'''n=[10,25,37,40,57,65]
for i in n:
    if i%10==7:
        print(i)'''

'''n=[10,20,30,40,30,50,60,50,40]
y=[]
for i in n:
    if i not in y:
        y.append(i)
    print(y)'''

shahid=[]
n=int(input('enter the size of list :'))
for i in range(0,n):
    e=input('enter the elements :')
    shahid.append(e)
print(shahid)

sanjay=[]
n=int(input('enter the size of list :'))
for i in range(0,n):
    e=input('enter the elements :')
    sanjay.append(e)
print(sanjay)

for i in shahid:
    for j in sanjay:
        if i==j:
            print(i)

            
