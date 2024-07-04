class linked3:
    def __init__(self,data):
        self.data=data
        self.next=None
def printl(head):
    if head == None:
        print("empty list")
        return
    cur=head.next
    print(head.data,end="-->")
    while cur != head:
        print(cur.data,end="-->")
        cur=cur.next
    print()
def insertingathead(head,val):
    newnode=linked3(val)
    if head==None:
        newnode.next=newnode
        return newnode
    newnode.next=head
    cur=head
    while cur.next!=head:
        cur=cur.next
    cur.next=newnode
    return newnode
def insertingattail(head,val):
    newnode=linked3(val)
    if head == None:
        newnode.next=newnode
        return newnode
    cur=head
    while cur.next != head:
        cur=cur.next
    cur.next=newnode
    newnode.next=head
    return head
def insertingatpos(head,pos,val):
    newnode=linked3(val)
    if head == None:
        print("list is empty cant insert ")
        return
    cur = head
    prev=None
    for i in range(pos):
        prev=cur
        cur = cur.next
    prev.next=newnode
    newnode.next=cur
    return head
def deleteathead(head):
    if head == None:
        print("cant delete empty list")
        return
    sec=head.next
    cur = head
    while cur.next != head:
        cur=cur.next
    cur.next=sec
    head.next=None
    return sec
def deletingattail(head):
    if head == None:
        print("cant delete empty list")
        return
    cur = head
    prev=None
    while cur.next !=head:
        prev=cur
        cur=cur.next
    prev.next=head
    cur.next=None
    return head
def deletingatpos(head,pos):
    if head ==  None:
        print("cant delete empty list")
        return
    cur=head
    prev=None
    for i in range(pos):
        prev=cur
        cur=cur.next
    prev.next=cur.next
    cur.next=None
    return head
head=None
l=[1,2,3,4,5,6]
print(l)
for i in l:
    head=insertingattail(head,i)
print("inserting at tail")
printl(head)
head1=None
for i in l:
    head1=insertingathead(head1,i)
print("inserting at head")
printl(head1)
print("inserting at particular pos")
head1=insertingatpos(head1,2,4000)
printl(head1)
print("deleting head node")
head1=deleteathead(head1)
printl(head1)
print("deleting at tail")
head1=deletingattail(head1)
print(head1)
print("deleting at particular pos")
head1=deletingatpos(head1,2)
printl(head1)



