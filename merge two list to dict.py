l1=list(map(int,input("list1").split()))
l2=list(map(int,input("list2").split()))
d={}
for i in range(len(l1)):
    g=l1[i]
    f=l2[i]
    d[g]=f
print(d)
