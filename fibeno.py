n=int(input("enter number"))
a,b=0,1
for i in range(n):
    print(a,sep="  ")
    a,b=b,a+b
    
