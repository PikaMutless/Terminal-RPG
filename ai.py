from Mob import Mob
from random import randint
def enemy_turn(self, enemy, player):
    flee_chance = randint(1,51)
    flee_chance = 1
    if enemy.hit_point < enemy.max_hit_point / 2:
        enemy.heal()
    elif flee_chance == 1:
        print(enemy.name,"ran away")
        enemy =  self.create_enemy()
    else:
        enemy.attack(player)