import print_hp_ascii  as ascii
import classe
import keyboard
import sentence
import clear
import create_game


def press_enter():
    print(sentence.press_enter_to_continue)

    keyboard.wait('enter')

def print_introduction():
    name = classe.player.name
    text = "Hi " + name
    type = "other"
    delay = 0.02
    ascii.print_ascii_text(text, type, delay)
    text= "You wake up in the middle of a forest surrounded by monsters."
    press_enter()
    clear.clear()
    ascii.print_ascii_text(text, type, delay)
    text = "To escape this forest you must beat the Boss who can be found with a special stone."
    press_enter()
    clear.clear()
    ascii.print_ascii_text(text, type, delay)
    text = "This stone is selled by a merchant but it is very expensive."
    press_enter()
    clear.clear()
    ascii.print_ascii_text(text, type, delay)
    text = "Prepare youself and earn coins by beating the different monsters you will encounter."
    press_enter()
    clear.clear()
    ascii.print_ascii_text(text, type, delay)
    text = "But be carefull, because the deeper you will go, the stronger the monsters will be."
    press_enter()
    clear.clear()
    ascii.print_ascii_text(text, type, delay)
    text = "I wish you good luck " + name
    press_enter()
    clear.clear()
    create_game.create_game()
