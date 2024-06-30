class linkedlist:
    def __init__(self,data):
        self.data=data
        self.next=None
def printlinkedlist(head):
    cur=head
    while cur.next!=None:
        print(cur.data,end="-->")
        cur=cur.next                    
o1=linkedlist(100)
o2=linkedlist(200)
o3=linkedlist(300)
o4=linkedlist(400)
o5=linkedlist(500)
o1.next=o2
o2.next=o3
o3.next=o4
o4.next=o5
printlinkedlist(o1)
