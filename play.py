import classe
import spawner_entity as spawner
import arbre as arbre
import print_inventory as inventory
import inventory_panel as inv_panel
import save
import sentence
import clear
import print_hp_ascii as ascii
import keyboard
side = "s"


def game():
    accept = False
     #Gameloop
    while accept == False:
        try:
            valeur = None
            valeur = str(input(sentence.enter_your_choice))

            
            if valeur == "z":
                accept = True
                if (classe.player.position_y  > 0) :
                    classe.player.position_y -= 1
                    print(valeur)
                    spawner.spawn_entity(classe.player)
                    return valeur

                
            elif valeur == "s":
                accept = True
                if (classe.player.position_y < 8) :
                    classe.player.position_y += 1
                    print(valeur)
                    spawner.spawn_entity(classe.player)
                    return valeur


            elif valeur == "q":
                accept = True
                if (classe.player.position_x  > 0 ) :
                    classe.player.position_x -= 1
                    print(valeur)
                    spawner.spawn_entity(classe.player)
                    return valeur


            elif valeur == "d":
                accept = True
                if (classe.player.position_x < 8) :
                    classe.player.position_x += 1
                    print(valeur)
                    spawner.spawn_entity(classe.player)
                    return valeur

            elif valeur == "exit":
                exit()
            
            elif valeur == "i" or valeur == "inventory" :
                valeur = True
                clear.clear()
                inventory.print_inventory()
                print(sentence.exit_inventory)  
                classe.player.show_inventory("")
                boss_stone = inv_panel.inventory(classe.player)
                if boss_stone == "Boss Stone" :
                    spawner.spawn_entity(classe.player, True)
                return valeur
            
            elif valeur == "a" or valeur == "armory" :
                valeur = True
                clear.clear()
                inventory.print_armory()
                print(sentence.exit_armory)  
                classe.player.show_inventory("weapon")
                inv_panel.inventory(classe.player, "weapon")
                return valeur
            
            elif valeur == "shop" :
                valeur = True
                clear.clear()
                inventory.print_shop()
                print(sentence.exit_shop)
                classe.player.show_inventory("shop")
                inv_panel.inventory(classe.player, "shop")


            
            elif valeur == "save":
                save.save(classe.player)
            elif valeur == "":
                valeur = True
                clear.clear()
                arbre.drawMap("s")

            elif valeur == "about" or valeur == "commands" or valeur == "command" :
                clear.clear()
                about()
            else:
                print(sentence.invalid_choice)
        except ValueError :
            print(sentence.invalid_choice)

def play():
    #Draw the player and the map.
    #Change the sprite of the player  when the direction change
    arbre.drawMap("s")
    old_position = ("s")
    while True:
        side = game()
        if (side != "s" and side != "q" and side != "d" and side != "z"):
            arbre.drawMap(old_position)
        else:
            arbre.drawMap(side)
            old_position = side



def about():
    clear.clear()
    ascii.print_ascii_text("Movement :", "other")
    print("")
    ascii.print_ascii_text("z : top", "other")
    print("")
    ascii.print_ascii_text("s : bottom", "other")
    print("")
    ascii.print_ascii_text("q : left", "other")
    print("")
    ascii.print_ascii_text("d : right", "other")
    print("")
    print("")
    ascii.print_ascii_text("Panels :", "other")
    print("")
    ascii.print_ascii_text("i : inventory", "other")
    print("")
    ascii.print_ascii_text("a : armory", "other")
    print("")
    ascii.print_ascii_text("shop : shop", "other")

    press_enter()
    clear.clear()
    arbre.drawMap("s")



def press_enter():
    print(sentence.press_enter_to_continue)

    keyboard.wait('enter')