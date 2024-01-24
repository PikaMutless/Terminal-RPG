from random import randint
class Mob:
    def __init__(self, hit_point, strength, level, name, agility) -> None:
        self.hit_point = hit_point
        self.max_hit_point = hit_point
        self.strength = strength
        self.level = level
        self.name = name
        self.agility = agility
        self.is_lvl_up = False
        self.heal_potion_amount = 3
        print("A new mob created")

    
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
                
                self.is_lvl_up = True
                print(f"{self.name} killed {target.name}!")
            else:
                print(f"{self.name} dealt {damage_power} damage to {target.name}!")
                
        else:
            print(f"{self.name} missed!")

    def lvl_up_controller(self):
        if self.is_lvl_up == True:
            self.level += 1
            self.is_lvl_up = False

    def heal(self):
        if self.heal_potion_amount > 0:
            heal_amount = self.max_hit_point / 5 
            self.hit_point += heal_amount
            if self.hit_point > self.max_hit_point:
                self.hit_point = self.max_hit_point
        self.heal_potion_amount -= 1
        print(f"{self.name} healed {heal_amount} hit points")



