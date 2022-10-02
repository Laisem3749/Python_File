class Hourse():
    def __init__(self, breed, wm, owner):
        self.breed = breed
        self.wm = wm
        self.owner = owner

class Human():
    def __init__(self, name):
        self.name = name

p = Human('Vovan')
h = Hourse('white', 'wooman', p)
print(h.owner.name)

