n=int(input())
sp=n
for i in range(n):
    for l in range(i):
        print(" ",end=" ")
    for j in range(sp):
        print(chr(j+65),end=" ")
    print()
    sp-=1
