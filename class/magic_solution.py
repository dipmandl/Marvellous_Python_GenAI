#Dunder method/magic method/special method

class Demo:
    def __init__(self,a):
        self.no=a

    def __add__(self, other):
        print("Inside __add__")
        return self.no + other.no

    def __sub__(self, other):
        return self.no - other.no

    def __mul__(self, other):
        return self.no * other.no

    def __truediv__(self, other):
        return self.no / other.no


obj1=Demo(11)
obj2=Demo(21)
print(11+21) #32
print(obj1.no+obj2.no)    #this can be done using the dunder method using above __add__ method
print(obj1+obj2)    #__add__(obj1,obj2)
print(obj1-obj2)    #__sub__(obj1,obj2)
print(obj1*obj2)    #__mult__(obj1,obj2)
print(obj1/obj2)    #__div__(obj1,obj2)

