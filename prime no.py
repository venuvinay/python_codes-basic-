n=int(input())
count=0
for i in range(2,n):
    if n%i==0:
        count+=1
if count==0 and n!=1:
    print("prime")
else:
    print("not a prime")
    

