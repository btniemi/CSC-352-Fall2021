class Rocket():
    # rocket simulates a rocket ship for a game, or a physics simulation

    def __init__(self):
        # each rocket has an (x,y) position
        self.x = 0
        self.y = 0

    def move_up(self, num):
        # increment the y position of the rocket
        self.y += num


my_rocket = Rocket()
print(my_rocket)
print(my_rocket.__dict__)
print("Rocket altitude:", my_rocket.y)
my_rocket.move_up(1)
print("Rocket altitude:", my_rocket.y)
my_rocket.move_up(1)
print("Rocket altitude:", my_rocket.y)

my_rockets = [Rocket() for x in range(0, 5)]

for rocket in my_rockets:
    print(rocket)

my_rockets[0].move_up(1)
my_rockets[1].move_up(9)
my_rockets[2].move_up(6)
my_rockets[3].move_up(20)
my_rockets[4].move_up(2)

for rocket in my_rockets:
    print("Rocket altitude:", rocket.y)

# use this for assignment
