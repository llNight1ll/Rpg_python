import classe as classe
import orc as anime
import draw_hp as hp


def fight(enemy, player):

    while enemy.health > 0:
        accept = False
        while accept == False:
            try:
                valeur = None
                valeur = str(input("Enter your choice: "))

                if valeur == "1":
                    accept = True
                    enemy.loose_hp(10)
                    anime.player_attack_animation()
                    hp.draw_hp_ennemy(enemy)
                    hp.draw_hp_player(player)

                    if enemy.health > 0:

                        enemy_attack(enemy, player)
                    else:
                        break


            except ValueError :
                print("Invalid choice. Please try again.")


def enemy_attack(enemy, player):
    anime.ennemy_attack_animation()
    player.loose_hp(enemy.strenght)
    hp.draw_hp_ennemy(enemy)
    hp.draw_hp_player(player)
