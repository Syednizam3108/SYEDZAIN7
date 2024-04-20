zain=(100,200,300,400,500)
shahid=(600,700,800,900,1000)
sanjay=zain+shahid
print(sanjay)
print(type(zain))
print(sanjay*2)
print(zain*2)
print(shahid*2)
print(len(sanjay))
print(max(sanjay))
print(min(sanjay))
print(sum(sanjay))
for i in zain:
    if i in shahid:
        shahid.append(i)
print(shahid)