l=list(map(int,input().split()))
v=l
v1=0
c=0
count=0
for i in v:
    for j in range(2,i):
        if i%j==0:
            count+=1
        if count==0 and i!=1:
            v1+=1
        else:
            c+=1
print("prime no:",v1)
