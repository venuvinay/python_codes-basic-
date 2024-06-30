class linkedlist:
    def __init__(self,data):
        self.data=data
        self.next=None
def printlinked(head):
    cur=head
    while cur !=None:
        print(cur.data,end="-->")
        cur=cur.next
    print()
def insertingattail(head,val):
    newnode=linkedlist(val)
    if head==None:
        return newnode
    tail=head
    while tail.next!=None:
        tail=tail.next
    tail.next=newnode
    return head
def insertathead(head,val):
    newnode=linkedlist(val)
    if head==None:
        return newnode
    newnode.next=head
    return newnode
o=linkedlist(100)
o1=linkedlist(400)
o2=linkedlist(500)
o3=linkedlist(600)
o4=linkedlist(1600)
o.next=o1
o1.next=o2
o2.next=o3
o3.next=o4
printlinked(o)
head=insertingattail(o,200)
printlinked(head)
head1=insertathead(head,5000)
printlinked(head1)






    
