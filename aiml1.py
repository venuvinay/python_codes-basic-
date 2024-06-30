n=int(input())
l=[]
n1=[]
for i in range(1,n+1):
    l.append(i)
print(l)
for i in l:
    if i/1==1:
        n1.append(1)
    elif i%2==0:
        n1.append(2)
    elif i%3==0:
        n1.append(3)
    else:
        n1.append(5)
print(n1)
