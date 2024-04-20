Name=str(input('enter ur name:'))
length=len(Name)
for i in range(length):
    for j in range(length):
        if i==0 or i==length or i==length-1 or i+j==length-1:
            print(Name[j],end=" ")
        else:
            print(" ",end=" ")
    print()