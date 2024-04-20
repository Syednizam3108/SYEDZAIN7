num=int(input("enter no.of lemons:"))
print("equal" if num==21 else "less by {}".format(21-num) if num<21 else "more by{}".format(num-21))