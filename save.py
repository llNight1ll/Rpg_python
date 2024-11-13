import pickle

def save(player):
    #Write the player datas into a file.dat
    save_file ="save.dat"
    data = {
        "name": player.name,
        "position_x": player.position_x,
        "position_y": player.position_y,
        "base_full_hp": player.base_full_hp,
        "base_defence": player.base_defence,
        "base_strenght": player.base_strenght,
        "base_speed": player.base_speed,
        "full_hp": player.full_hp,
        "defence": player.defence,
        "strenght": player.strenght,
        "health": player.health,
        "speed": player.speed,
        "current_xp": player.current_xp,
        "xp_to_next_lvl": player.xp_to_next_lvl,
        "lvl": player.lvl,
        "weapon": player.weapon,
        "inventory": player.inventory,
        "armory": player.armory,
        "money": player.money,
        "equiped_weapon": player.equiped_weapon

    }
    try :
        with open(save_file, "wb") as file:
            pickle.dump(data, file)
        print("Save is terminated")
    except :
        print("Save has failed")


def load_game(player, save_file="save.dat"):
    #Load the game
    try:
        with open(save_file, "rb") as file:
            data = pickle.load(file)
            
            player.name = data["name"]
            player.position_x = data["position_x"]
            player.position_y = data["position_y"]
            player.base_full_hp = data["base_full_hp"]
            player.base_defence = data["base_defence"]
            player.base_strenght = data["base_strenght"]
            player.base_speed = data["base_speed"]
            player.full_hp = data["full_hp"]
            player.defence = data["defence"]
            player.strenght = data["strenght"]
            player.health = data["health"]
            player.speed = data["speed"]
            player.current_xp = data["current_xp"]
            player.xp_to_next_lvl = data["xp_to_next_lvl"]
            player.lvl = data["lvl"]
            player.weapon = data["weapon"]
            player.inventory = data["inventory"]
            player.armory = data["armory"]
            player.money = data["money"]
            player.equiped_weapon = data["equiped_weapon"]

            print("Game loaded successfully.")
            
    except FileNotFoundError:
        print("Save file not found. Starting a new game.")
