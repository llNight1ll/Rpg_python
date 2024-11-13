import create_game
import save
import classe
import sentence
import clear
import intro
import time
import print_hp_ascii  as ascii
import keyboard
def start():
    #Start options
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

            #Start a new game
            if valeur == 1:
                accept = True
                print(valeur)
                clear.clear()
                name = str(input(sentence.enter_your_name))
                classe.player.name = name
                try:
                    intro.print_introduction()
                except :
                    print(sentence.invalid_choice)
                    time.sleep(2)
                    start()

            #Load a game
            elif valeur == 2:
                accept = True
                print(valeur)
                save.load_game(classe.player)
                create_game.create_game()

            #Show commands
            elif valeur == 3:
                accept = True
                print(valeur)
                about()
            
            #Quit the game
            elif valeur == 4:
                accept = True
                print(valeur)
                exit()
            else:
                print(sentence.invalid_choice)

        except ValueError :

            print(sentence.invalid_choice)


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
    start()



def press_enter():
    print(sentence.press_enter_to_continue)

    keyboard.wait('enter')