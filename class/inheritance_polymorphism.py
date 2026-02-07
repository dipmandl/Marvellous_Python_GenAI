class Parent:
    def __init__(self):
        print("Inside parent constructor.")


    def fun(self):
        print("Inside fun method of parent!!")


class Child(Parent):
    def __init__(self):
        print("Inside child constructor.")
        # super().__init__()



    def fun(self):
        super().fun(self)
        print("Inside fun method of child1.")

    def fun(self):
        print("Inside fun method of child2.")


obj1=Child()
obj1.fun()

