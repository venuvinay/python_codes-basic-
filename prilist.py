l=list(map(int,input().split()))
b=list()
c=list()
for i in l:
    count=0
    for j in range(2,i):
        if i%j==0:
            count+=1
    if count == 0 and i!=1:
        b.append(i)
    else:
        c.append(i)
print("count of prime no",len(b))
        
        
        
