import time
import sys

def draw_hp_ennemy(enemy ):
    hp = enemy.health

    lenght_hp = round( enemy.full_hp - (hp / enemy.full_hp * 10))

    for k in range(20):
        sys.stdout.write("\033[31m\u25A0\033[0m")
        sys.stdout.flush()
        time.sleep(0.05)  



    sys.stdout.write('\r')

    for j in range(lenght_hp*2):
        sys.stdout.write("\033[37m\u25A0\033[0m")
        sys.stdout.flush()
        time.sleep(0.1)
        
        

    
    for i in range(20-lenght_hp*2):
        sys.stdout.write("\033[31m\u25A0\033[0m")
        sys.stdout.flush()
    
    print( "    " , hp, "/", enemy.full_hp)

def draw_hp_player(player):
    hp = player.health

    lenght_hp = round( player.full_hp - (hp / player.full_hp * 10))

    for k in range(20):
        sys.stdout.write("\033[32m\u25A0\033[0m")
        sys.stdout.flush()
        time.sleep(0.05)  



    sys.stdout.write('\r')

    for j in range(lenght_hp*2):
        sys.stdout.write("\033[37m\u25A0\033[0m")
        sys.stdout.flush()
        time.sleep(0.1)
        
        

    
    for i in range(20-lenght_hp*2):
        sys.stdout.write("\033[32m\u25A0\033[0m")
        sys.stdout.flush()
    
    print( "    " , hp, "/", player.full_hp, end= "")



