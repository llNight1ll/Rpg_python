import os
import classe as classe

VERT = "\033[92m"
MARRON = "\033[33m"
RESET = "\033[0m"
BLEU = "\033[94m"

arbre = r"""
           ++           
          ++++          
         ++++++         
        ++++++++        
       ++++++++++       
        ++++++++        
       ++++++++++       
      ++++++++++++      
       ++++++++++       
     ++++++++++++++     
    ++++++++++++++++    
       ++++++++++       
           **           
"""

player = r"""
                        
                        
                        
      @@@@@@@@@@@@@     
      @@@@@@@@@@@@@     
      @@@@@@@@@@@@@     
      @@@@@@@@@@@@@     
      @@@@@@@@@@@@@     
      @@@@@@@@@@@@@     
      @@@@@@@@@@@@@     
                        
                        
                        
                        
"""

# Afficher le motif avec des couleurs
def print_arbre(number_of_tree):
    for ligne in arbre.splitlines():
        ligne_coloree = ligne.replace("+", f"{VERT}+{RESET}").replace("*", f"{MARRON}*{RESET}")
        for i in range(number_of_tree):
            print(ligne_coloree + "                     ", end="")
        print("")

def print_player():
    for ligne in player.splitlines():
        ligne_coloree = ligne.replace("@", f"{BLEU}+{RESET}")
        print(ligne_coloree+ "                     ")

def print_arbre_player(number_of_tree):
    ligne_player = player.splitlines()
    ligne_arbre = arbre.splitlines()
    
    for ligne_p, ligne_a in zip(ligne_player, ligne_arbre):
        ligne_coloree = ligne_a.replace("+", f"{VERT}+{RESET}").replace("*", f"{MARRON}*{RESET}")
        for i in range(number_of_tree):
            print(ligne_coloree + "                     ", end="")
        
        print(ligne_p + "                     ", end="")
         
        for j in range(9- number_of_tree - 1):
            print(ligne_coloree + "                     ", end="")

        
        print("")
    
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
    x = classe.player.position_x
    y = classe.player.position_y
    l_map[y][x] = "●"

    for k in range(9):
        if k != y :
            print_arbre(9)
        else :
           print_arbre_player(9-(9-x) -1)        

 
    print("position :" , str(x), str(y))


def move_cursor_up(x):
    print(f"\033[{x}A", end='')