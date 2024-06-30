l=list(map(int,input().split()))
v=list()
print(l)
for i in l:
    r=0
    while(i>0):
        digit=i%10
        r=r+digit
        i=i//10
    v.append(r)
print(v)
