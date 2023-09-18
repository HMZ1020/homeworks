print("--------------------------")


class humen:
    def __init__(self,name,health,speed):
        self.name = name
        self.health = health
        self.speed = speed
    def kf(self):
        print(self.name , self.health, self.speed )


humen1 = humen(name = "ali" , health =  2 , speed =  1)

humen1.kf()


print("--------------------------")


