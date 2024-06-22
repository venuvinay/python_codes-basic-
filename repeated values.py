d={}
for i in range(4):
    key=input("enter key")
    value=input("enter value")
    d[key]=value
key=input("enter key to search")
if key in d.keys():
    print("key found")
else:
    print("key not founded")
