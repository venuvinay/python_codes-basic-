class stud:
    def __init__(self,name,roll,cmarks,javamarks,pythonmarks):
        self.name=name
        self.roll=roll
        self.cmarks=cmarks
        self.javamarks=javamarks
        self.pythonmarks=pythonmarks
    def printde(self):
        print("name:",self.name)
        print("roll:",self.roll)
        print("cmarks:",self.cmarks)
        print("javamarks:",self.javamarks)
        print("pythonmarks:",self.pythonmarks)
o=stud("vinay","21HQ1A0517",99,99,99)
o.printde()
o1=stud("mark","21HQ1A05100",98,98,98)
o1.printde()

