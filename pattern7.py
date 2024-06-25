n=int(input())
for i in range(n):
    for j in range(1,i+2):
        if i%2!=0:
            print("@",end="")
        else:
            print(i+1,end="")
    print()
