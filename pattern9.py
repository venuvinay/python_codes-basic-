n=int(input())
r=0
sp=n
for i in range(n):
    for k in range(r):
        print(" ",end="")
    for j in range(sp):
        print(chr(j+65),end="")
    print()
    r+=1
    sp-=1
