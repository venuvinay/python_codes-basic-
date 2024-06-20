list3=list(map(int,input().split()))
l=len(list3)
d1=[]
i=0
while(i<l):
    d=list3.count(list3[i])
    if d%2!=0:
        d1.append(list3[i])
        i+=1
print(set(d1))
    
    
