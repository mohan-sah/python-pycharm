class Animal:
    def __init__(self):
        self.num_eyes = 2


    def breathe(self):
        print("inhale exhale")



class Fish(Animal):

    def __init__(self):
        super().__init__()

    def breathe(self):
        super().breathe()
        print("doing this under water0")


    def swim(self):
        print("moving in wather")


nemo = Fish()
nemo.swim()
nemo.breathe()
print(nemo.num_eyes)