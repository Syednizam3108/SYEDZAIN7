def is_prime(num):
    if num<=1:
        return False
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
    return True
def is_leap_year(year):
    if(year%4==0 and year%100!=0)or(year%400==0):
        return True
    else:
        return False
inputs=[]
for i in range(5):
    number=int(input("enter a number:"))
    inputs.append(number)

for number in inputs:
    if is_prime(number):
        print(number,"is a prime number")
    if is_leap_year(number):
        print(number,"is a leap year:")
        

