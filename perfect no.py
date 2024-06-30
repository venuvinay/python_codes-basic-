n=int(input())
l=0
for i in range(1,n):
    if n%i==0:
        l+=i
if l==n:
    print("perfect no ")
else:
    print("not a perfect no")
