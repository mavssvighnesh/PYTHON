class dog:
    def __init__(self,name,age):
         self.name=name
         self.age=age
    def bark(self):
        print(self.name+"barks")
    def get_age(self):
         print(f"dog name:{self.name} age:{self.age}")
    def get_name(self):
         print(f"dog name:{self.name}")

d=dog("tim",4)
d2=dog("cook",6)

d.get_name()
d.get_age()

d2.bark()
