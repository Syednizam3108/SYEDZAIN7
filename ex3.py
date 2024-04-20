email="syed@gmail.com"
psw=123456
uemail=str(input("enter the email"))
upsw=int(input("enter the psw"))
if(email==uemail and psw==upsw):
    print("login success")
else:
    print("login failed")