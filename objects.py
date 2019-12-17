class Car():
    def __init__(self,name):
        self.name = name

    def honk(self):
        print('i am a car')

class Tata(Car):
    def __init__(self,name):
        self.name = name

    # def honk(self):
    #     print('i am tata',self.name)

t=Tata('swift')
c=Car('swift')

t.honk()
c.honk()


