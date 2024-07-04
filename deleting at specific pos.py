class dlink:
    def __init__(self,data):
        self.data=data
        self.next=None
def insertingattail(head,val):
    newnode=dlink(val)
    if head == None:
        return newnode
    tail=head
    while tail.next!=None:
        tail=tail.next
    tail.next=newnode
    return head
def printlinked(head):
    if head == None:
        print("no list to print")
        return
    cur=head
    while cur !=None:
        print(cur.data,end="-->")
        cur = cur.next
    print()
def deletepos(head,pos):
    prev=None
    cur=head
    for i in range(pos):
        prev=cur
        cur=cur.next
    prev.next=cur.next
    return head
l=[23,56,12,23,4,5]
head=None
for i in l:
    head=insertingattail(head,i)
printlinked(head)
deletepos(head,2)
printlinked(head)
