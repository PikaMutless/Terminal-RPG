from random import randint, choice
from Mob import Mob

name_list = ["Frank", "Mahmut", "Barış", "Umut",
             "Yüksel", "Gülçin", "Alper", "Ece",
             "Ömer", "Sans", "Flowey", "Asgore",
             "Toriel", "Thanos", "Burak", "Eren",
             "Süleyman", "Ahmet", "Hasan", "Papyrus",
             "Ecrin", "Güneş", "Elif", "Zekai Kral"]

class Game:
    def __init__(self) -> None:
        player_name = input("What is your name? \n=>")
        self.player =  Mob(randint(8,13), randint(1,4), 1,  "", randint(1,4))
        self.player.name = player_name
        self.enemy = self.create_enemy()

    def loop(self) -> None:
        while self.player.level < 10:
            print("\033[92m#"*20,"\n")
            print("\033[91m",self.enemy.name, ":", self.enemy.hit_point, "HP")
            print("\033[97m You :", self.player.hit_point, "HP")
            players_choise = int(input(f" Attack(1) | Heal(2) | Flee (3) | Check(4)\n=>"))
            if players_choise == 1:
                self.player.attack(self.enemy)
            elif players_choise == 2:
                self.player.heal()
            elif players_choise == 3:
                print("You ran away!")
                self.enemy =  self.create_enemy()
            elif players_choise == 4:
                check_character = int(input("You(1) | Enemy(2)\n=>"))
                if check_character == 1:
                    print("Name :", self.player.name, "\nLevel :", self.player.level, "\nHit Point :", self.player.hit_point ,"/",self.player.max_hit_point, "\nStrength :", self.player.strength, "\nAgility :",self.player.agility)
                elif check_character == 2:
                    print("Name :",self.enemy.name, "\nLevel :", self.enemy.level, "\nHit Point :", self.enemy.hit_point ,"/",self.enemy.max_hit_point, "\nStrength :", self.enemy.strength, "\nAgility :",self.enemy.agility)
            if self.enemy.hit_point <= 0:
                self.enemy = self.create_enemy()
        print("You did it. You finally got to the lvl 10. Now you can get back to the normal world!")
                
    def create_enemy(self):
        player_lvl = self.player.level   
        enemy = Mob(randint(player_lvl*8, player_lvl*13), randint(player_lvl*1, player_lvl*4), player_lvl,  choice(name_list), randint(player_lvl*1, player_lvl*4))

        return enemy
    
if __name__ == "__main__":
    game = Game()
    game.loop()

