# Polymorphism:
#               Polymorphism in programming gives a program the ability to redefine methods for derived classes

class Eagle:
    def fly(self):
        print("Eagle Can Fly")

    def swim(self):
        print("Eagle Cannot Swim")


class Penguin:
    def fly(self):
        print("Penguin Cannot Fly")

    def swim(self):
        print("Penguin Can Swim")


def flying_test(bird):
    bird.fly()


e1 = Eagle()
p1 = Penguin()

# polymorphism principle
flying_test(e1)
flying_test(p1)