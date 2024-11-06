import classe as classe
import orc as anime
import draw_hp as hp
import time
import game_over as end
import fight_option as fight_option
import run as run
import inventory_panel as inv_panel
import print_inventory as inventory




def fight(enemy, player):
    time.sleep(1)

    while enemy.health > 0 and player.health > 0:
        accept = False
        while accept == False:
            try:
                valeur = None

                fight_option.print_option()

                
                valeur = str(input("Enter your choice: "))
                print(enemy.speed)


                if valeur == "1":
                    accept = True
                    if player.speed >= enemy.speed:

                        enemy.loose_hp(round(player.strenght * player.equiped_weapon.damage / (enemy.defence / 2)))
                        anime.player_attack_animation()
                        hp.draw_hp_ennemy(enemy)
                        hp.draw_hp_player(player)
                        time.sleep(1)


                        if enemy.health > 0:

                            enemy_attack(enemy, player)
                        else:
                            player.gain_xp(enemy.xp)
                            return
                    else :
                        if enemy.health > 0:

                            enemy_attack(enemy, player)

                    
                            enemy.loose_hp(round(player.strenght * player.equiped_weapon.damage / (enemy.defence / 2)))
                            anime.player_attack_animation()
                            hp.draw_hp_ennemy(enemy)
                            hp.draw_hp_player(player)
                            time.sleep(1)

                        else:
                            player.gain_xp(enemy.xp)
                            return
                if valeur =="2" :
                    inventory.print_armory()
                    print("To exit the armory enter 0")  
                    classe.player.show_inventory("weapon")
                    inv_panel.inventory(classe.player,"weapon")

                if valeur ==  "3":
                    inventory.print_inventory()
                    print("To exit the inventory enter 0")  
                    classe.player.show_inventory("")
                    inv_panel.inventory(classe.player)
                    anime.neutre()
                    hp.draw_hp_ennemy(enemy)
                    hp.draw_hp_player(player)

                if valeur == "4":
                    escape = run.run(enemy,player)
                    if escape == True :
                        return



            except ValueError :
                print("Invalid choice. Please try again.")


def enemy_attack(enemy, player):
    anime.ennemy_attack_animation()
    player.loose_hp(round(enemy.strenght / (player.defence /2)))
    hp.draw_hp_ennemy(enemy)
    hp.draw_hp_player(player)
    time.sleep(1)
    if player.health <= 0 :
        end.game_over()
        
