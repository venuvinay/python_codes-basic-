class link:
    def __init__(self,data):
        self.data=data
        self.next=None
def printlinked(head):
    if head == None:
        print("list is empty")
        return
    cur=head
    while cur !=None:
        print(cur.data,end="-->")
        cur=cur.next
    print()
def insertingpos(head,pos,val):
    if head == None:
        print("cant insert in empty list ")
        return
    newnode=link(val)
    prev=None
    cur=head
    for i in range(pos):
        prev=cur
        cur=cur.next
    prev.next=newnode
    newnode.next=cur
    return head
def insertingtail(head,val):
    newnode=link(val)
    if head == None:
        return newnode
    cur=head
    while cur.next != None:
        cur=cur.next
    cur.next=newnode
    return head
l=[10,20,30,40]
head=None
for i in l:
    head=insertingtail(head,i)
printlinked(head)
head=insertingpos(head,2,100)
printlinked(head)

