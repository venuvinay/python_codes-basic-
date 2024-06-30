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
class child2(child1):
    def __init__(self):
        print("final child")
        child1.__init__(self,100)
obj=child2()
obj.printchild1()
obj.parentname()
