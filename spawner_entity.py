import classe as classe
import os
import arbre as arbre
import time
import fight as fight
import fight_animation as anime
import draw_hp as hp
import clear as clear
import find_potion as find_potion


def spawn_entity(player):
    enemy = None

    
    entity_presence = int.from_bytes(os.urandom(1), "big") % 10 + 1

    if entity_presence <= 2 :

        random_enemy = int.from_bytes(os.urandom(1), "big") % 10 + 1

        if random_enemy < 2 :

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

    elif entity_presence == 3 :

        effect = ""

        random_lvl = int.from_bytes(os.urandom(1), "big") % 10 + 1
        random_effect = int.from_bytes(os.urandom(1), "big") % 4 + 1
       
        if random_lvl <= 4 :
            random_lvl = 1
        
        elif random_lvl > 4 and random_lvl <= 7:
            random_lvl = 2
        
        elif random_lvl > 7 and random_lvl <= 9 :
            random_lvl = 3
        
        elif random_lvl == 10 :
            random_lvl = 4
        

        if random_effect == 1 :
            effect = "Heal Potion"

        elif random_effect == 2 :
            effect = "Speed Potion"

        elif random_effect == 3 :
            effect = "Strenght Potion"

        elif random_effect == 4 :
            effect = "Defence Potion"

        potion = classe.Potion(effect, random_lvl)
        player.add_object(potion)
        print(potion)
        find_potion.find_potion_message()




def found_enemy():
    for i in range(4):
        arbre.drawMap("z")
        time.sleep(0.2)
        clear.clear()
        time.sleep(0.2)

