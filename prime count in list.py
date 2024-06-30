def prime1(n):
    count=0
    co=0
    v1=0
    for i in range(2,n):
        if n%i==0:
            count+=1
    if count==0 and n!=1:
        co+=1
        
    else:
        v1+=1
    
l=list(map(int,input().split()))
v=l
for i in range(len(v)):
    prime1(v[i])

    


            
