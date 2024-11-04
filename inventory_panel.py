

def inventory(player):
    while True:
        try:
            value = None


            value = int(input("Enter your choice: "))


            if value == "exit" or value == 0:
                break
            else :

                player.delet_object(value)
                


        except ValueError :
            print("Invalid choice. Please try again.")