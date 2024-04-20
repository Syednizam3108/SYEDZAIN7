def Zain():
    return "this is my bank balance"
test_dict={"fname":Zain,"age":22,"address":"Hubli"}
print("the original dictionary is:"+str(test_dict))
res=test_dict['fname']()
print("the required call result:"+str(res))