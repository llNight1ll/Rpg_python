import  map as map
import classe as classe
import spawner_enemy as spawner
import arbre as arbre


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
                    spawner.spawn_ennemy()

                
            elif valeur == "s":
                accept = True
                if (classe.player.position_y < 8) :
                    classe.player.position_y += 1
                    print(valeur)
                    spawner.spawn_ennemy()


            elif valeur == "q":
                accept = True
                if (classe.player.position_x  > 0 ) :
                    classe.player.position_x -= 1
                    print(valeur)
                    spawner.spawn_ennemy()


            elif valeur == "d":
                accept = True
                if (classe.player.position_x < 8) :
                    classe.player.position_x += 1
                    print(valeur)
                    spawner.spawn_ennemy()

            elif valeur == "exit":
                exit()
            else:
                print("Invalid choice. Please try again.")
        except ValueError :
            print("Invalid choice. Please try again.")

def play():
    while True:
        arbre.drawMap()
        print("Enter your move (z, s, q, d):")
        game() 
