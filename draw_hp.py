import time
import sys

def draw_hp_ennemy(damage, color, max_hp, old_hp ):
    hp = max_hp - damage

    lenght_hp = round(damage/max_hp * 10)

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
    
    print( "    " , hp, "/", max_hp)
    draw_hp_player(15, "green", 50, 45)

def draw_hp_player(damage, color, max_hp, old_hp ):
    hp = max_hp - damage

    lenght_hp = round(damage/max_hp * 10)

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
    
    print( "    " , hp, "/", max_hp, end= "")

    

  


   

draw_hp_ennemy(40, "red", 100, 100)


