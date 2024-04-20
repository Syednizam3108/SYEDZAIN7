email="syed@gmail.com"
psw=123456
otp=7861
uemail=str(input("enter the email"))
upsw=int(input("enter the psw"))
uotp=int(input("enter the otp"))
if(email==uemail and psw==upsw):
    print("login success")
    if(otp==uotp):
        print("transaction is successfull")
    else:
        print("otp is wrong")
else:
    print("login failed")
