from random import randint
from Mob import Mob

# Display health of player and enemy in each loop

name_list = ["Frank", "Mahmut", "Barış", "Umut",
             "Yüksel", "Gülçin", "Alper", "Ece",
             "Ömer", "Sans", "Flowey", "Asgore",
             "Toriel", "Thanos", "Burak", "Eren",
             "Süleyman", "Ahmet", "Hasan", "Papyrus",
             "Ecrin", "Güneş", "Elif", "Zekai Kral"]

class Game:
    def __init__(self) -> None:
        self.player_name = input("What is your name? \n=>")
        Mobs.player.name = self.player_name

    def loop(self) -> None:
        while Mobs.player.level < 10:
            print(Mobs.monster.name, ":", Mobs.monster.hit_point, "HP")
            print("You :", Mobs.player.hit_point, "HP")
            players_choise = int(input(f"Attack(1) | Heal(2) | Flee (3)"))
            if players_choise == 1:
                Mobs.player.attack(Mobs.monster)
            elif players_choise == 2:
                Mobs.player.heal()
            elif players_choise == 3:
                pass#BAK BURAYA UNUTMA!!!
                
        
class Mobs:
    player = Mob(randint(8,17), randint(1,4), 1,  "init player", randint(1,4))
    monster = Mob(randint(8,17), randint(1,4), 1,  name_list[randint(0,25)], randint(1,4))

if __name__ == "__main__":
    game = Game()
    game.loop()