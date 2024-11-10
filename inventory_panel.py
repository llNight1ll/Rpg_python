import sentence as sentence

def inventory(player, type = ""):
    while True:
        try:
            value = None


            value = int(input(sentence.enter_your_choice))


            if value == "exit" or value == 0:
                break
            else :
                hase_used = player.delet_object(value,type)
                return hase_used
                


        except ValueError :
            print(sentence.invalid_choice)