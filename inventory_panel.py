

def inventory(player):
    accept = False
    while accept == False:
        try:
            value = None


                
            value = int(input("Enter y: "))
            print("caca", value)


            if value == "exit" or value == 0:
                accept = True
                break
            else :

                accept = True
                player.delet_object(value)
                


        except ValueError :
            print("Invalid choice. Please try again.")