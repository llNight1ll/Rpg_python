import sys
import clear

die = r"""


_____.___.                         ________   .__             .___
\__  |   |  ____   __ __           \______ \  |__|  ____    __| _/
 /   |   | /  _ \ |  |  \           |    |  \ |  |_/ __ \  / __ | 
 \____   |(  <_> )|  |  /           |    `   \|  |\  ___/ / /_/ | 
 / ______| \____/ |____/           /_______  /|__| \___  >\____ | 
 \/                                        \/          \/      \/ 


"""

def game_over():
    clear.clear()
    print (die)
    sys.exit(1)