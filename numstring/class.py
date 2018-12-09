import random


class Theif():
    sneaky = "sathish"


    def hell(self):
        return bool(random.randint(0,1))


apple = Theif()
print (apple.hell())
print (apple.sneaky)
apple.sneaky = "talluri"
print (apple.sneaky)