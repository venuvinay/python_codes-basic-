d1={}
for i in range(4):
    key=input("enter key d1")
    value=input("enter value d1")
    d1[key]=value
d2={}
for i in range(4):
    key=input("enter key d2")
    value=input("enter value d2")
    d2[key]=value
d1.update(d2)
print(d1)
