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
            players_choise = int(input(f"If you want to attack {Mobs.monster.name}, press '1', if you want to use healing potion, press '2'."))
            if players_choise == 1:
                Mobs.player.attack(Mobs.monster)
            elif players_choise == 2:
                Mobs.player.heal()
                
        
class Mobs:
    player = Mob(randint(8,17), randint(1,4), 1,  "init player", randint(1,4))
    monster = Mob(randint(8,17), randint(1,4), 1,  name_list[randint(0,19)], randint(1,4))

if __name__ == "__main__":
    game = Game()
    game.loop()