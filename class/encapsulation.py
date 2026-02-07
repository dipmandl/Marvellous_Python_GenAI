class Arithmetic:
    def __init__(self,a,b):
        self.no1=a
        self.no2=b
        print("Objects get created succesfully.")

    def addition(self):
        ans=0
        ans= self.no1+self.no2
        return ans

    def subtraction(self):
        ans=0
        ans=self.no1-self.no2
        return ans

obj1=Arithmetic(11,10)   #Arithmatic(id(obj1),11,10)-->__init(id(obj1),11,10)
obj2=Arithmetic(21,12)   ##Arithmatic(id(obj2),21,20)-->__init(id(obj1),21,20)

ret=obj1.addition()
print("Addition is for obj1 : ",ret)  #21

ret=obj2.subtraction()
print("Subtraction is for obj2: ",ret)   #9
