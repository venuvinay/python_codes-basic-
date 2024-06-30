class link:
    def __init__(self,data):
        self.data=data
        self.next=None
def printlinked(head):
    cur=head
    while cur != None:
        print(cur.data,end="-->")
        cur=cur.next
    print()
def insertinglinkedhead(head,val):
    newnode=link(val)
    if head == None:
        return newnode
    newnode.next=head
    return newnode
def insertinglinkedtail(head,val):
    newnode1=link(val)
    if head == None:
        return newnode
    tail=head
    while tail.next!=None:
        tail=tail.next
    tail.next=newnode1
    return head
head=None
l=[10,20,30,40]
for i in l:
    head=insertinglinkedhead(head,i)
    #tail=insertinglinkedtail(head,i)
printlinked(head)
print()
#printlinked(tail)
    



        
