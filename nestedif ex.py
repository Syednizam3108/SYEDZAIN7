email="syedzain@gmail.com"
password=123456
otp=890799
uemailid=str(input('enter the email id:'))
upassword=int(input('enter the password:'))
if(uemailid==email):
    if(upassword==password):
        print('login success')
        uotp=int(input('enter otp:'))
        if(uotp!=otp):
            print('transaction failed due to invalid otp')
        else:
                print('transaction successful')
    else:
        print('login failed due to incorrect password')
else:
    print('login failed due to incorrect email')
    
