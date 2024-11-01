import classe as classe
import os
import arbre as arbre
import time
import fight as fight
import fight_animation as anime
import draw_hp as hp



def spawn_ennemy():
    enemy = None

    
    enemy_presence = int.from_bytes(os.urandom(1), "big") % 10 + 1

    if enemy_presence <= 2 :

        random_enemy = int.from_bytes(os.urandom(1), "big") % 10 + 1

        if random_enemy < 5 : 

            random_lvl = int.from_bytes(os.urandom(1), "big") % 10 + 1

            enemy = classe.monster("Orc", random_lvl)

            found_enemy()

            anime.print_fight()

            hp.draw_hp_ennemy(enemy)
            hp.draw_hp_player(classe.player)

            fight.fight(enemy, classe.player)


        elif random_enemy >= 5 and random_enemy < 7 : 

            random_lvl = int.from_bytes(os.urandom(1), "big") % 10 + 1

            enemy = classe.monster("Orc", random_lvl)

            found_enemy()

            anime.print_fight()

            hp.draw_hp_ennemy(enemy)
            hp.draw_hp_player(classe.player)

            fight.fight(enemy, classe.player)


        elif random_enemy >= 7 : 

            random_lvl = int.from_bytes(os.urandom(1), "big") % 10 + 1

            enemy = classe.monster("Orc", random_lvl)

            found_enemy()

            anime.print_fight()

            hp.draw_hp_ennemy(enemy)
            hp.draw_hp_player(classe.player)

            fight.fight(enemy, classe.player)


        return enemy

def found_enemy():
    for i in range(4):
        arbre.drawMap("z")
        time.sleep(0.2)
        clear_console()
        time.sleep(0.2)

def clear_console():
    # Pour Windows
    if os.name == 'nt':
        os.system('cls')
    # Pour Mac et Linux (os.name est 'posix')
    else:
        os.system('clear')
