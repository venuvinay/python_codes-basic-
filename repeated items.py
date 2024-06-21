t=tuple(map(int,input().split()))
a=0
for i in t:
    d=t.count(i)
    if d>1:
        a=d
print(a)
        
        
