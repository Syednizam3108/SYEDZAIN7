email="syed@gmail.com"
psw=123456
uemail=str(input("enter the email"))
upsw=int(input("enter the psw"))
if(email==uemail):
    if(psw==upsw):
        print("login success")
    else:
        print("login faied due to incorrect psw")
else:
    print("login failed due to incorrect email")