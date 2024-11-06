

def inventory(player, type = ""):
    while True:
        try:
            value = None


            value = int(input("Enter your choice: "))


            if value == "exit" or value == 0:
                break
            else :
                print(type)
                player.delet_object(value,type)
                


        except ValueError :
            print("Invalid choice. Please try again.")