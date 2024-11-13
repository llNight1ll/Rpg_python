import classe
import os
import arbre
import time
import fight
import fight_animation as anime
import draw_hp as hp
import find_potion
import print_hp_ascii as ascii
import sys
import clear

def spawn_entity(player, is_boss = False):
    #Exception for boss fight
    enemy = None
    if is_boss == True :
        enemy = classe.boss
        found_enemy()

        anime.print_fight(enemy)

        hp.draw_hp_ennemy(enemy)
        hp.draw_hp_player(classe.player)

        has_win = fight.fight(enemy, classe.player)

        if has_win == True :
            clear.clear()
            ascii.print_ascii_text("Congrats, You escaped the forest", "other")
            sys.exit(1)
            
        
        return enemy
    
   #Decide if a monster is present 
    entity_presence = int.from_bytes(os.urandom(1), "big") % 10 + 1

    #If a monster is present :
    if entity_presence <= 2 :

        random_enemy = int.from_bytes(os.urandom(1), "big") % 10 + 1

        #If the monster is an orc :
        if random_enemy <= 5 : 

            random_lvl = int.from_bytes(os.urandom(1), "big") % (player.position_y + 3) + 1

            enemy = classe.monster("Orc", random_lvl)



        #If the monster is an Gobelin :
        elif random_enemy > 5 : 

            random_lvl = int.from_bytes(os.urandom(1), "big") % ( player.position_y + 3) + 1

            enemy = classe.monster("Gobelin", random_lvl)


      
        found_enemy()

        anime.print_fight(enemy)

        hp.draw_hp_ennemy(enemy)
        hp.draw_hp_player(classe.player)

        fight.fight(enemy, classe.player)
        
        return enemy

    #If a potion is found :
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

        potion = classe.potion(effect, random_lvl)
        player.add_object(potion,"")
        print(potion)
        find_potion.find_potion_message()




def found_enemy():
    for i in range(4):
        arbre.drawMap("z")
        time.sleep(0.2)
        clear.clear()
        time.sleep(0.2)

