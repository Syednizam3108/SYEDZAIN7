x=()
y=()
n1=int(input('enter a size'))
for i in range(0,n1):
    ele=int(input('enter the elements'))
    x.append(ele)
n2=int(input('enter b size'))
for i in range(0,n2):
    ele=int(input('enter the elements'))
    y.append(ele)
for i in x:
    if i in y:
        print(i)