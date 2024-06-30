st1=input()
st2=input()
if len(st1) != len(st2):
    print("Not a anagrams")
    exit(0)
store1 = dict()
store2 = dict()

for ch in st1:
    if ch in store1:
        store1[ch] += 1
    else:
        store1[ch] = 1

for ch in st2:
    if ch in store2:
        store2[ch] += 1
    else:
        store2[ch] = 1
        
val = True
for key in store1.keys():
    if key not in store2.keys() or store2[key] != store1[key]:
        val = False
        break
if val:
    print("Anagrams")
else:
    print("Not an Anagrams")
