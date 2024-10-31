import classe as classe

def fight(enemy):
    accept = False
    while classe.enemy.health
    while accept == False:
        try:
            valeur = None
            valeur = str(input("Enter your choice: "))

            if valeur == "1":
                accept = True
                print(valeur)
                # Player attacks enemy
                print("You hit the enemy!")
                # Enemy loses health
                # Check if enemy is defeated
                if enemy.health <= 0:
                    print("You defeated the enemy!")
                    accept = True
                else:
                    print(f"Enemy health: {enemy.health}")
        except ValueError :
            print("Invalid choice. Please try again.")
