import os

def run(enemy, player):
    status = False
    chance_of_escape =  (player.speed - enemy.speed) 

    if chance_of_escape > 0 :
        status = True
    else :
        can_escape = int.from_bytes(os.urandom(1), "big") % 3 + 1

        if can_escape == 1:
            status = True


    return status