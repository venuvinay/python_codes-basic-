d={}
for i in range(4):
    key=input("enter key")
    value=input("enter value")
    d[key]=value
print(d.setdefault('n'))
print(d)
