import time
import orc
import clear

fight = r"""
  ______  _____  _____  _    _  _______ 
 |  ____||_   _|/ ____|| |  | ||__   __|
 | |__     | | | |  __ | |__| |   | |   
 |  __|    | | | | |_ ||  __  |   | |   
 | |      _| |_| |__| || |  | |   | |   
 |_|     |_____|\_____||_|  |_|   |_|   
                                        
                                        
"""

def print_fight(enemy):

    indent = " " * 250

    fight_centered = "\n".join([ indent + line1 for line1 in fight.splitlines()])

    for i in range(20) :
        if (i + 1) % 2 == 0:
            clear.clear()
        else :
            print(fight_centered)
            time.sleep(0.1)
            clear.clear()
                
    orc.neutre(enemy)



