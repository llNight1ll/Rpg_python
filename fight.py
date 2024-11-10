import classe as classe
import orc as anime
import draw_hp as hp
import time
import game_over as end
import fight_option as fight_option
import run as run
import inventory_panel as inv_panel
import print_inventory as inventory
import sentence as sentence
import clear as clear



def fight(enemy, player):
    time.sleep(1)

    while enemy.health > 0 and player.health > 0:
        accept = False
        while accept == False:
            try:
                valeur = None

                fight_option.print_option()

                valeur = str(input(sentence.enter_your_choice))
                print(enemy.speed)


                if valeur == "1":
                    accept = True
                    if player.speed >= enemy.speed:
                            
                        for id, object in player.armory.items():
                            if object == player.equiped_weapon:
                                object.health -=1
                                if  object.health == 0 :
                                    player.equiped_weapon = player.armory[1]
                                    del player.armory[id]
                                    break

                        enemy.loose_hp(round(player.strenght + player.equiped_weapon.damage / (enemy.defence / 2)))
                        anime.player_attack_animation(enemy)
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

                    
                            for id, object in player.armory.items():
                                if object == player.equiped_weapon:
                                    object.health -=1
                                    if  object.health == 0 :
                                        player.equiped_weapon = player.armory[1]
                                        del player.armory[id]
                                        break

                            enemy.loose_hp(round(player.strenght + player.equiped_weapon.damage / (enemy.defence / 2)))
                            anime.player_attack_animation(enemy)
                            hp.draw_hp_ennemy(enemy)
                            hp.draw_hp_player(player)
                            time.sleep(1)

                        else:
                            player.gain_xp(enemy.xp)
                            return
                if valeur =="2" :
                    inventory.print_armory()
                    print(sentence.exit_armory)  
                    classe.player.show_inventory("weapon")
                    has_used = inv_panel.inventory(classe.player,"weapon")
                    clear.clear()
                    if has_used == True:
                        enemy_attack(enemy, player)

                if valeur ==  "3":
                    inventory.print_inventory()
                    print()  
                    classe.player.show_inventory("")     
                    has_used = inv_panel.inventory(classe.player)
                    clear.clear()
                    anime.neutre(enemy)
                    hp.draw_hp_ennemy(enemy)
                    hp.draw_hp_player(player)
                    
                    if has_used == True:
                        enemy_attack(enemy, player)

                if valeur == "4":
                    escape = run.run(enemy,player)
                    if escape == True :
                        return
                    else :
                        enemy_attack(enemy, player)



            except ValueError :
                print(sentence.invalid_choice)


def enemy_attack(enemy, player):
    anime.enemy_attack_animation(enemy)
    player.loose_hp(round(enemy.strenght / (player.defence)))
    hp.draw_hp_ennemy(enemy)
    hp.draw_hp_player(player)
    time.sleep(1)
    if player.health <= 0 :
        end.game_over()
        
