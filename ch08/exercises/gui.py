class Mario:
    def __init__(self, name, lives, score):
        self.name = name
        self.lives = lives
        self.score = score

    def jump(self):
        print(f"{self.name} jumps high into the air!")

    def power_up(self):
        self.score += 1000
        print(f"{self.name} has powered up! Score: {self.score}")


class Goomba:
    def __init__(self, color, size, speed):
        self.color = color
        self.size = size
        self.speed = speed

    def stomp(self):
        print(f"You've defeated the {self.color} Goomba!")

    def attack(self):
        print(f"The {self.color} Goomba charges at you!")


class Bowser:
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power

    def roar(self):
        print(f"{self.name} lets out a deafening roar!")

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            print(f"{self.name} has been defeated!")
        else:
            print(f"{self.name} takes {damage} damage. Health: {self.health}")
