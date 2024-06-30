class base:
    def __init__(self,name='vinay',rollNo='21HQ1A0517'):
        self.name=name
        self.rollno=rollNo
        print("base class")
    def memberbase(self):
        print("member of base ")
class derived(base):
    def __init__(self,marks1=10,marks2=28):
        self.marks=marks1
        self.marks1=marks2
        print("derived class ")
        base.__init__(self)
    def printbase(self):
        print(self.name,self.rollno)
obj=derived()
obj.memberbase()
obj.printbase()
