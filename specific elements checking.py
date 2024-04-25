a={'balaji':10,'banana':20,'mango':30,'bhaskar':40}
for key, value in a.items():
    if key[3].lower()=='a':
        print(f"the value of'{key}' is {value}")
