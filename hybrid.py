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
class derived2(derived):
    def __init__(self):
        print("multi-level inheritance")
        derived.__init__(self)
class derived3(base):
    def __init__(self):
        print("hybrid in heritance")        
obj1=derived3()
obj1.memberbase()
obj2=derived2()
obj2.printbase()
obj2.memberbase()
obj=derived()
obj.memberbase()
obj.printbase()
