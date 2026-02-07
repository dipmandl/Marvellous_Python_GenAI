class Parent:
    def __init__(self,a,b):
        print("Inside parent constructor.")
        self.no1=a
        self.no2=b

    def fun(self):
        print("Inside fun method of parent!!",self.no1,self.no2)


class Child(Parent):
    def __init__(self,a,b):
        print("Inside child constructor.")
        self.a=11
        self.b=25
        # print(self.no1)   if we are using before calling the super it will thrown error.
        super().__init__(a, b)
        # print(self.no1)    it will not thrown any error.


    def son(self):
        print("Inside son method of child.",self.a,self.b,self.no1,self.no2)


obj1=Child(21,10)
print("variables comes from parent")
print(obj1.no1)     #21
print(obj1.no2)     #10
print("variables comes from child")
print(obj1.a)       #11
print(obj1.b)       #25

#Calling methods
obj1.fun()

obj1.son()


