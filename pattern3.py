n=3
for i in  range(n+1):
    for j in range(i+1):
        if i%2!=0:
            print("#",end="")
        else:
            print("*",end="")
    print()
    
