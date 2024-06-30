class parent:
    def __init__(self,itemname,id):
        self.item=itemname
        self.id=id
    def parentname(self):
        print("parent class")
        print(self.item,self.id)
class child1(parent):
    def __init__(self,cost):
        self.cost=cost
        print("constructor of child1")
        parent.__init__(self,"phone",123)
    def printchild1(self):
        print(self.cost)
        print("child member")
class child2(parent):
    def __init__(self):
        print("final child")
        parent.__init__(self,"laptop",100)
obj=child2()
obj.parentname()
obj1=child1(200)
obj1.parentname()
obj1.printchild1()
