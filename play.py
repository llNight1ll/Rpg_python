import  map as map
import classe as classe
import spawner_entity as spawner
import arbre as arbre
import print_inventory as inventory

side = "s"


def game():
    accept = False
    while accept == False:
        try:
            valeur = None
            valeur = str(input("Enter your choice: "))

            if valeur == "z":
                accept = True
                if (classe.player.position_y  > 0) :
                    classe.player.position_y -= 1
                    print(valeur)
                    spawner.spawn_entity(classe.player)
                    spawner.spawn_entity()
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
                inventory.print_inventory()
                classe.player.show_inventory()
            else:
                print("Invalid choice. Please try again.")
        except ValueError :
            print("Invalid choice. Please try again.")

def play():
    arbre.drawMap("s")
    old_position = ("s")
    while True:
        print("Enter your move (z, s, q, d):")
        side = game()
        if (side != "s" and side != "q" and side != "d" and side != "z"):
            arbre.drawMap(old_position)
        else:
            arbre.drawMap(side)
            old_position = side
