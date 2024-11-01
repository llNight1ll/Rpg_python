import classe as classe
import orc as anime
import draw_hp as hp
import time
import game_over as end
import fight_option as fight_option
import run as run



def fight(enemy, player):
    time.sleep(5)

    while enemy.health > 0 and player.health > 0:
        accept = False
        while accept == False:
            try:
                valeur = None

                fight_option.print_option()
                
                valeur = str(input("Enter your choice: "))

                if valeur == "1":
                    accept = True
                    enemy.loose_hp(10)
                    anime.player_attack_animation()
                    hp.draw_hp_ennemy(enemy)
                    hp.draw_hp_player(player)
                    time.sleep(1)


                    if enemy.health > 0:

                        enemy_attack(enemy, player)
                    else:
                        return
                if valeur == "4":
                    escape = run.run(enemy,player)
                    if escape == True :
                        return



            except ValueError :
                print("Invalid choice. Please try again.")


def enemy_attack(enemy, player):
    anime.ennemy_attack_animation()
    player.loose_hp(enemy.strenght)
    hp.draw_hp_ennemy(enemy)
    hp.draw_hp_player(player)
    time.sleep(1)
    if player.health <= 0 :
        end.game_over()
        
