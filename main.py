from random import randint
from game import Mob

name_list = ["Frank", "Mahmut", "Barış", "Umut", 
             "Yüksel", "Gülçin", "Alper", "Ece",
             "Ömer", "Sans", "Flowey", "Asgore",
             "Toriel", "Thanos", "Burak", "Eren",
             "Süleyman", "Ahmet", "Hasan"]



player_name = input("What's your name?")
monster = Mob(randint(8,17), randint(1,4), 1,  name_list[randint(0,19)], randint(1,4))
player = Mob(randint(8,17), randint(1,4), 1,  player_name, randint(1,4))
player.attack(monster)
