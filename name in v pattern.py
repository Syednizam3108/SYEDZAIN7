NAME=str(input('enter ur name:'))
length=len(NAME)
for i in range(length):
    for j in range(length*2):
        if j==i or j==length*2-1-i:
            print(NAME[i],end=" ")
        else:
            print(" ",end=" ")
    print()
