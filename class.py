class stud:
    def __init__(self,name,brand,Type,price,rating,delivery):
        self.name=name
        self.brand=brand
        self.Type=Type
        self.price=price
        self.rating=rating
        self.delivery=delivery
    def printde(self):
        print("name:",self.name)
        print("brand:",self.brand)
        print("Type:",self.Type)
        print("price:",self.price)
        print("rating:",self.rating)
        print("delivery with in:",self.delivery)
o=stud("smartwatch","apple","electronic",15000,4.5,"3 days")
o.printde()
o1=stud("mobile","apple","electronic",78000,4.2,"2 days")
o1.printde()
o2=stud("laptop","apple","electronic",100000,4.4,"1 days")
o2.printde()
