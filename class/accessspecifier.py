class Demo:
    def __init__(self):
        self.no1=10         #treated as public
        self._no2=20        #treated as protected
        self.__no3=30       #treated as private

obj=Demo()

