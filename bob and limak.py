b1=int(input("enter wt of brother 1"))
b2=int(input("enter wt of second bro"))
year=0
while(b1<b2):
    b1*=3
    b2*=2
    year+=1
print("no years taken to gain wt is ",year,"wts are",b1,b2)
