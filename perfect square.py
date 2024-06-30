n=int(input())
count=0
for i in range(2,n):
    if n%i==0 and i*i == n:
        count+=1
if count == 1:
    print("perfect")
else:
    print("else")
    
    
