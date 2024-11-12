import classe
import os
import print_hp_ascii as ascii

def clear_console():
    # Pour Windows
    if os.name == 'nt':
        os.system('cls')
    # Pour Mac et Linux (os.name est 'posix')
    else:
        os.system('clear')

def drawMap():
    clear_console()
    m = 9
    n = 9
    l_map = [[" " for _ in range(m)] for _ in range(n)]
    i = 0
    x = classe.player.position_x
    y = classe.player.position_y
    l_map[y][x] = "●"

    print(" ", end="")
    while i  < 15 :
        print("_ ", end="" )
        i = i + 1

    print("")
    for k in range(9):
        for j in range(9):
            if j == 8:
                print(str(l_map[k][j]) + "🌲|", end="\n")
            elif j == 0 :
                print("|🌲" + str(l_map[k][j]) + "🌲", end="" )
            else :
                print(str(l_map[k][j]) + "🌲", end="")


    position = "position " + str(x) + " : " + str(y)
    ascii.print_ascii_text(position, "player")

