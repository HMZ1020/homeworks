

class Father: 
    def __init__(self, name, age, speed):

        self.name = name
        self.age = age 
        self.speed = speed

    def go_bathroom(self):
        print(f"he is going to the bathroom and his speed is {self.speed}")

    def eat(self, food):
        print(f"he is eating {food}")


class Son(Father):
    def __init__(self, name, age, speed):  
        super().__init__(name, age, speed)    

    def play(self, game):
        print(f"he is playing {game}")

    def go_school(self):
        print(f"he is going to school")    

father = Father(name = "hamza", age = 23, speed = 100)
ahmed = Son(name = "ahmed", age = 4, speed = 10)        

ahmed.play(game = "call of duty ")
father.go_bathroom()