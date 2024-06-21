li=[1,2,3,(1,2,3)]
count=0
for i in li:
    if type(i)==tuple:
        break
    count+=1
print(count)
