import cmath as m
a=int(input())
b=int(input())
c=int(input())
d=b*b-(4*a*c)
root1=(-b+m.sqrt(d))/2*a
root2=(-b-m.sqrt(d))/2*a
print(root1,root2)
