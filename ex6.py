'''num1=int(input('enter the num1'))
num2=int(input('enter the num2'))
if(num1>num2):
    print(num1,' is greater ')
elif(num1==num2):
    print('both are equal')
else:
    print(num2,' is greater ')'''
    
    
#useing ternary operater

'''num1=int(input('enter the num1 '))
num2=int(input('enter the num2 '))
print('num1 is greater ' if num1>num2 else 'num2 is greate ')'''


a=5
b=6
c=3
print('a' if a>b and a>c else 'b' if b>c else 'c')
