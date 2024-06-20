list1=list(map(int,input().split()))
l=len(list1)
temp=list1[0]
list1[0]=list1[l-1]
list1[l-1]=temp
print(list1)
