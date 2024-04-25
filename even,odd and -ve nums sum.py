a=[2,4,1,-3,-5,7]
sum1=0
sum2=0
sum3=0
for num in a:
    if num<0:
        sum1+=num
    elif num%2==0:
        sum2+=num
    else:
        sum3+=num
print('sum of -ve nums:',sum1)
print('sum of even numbers:',sum2)
print('sum of odd numbers:',sum3)

    
