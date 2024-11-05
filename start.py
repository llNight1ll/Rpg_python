import create_game as create_game
import save as save
import classe as classe
def start():
    print("Main Menu :")
    print("1 - Create New Game")
    print("2 - Load Saved Game")
    print("3 - About")
    print("4 - Exit")
    accept = False
    while accept == False:
        try:
            valeur = None
            valeur = int(input("Enter your choice: "))

            if valeur == 1:
                accept = True
                print(valeur)
                create_game.create_game()

            elif valeur == 2:
                accept = True
                print(valeur)
                save.load_game(classe.player)
                create_game.create_game()

            elif valeur == 3:
                accept = True
                print(valeur)
                about()

            elif valeur == 4:
                accept = True
                print(valeur)
                exit()
            else:
                print("Invalid choice. Please try again.")

        except ValueError :

            print("Invalid choice. Please try again.")


def about():
    print("Movement :")
    print("z = top")
    print("s = bottom")
    print("q = left")
    print("d = right")
