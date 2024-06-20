list5=list(map(int,input().split()))
ev=[]
od=[]
for i in range(len(list5)):
    if list5[i]%2==0:
        ev.append(list5[i])
    else:
        od.append(list5[i])
ev.sort()
ev.reverse()
od.sort()
e=ev+od
print(e)

               
               
