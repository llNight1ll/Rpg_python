import create_game
import save
import classe
import sentence
import clear
import intro
def start():
    print(sentence.main_menu)
    print(sentence.create_new_game)
    print(sentence.load_saved_game)
    print(sentence.about)
    print(sentence.exit)
    accept = False
    while accept == False:
        try:
            valeur = None
            valeur = int(input(sentence.enter_your_choice))

            if valeur == 1:
                accept = True
                print(valeur)
                clear.clear()
                name = str(input(sentence.enter_your_name))
                classe.player.name = name
                intro.print_introduction()

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
                print(sentence.invalid_choice)

        except ValueError :

            print(sentence.invalid_choice)


def about():
    print("Movement :")
    print("z = top")
    print("s = bottom")
    print("q = left")
    print("d = right")
