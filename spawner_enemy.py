import classe as classe
import os
import fight_animation as fight



def spawn_ennemy():
    enemy = None

    
    enemy_presence = int.from_bytes(os.urandom(1), "big") % 10 + 1

    if enemy_presence <= 2 :

        random_enemy = int.from_bytes(os.urandom(1), "big") % 10 + 1

        if random_enemy < 5 : 

            random_lvl = int.from_bytes(os.urandom(1), "big") % 10 + 1

            enemy = classe.monster("Orc", random_lvl)

            fight.print_fight()


        elif random_enemy >= 5 and random_enemy < 7 : 

            random_lvl = int.from_bytes(os.urandom(1), "big") % 10 + 1

            enemy = classe.monster("Orc", random_lvl)

            fight.print_fight()


        elif random_enemy >= 7 : 

            random_lvl = int.from_bytes(os.urandom(1), "big") % 10 + 1

            enemy = classe.monster("Orc", random_lvl)

            fight.print_fight()


        return enemy
