class linkedlist:
    def __init__(self,data):
        self.data=data
        self.next=None
def printlinked(head):
    if head == None:
        print("no linked list to print")
    cur=head
    while cur!=None:
        print(cur.data,end="-->")
        cur=cur.next
    print()
def insertingathead(head,val):
    newnode=linkedlist(val)
    if head == None:
        return newnode
    newnode.next=head
    return newnode
def insertingattail(head,val):
    newnode=linkedlist(val)
    if head == None:
        return newnode
    tail=head
    while tail.next!=None:
        tail=tail.next
    tail.next=newnode
    return head
def deletenodeattail(head):
    if head == None:
        print("cant delete empty list")
        return None
    prev=None
    cur=head
    while cur.next !=None:
        prev=cur
        cur=cur.next
    prev.next=None
    return head
def deleteathead(head):
    if head == None:
        print("cant delete empty list")
        return None
    sec=head.next
    head.next=None
    return sec
head=None
l=list(map(int,input("enter list of elements").split()))
print(l)
for i in l:
    head=insertingattail(head,i)
printlinked(head)
head = deletenodeattail(head)
printlinked(head)
head = deleteathead(head)
printlinked(head)
l1=list(map(int,input("enter list of elements").split()))
print(l1)
for i in l1:
    head=insertingathead(head,i)
printlinked(head)
head = deletenodeattail(head)
printlinked(head)
head = deleteathead(head)
printlinked(head)

    
    
