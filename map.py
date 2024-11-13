import classe
import os
import print_hp_ascii as ascii

def clear_console():
    #Clear console
    if os.name == 'nt':
        os.system('cls')


def drawMap():
    clear_console()
    #Create the map
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
    #Print the map
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

