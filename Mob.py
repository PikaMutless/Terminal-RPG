from random import randint
class Mob:
    def __init__(self, max_hit_point, strength, level, name, agility) -> None:
        self.max_hit_point = max_hit_point
        self.hit_point = max_hit_point
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
                self.lvl_up_controller()


            else:
                print(f"{self.name} dealt {damage_power} damage to {target.name}!\n")
                
        else:
            print(f"{self.name} missed!\n")

    def lvl_up_controller(self):
        if self.is_lvl_up == True:
            self.level += 1
            self.is_lvl_up = False
            self.max_hit_point += randint(8,13) 
            self.hit_point = self.max_hit_point
            self.strength += randint(1,4)
            self.agility += randint(1,3)

    def heal(self):
        if self.heal_potion_amount > 0:
            heal_amount = round(self.max_hit_point / 2) 
            if self.hit_point + heal_amount > self.max_hit_point:
                heal_amount = self.max_hit_point - self.hit_point
            self.hit_point += heal_amount

            print(f"{self.name} healed {heal_amount} hit points")    
            self.heal_potion_amount -= 1
        else:
            print(f"{self.name} don't have heal potion!")  
        
#Add races that are getting some stats more and getting some stats less. 


