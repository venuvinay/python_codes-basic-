n=int(input())
sp=n-1
for i in range(n):
    for k in range(sp):
        print(" ",end="")
    i3=i
    for j in range(1,i+2):
        if i%2==0:
            print(j,end="")
        else:
            print(i3+1,end="")
            i3-=1
    print()
    sp-=1




