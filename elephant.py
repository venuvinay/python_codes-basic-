n=int(input("enetr axis point"))
if n <=5:
    print("distance taken is one step")
elif(n%5==0):
    print("steps covered is",n/5)
else:
    print("steps covered is ",n//5+1)
    
