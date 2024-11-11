import classe as classe
import clear as clear
import print_hp_ascii as ascii
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



player_side_right = r"""
      @@@@@@@@%         
   @@%#######%@@+       
  @%###%%%%%%#%%@@      
 @%%%%#####%%%%@@%%     
@@%%%%%%%%%@@.:*-:      
  @@%%%%%@@--..:::      
   @@@@@@==::::::       
     @@....@@@%         
    @-........-@+       
   @@-...@@..-+@+       
   @@-...@@--:=@@       
     @@%%%%@@@@         
       @@@@@@           
"""

player_side_left = r"""
       @@@@@@@@%       
    @@%#######%@@+     
   @@%%#%%%%%%%#%%@    
 %%%@@%%%%#####%%%%@   
   :*-.@@%%%%%%%%%@    
   :::..--@@%%%%%@@    
    :::==@@@@@@@       
     %@@....@@         
   +@-........-@       
   +@+-..@@...-@@      
   @@=-..@@..-@@       
      @@@@@%%%%@       
       @@@@@@@         
"""

player_side_front = r"""
       @@@@@@:         
     @@#%%%%#@@@@      
   @@##%%%%%%##@@@*    
@@%%%%%@@@%%%%%%%%@@   
@@%%%@@:::@@@%%%%%@@   
 =@@@::.....:%@@@@*    
 =@-:..@....@:.::@*    
   --..:....-:.--      
 +@::::......::::@#    
@%-::..::::::::::-#@   
  @@@::........@@@#    
   @@%%%@@@@%%%@@      
     @@@    @@@        
"""

player_side_back = r"""
       @@@@@@:         
   @@@@#%%%%#@@@@      
 =@@@##%%%%%%##@@@*    
@@%%%##########%%%@@   
@@%%%%%######%%%%%@@   
 =@%%%%%%%%%%%%%%@*    
 =@@@%%%%%%%%%%@@@*    
   @@%%%%%%%%%%@@      
=+@::@@@@@@@@@@::@+    
@%-::........::::-#@   
 *@@@::........@@@#    
   @@%%%@@@@%%%@@      
     @@@    @@@        
"""

player = player_side_back

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

def print_arbre_player(number_of_tree,player_sprite):
    ligne_player = player_sprite.splitlines()
    ligne_arbre = arbre.splitlines()
    
    for ligne_p, ligne_a in zip(ligne_player, ligne_arbre):
        ligne_coloree = ligne_a.replace("+", f"{VERT}+{RESET}").replace("*", f"{MARRON}*{RESET}")
        for i in range(number_of_tree):
            print(ligne_coloree + "                     ", end="")
        
        print(ligne_p + "                     ", end="")
         
        for j in range(9- number_of_tree - 1):
            print(ligne_coloree + "                     ", end="")

        
        print("")
    


def drawMap(side):
    clear.clear()
    m = 9
    n = 9
    l_map = [[" " for _ in range(m)] for _ in range(n)]
    x = classe.player.position_x
    y = classe.player.position_y
    l_map[y][x] = "●"

    if side == "z":
        player = player_side_back
    elif side == "q":
        player = player_side_left
    elif side == "d":
        player = player_side_right
    elif side == "s":
        player = player_side_front
    for k in range(9):
        if k != y :
            print_arbre(9)
        else :
           print_arbre_player(9-(9-x) -1, player)        

    
    position = "position " + str(x) + " : " + str(y)
    ascii.print_ascii_text(position, "other")


def move_cursor_up(x):
    print(f"\033[{x}A", end='')