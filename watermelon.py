watermelon=int(input("enter wt of water melon"))
if watermelon%2!=0 or watermelon==2:
    print("odd no of weight")
else:
    x=watermelon/2
    if(x%2==0):
        print("yes wts are",x,x)
    else:
        print("yes wts are",x-1,x+1)
