NAME=str(input('enter ur name:'))
length=len(NAME)
for i in range(length):
    for j in range(length):
        if i==j or i+j==length-1:
            print(NAME[j],end=" ")
        else:
            print(" ",end=" ")
    print()
