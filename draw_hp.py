import time
import sys
import print_hp_ascii as ascii

def draw_hp_ennemy(enemy ):
    hp = enemy.health

    lenght_hp = round((enemy.full_hp - hp) * 20 / enemy.full_hp)
         
    indent = " " * 400
    sys.stdout.write(indent)   

    for k in range(20):


        sys.stdout.write("\033[31m\u25A0\033[0m")
        sys.stdout.flush()
        time.sleep(0.05)  



    sys.stdout.write('\r')

    indent = " " * 400
    sys.stdout.write(indent)
    for j in range(lenght_hp):

        sys.stdout.write("\033[37m\u25A0\033[0m")
        sys.stdout.flush()
        time.sleep(0.1)
        
        

    
    for i in range(20 - lenght_hp):
        sys.stdout.write("\033[31m\u25A0\033[0m")
        sys.stdout.flush()

    print("")
    hp_string = str(hp) + "/" + str(enemy.full_hp)
    lvl_string = "lvl " + str(enemy.lvl)
    ascii.print_ascii_number(hp_string, "")
    ascii.print_ascii_number(lvl_string, "")

       
    

def draw_hp_player(player):
    hp = player.health

    lenght_hp = round((player.full_hp - hp) * 20 / player.full_hp)

    indent = " " * 50
    sys.stdout.write(indent)

    for k in range(20):
        sys.stdout.write("\033[32m\u25A0\033[0m")
        sys.stdout.flush()
        time.sleep(0.05)  



    sys.stdout.write('\r')

    indent = " " * 50
    sys.stdout.write(indent)

    for j in range(lenght_hp):
        sys.stdout.write("\033[37m\u25A0\033[0m")
        sys.stdout.flush()
        time.sleep(0.1)
        
        

    
    for i in range(20 - lenght_hp):
        sys.stdout.write("\033[32m\u25A0\033[0m")
        sys.stdout.flush()
    
    print("")
    hp_string = str(hp) + "/" + str(player.full_hp)
    lvl_string = "lvl " + str(player.lvl)
    ascii.print_ascii_number(hp_string, "player")
    ascii.print_ascii_number(lvl_string, "player")




