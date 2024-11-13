import sentence
import clear
import arbre
import print_hp_ascii as ascii

def inventory(player, type = ""):
    #Inventory, armory, shop function
    while True:
        try:
            value = None


            value = int(input(sentence.enter_your_choice))

            #Exit inventory, armory, shop
            if value == "exit" or value == 0:
                clear.clear()
                arbre.drawMap("s")
                break
            #Use object/weapon
            else :
                if type != "shop":
                    hase_used = player.delet_object(value,type)
                    return hase_used
                else :

                    player.delet_object(value,type)



        except ValueError :
            print("")
            ascii.print_ascii_text("no object with this id has been found", "other")