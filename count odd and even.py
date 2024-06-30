l=list(map(int,input().split()))
e=0
v=0
for i in l:
    if i%2==0:
        e+=i
    else:
        v+=i
print("sum of even",e)
print("sum of odd",v)
