d={}
for i in range(4):
    key=input("enter key")
    value=input("enter value")
    d[key]=value
keys1=input("enter key to remove")
d.pop(keys1)
print(d)
