n=int(input())
v=n
rev=0
#print("digit=",v%10)
while v>0:
    digit=v%10
    rev=rev+(digit*digit*digit)
    v=v//10
print(rev)
if n==rev:
    print("num is armstrong")
else:
    print("not a armstrong")
