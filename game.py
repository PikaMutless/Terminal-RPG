from random import randint

class Mob:
    def __init__(self, hit_point, strength, level, name, agility) -> None:
        self.hit_point = hit_point
        self.strength = strength
        self.level = level
        self.name = name
        self.agility = agility
    
    def is_hit(self):
        if self.target.agility == self.agility and randint(1,6) == 1:
            return False
        elif self.target.agility > self.agility and randint(1,4) == 1:
            return False
        elif self.target.agility < self.agility and randint(1,11) == 1:
            return False
        else:
            return True
        
    def attack(self, target:"Mob"):
        self.target = target
        damage_power = self.strength
        if self.is_hit(): 
            target.hit_point -= damage_power
            if target.hit_point <= 0:
                
            else:
                print(f"{self.name} dealt {damage_power} damage!")
        else:
            print(f"{self.name} missed!")

            
monster = Mob(55, 6, 5, "Frank", 6)
player = Mob(65, 5, 5, "Umut", 6)
player.attack(monster)
print(monster.hit_point)

class Bow:
    pass
class Sword:
    pass