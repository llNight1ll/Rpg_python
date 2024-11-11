import print_hp_ascii as ascii

class Potion :
  def __str__(self):
        return f"{self.name} (Level {self.lvl}) - Quantity: {self.quantity}"
      
  def __init__(self, name, lvl):
    self.name = name
    self.lvl = lvl
    self.quantity = 1

    if self.name == "Heal Potion" :

      self.effect = self.heal_effect
      self.price = 200 * lvl

    if self.name == "Strenght Potion" :

      self.effect = self.strenght_effect
      self.price = 150 * lvl

    
    if self.name == "Speed Potion" :

      self.effect = self.speed_effect
      self.price = 150 * lvl


    if self.name == "Defence Potion" :
      self.effect = self.defence_effect
      self.price = 150 * lvl

    



  def heal_effect(self, player):

    if player.health == player.full_hp :
      self.quantity += 1
      return

    heal =  round(player.full_hp * 0.2) * self.lvl


    player.health += heal
    if player.health > player.full_hp :
      player.health = player.full_hp

  def strenght_effect(self, player):

    strenght =  round(player.strenght * 0.2)  * self.lvl

    player.strenght += strenght

  def speed_effect(self, player):
  
    speed =  round(player.speed * 0.2)  * self.lvl

    player.speed += speed

  def defence_effect(self, player):
  
    defence =  round(player.defence * 0.2)  * self.lvl

    player.defence += defence


heal_potion = Potion("Heal Potion", 1)
heal_potion_lvl_2 = Potion("Heal Potion", 2)
heal_potion_lvl_3 = Potion("Heal Potion", 3)
heal_potion_lvl_4 = Potion("Heal Potion", 4)

strenght_potion = Potion("Strenght Potion", 1)
strenght_potion_lvl_2 = Potion("Strenght Potion", 2)
strenght_potion_lvl_3 = Potion("Strenght Potion", 3)
strenght_potion_lvl_4 = Potion("Strenght Potion", 4)

defence_potion = Potion("Defence Potion", 1)
defence_potion_lvl_2 = Potion("Defence Potion", 2)
defence_potion_lvl_3 = Potion("Defence Potion", 3)
defence_potion_lvl_4 = Potion("Defence Potion", 4)

speed_potion = Potion("Speed Potion", 1)
speed_potion_lvl_2 = Potion("Speed Potion", 2)
speed_potion_lvl_3 = Potion("Speed Potion", 3)
speed_potion_lvl_4 = Potion("Speed Potion", 4)



class Weapon :
  def __str__(self):
        if self.health >= 0 :
          return f"{self.name} (Level {self.lvl}) - Health: {self.health} - Additional damage: {self.damage}"
        else :          
          return f"{self.name} (Level {self.lvl}) - Additional damage: {self.damage}"
      
  
  
  def __init__(self, name, lvl):
    self.name = name
    self.lvl = lvl
    self.quantity = 1
    self.health = 0
    self.damage = 0

    if name == "Fist" :
      self.health = -1
    
    if name == "Cut" :
      self.damage = 15 * lvl 
      self.health = 50
      self.price = 1500 * lvl


    elif name == "Blade" :
      self.damage =  25 * lvl 
      self.health = 40
      self.price = 5000 * lvl


    elif name == "Railgun" :
      self.damage =  50 * lvl 
      self.health = 10
      self.price = 50000 * lvl



fist = Weapon("Fist", 1)

blade = Weapon("Blade", 1)
blade_lvl_2 = Weapon("Blade", 2)
blade_lvl_3 = Weapon("Blade", 3)
blade_lvl_4 = Weapon("Blade", 4)

cut = Weapon("Cut", 1)
cut_lvl_2 = Weapon("Cut", 2)
cut_lvl_3 = Weapon("Cut", 3)
cut_lvl_4 = Weapon("Cut", 4)

railgun = Weapon("Railgun", 1)
railgun_lvl_2 = Weapon("Railgun", 2)
railgun_lvl_3 = Weapon("Railgun", 3)
railgun_lvl_4 = Weapon("Railgun", 4)










class Entity :
  def __init__(self, name, weapon, health, strenght, defence, lvl, full_hp, speed, base_strenght, base_defence, base_full_hp, base_speed):
    self.name = name
    self.weapon = weapon
    self.health = health
    self.strenght = strenght
    self.defence = defence
    self.lvl = lvl
    self.full_hp = full_hp
    self.speed = speed
    self.base_strenght = base_strenght
    self.base_defence = base_defence
    self.base_full_hp = base_full_hp
    self.base_speed = base_speed



  

  def __str__(self):
    return self.name

  def level_up(self):
    self.lvl += 1
    self.strenght += round((2 * int(self.base_strenght) * int(self.lvl) )/100 + int(self.lvl) + 10)
    self.full_hp += round(( (2 * int(self.base_full_hp + 40) )* int(self.lvl) )/100 + int(self.lvl) + 10)
    self.health = int(self.full_hp)
    self.speed += round((2 * int(self.base_speed) * int(self.lvl) )/100 + int(self.lvl) + 10)
    self.xp_to_next_lvl = round(1.5 * int(self.xp_to_next_lvl))


    
  def loose_hp(self, hp):
    self.health -= hp
    if self.health < 0 :
      self.health = 0

  



class person(Entity) :

  def __init__(self,name, position_x, position_y):
    self.position_x = position_x
    self.position_y = position_y
    self.current_xp = 0
    self.xp_to_next_lvl =  5
    self.inventory = {}
    self.armory = {}
    self.shop = {}
    self.money = 1000000
    self.equiped_weapon = fist    

    super().__init__(name,fist,10,5,3, 1, 10,4,5,3,10,4)
  
  def gain_xp(self, xp):
    self.current_xp += xp

    if self.current_xp >= self.xp_to_next_lvl :
      while self.current_xp >= self.xp_to_next_lvl:
        self.current_xp -= self.xp_to_next_lvl
        self.level_up()
        ascii.print_ascii_text(str(self.lvl) + "lvl", "other")
        ascii.print_ascii_text("current xp " + str(self.current_xp), "other")
        ascii.print_ascii_text("xp needeed" + str(self.xp_to_next_lvl), "other")
      
  def gain_money(self, money):
    self.money += money
 
  def level_up(self):
    super().level_up()

 

  def add_object(self,object, type):
    if type != "weapon" and type != "shop":

      for id, object_in_inventory in self.inventory.items():
        
        if  object_in_inventory.name == object.name and object_in_inventory.lvl == object.lvl :
            object_in_inventory.quantity += 1
            return

      self.inventory[len(self.inventory) + 1] = object
    
    elif type == "weapon" :

      for id, object_in_inventory in self.armory.items():
        
        if  object_in_inventory.name == object.name and object_in_inventory.lvl == object.lvl :
            object_in_inventory.quantity += 1
            return

      self.armory[len(self.armory) + 1] = object

    elif type == "shop" :
      for id, object_in_inventory in self.shop.items():
        
        if  object_in_inventory.name == object.name and object_in_inventory.lvl == object.lvl :
            object_in_inventory.quantity += 1
            return

      self.shop[len(self.shop) + 1] = object



  def delet_object(self, id, type):
    has_used_item = False
    if type != "weapon" and type != "shop":  
      if id in self.inventory:
            self.inventory[id].quantity -= 1
            self.inventory[id].effect(player)
            if  self.inventory[id].quantity == 0 :
              del self.inventory[id]
              has_used_item = True
              return has_used_item
              
      else:
        ascii.print_ascii_text("No object with this ID has been found", "other")
    elif type == "weapon" :      
      if id in self.armory:
          self.equiped_weapon = self.armory[id]
          ascii.print_ascii_text(self.equiped_weapon, "other")
          has_used_item = True
          return has_used_item
              
      else:
        ascii.print_ascii_text("No object with this ID has been found", "other")
    
    elif type == "shop" :
      if id in self.shop:

        if  isinstance(self.shop[id], Potion):
          if self.money >= self.shop[id].price:    
            self.add_object(self.shop[id], "")
            self.money -= self.shop[id].price
            ascii.print_ascii_text("You have now " + str(self.money) + " coins", "other")

          else : 
            ascii.print_ascii_text("You dont have enought money to buy this", "other")

        elif  isinstance(self.shop[id], Weapon):
          if self.money >= self.shop[id].price:    
            self.add_object(self.shop[id], "weapon")
            self.money -= self.shop[id].price
            ascii.print_ascii_text("You have now " + str(self.money) + " coins", "other")

          else : 
            ascii.print_ascii_text("You dont have enought money to buy this", "other")
        
        

              
      else:
        ascii.print_ascii_text("No object with this ID has been found", "other")


    
  def show_inventory(self, type):
    if type != "weapon" and type != "shop":
      ascii.print_ascii_text("Coins : " +  str(self.money), "other")
      for id, object in self.inventory.items():
          ascii.print_ascii_text(f"{id} - : {object}","other")
    elif type == "weapon" :
      for id, object in self.armory.items():
          if object == self.equiped_weapon:
            ascii.print_ascii_text(f"{id} - : {object} Equiped", "other")
          else:
            ascii.print_ascii_text(f"{id} - : {object}", "other")

    elif type == "shop":
        for id, object in self.shop.items():
          ascii.print_ascii_text(f"{id} - : {object} - Price: {object.price} Coins", "other")
          print("")


  def loose_hp(self,hp):
    super().loose_hp(hp)






class monster(Entity) :
  def __init__(self, monster_type, lvl):

    self.monster_type = monster_type



    if monster_type == "Gobelin":
      base_full_hp = 20
      base_health = base_full_hp
      base_strenght = 2
      base_defence = 3
      base_speed = 5
      self.xp = 5
      self.money = 100

      if lvl > 1 :
        full_hp = base_health + round(lvl/(lvl-1) * base_health/4 + lvl)
        strenght = base_strenght + round(lvl/(lvl-1) * base_strenght/4 + lvl)
        defence = base_defence + round(lvl/(lvl-1) * base_defence/4 + lvl)
        speed = base_speed + round(lvl/(lvl-1) * base_speed/4 + lvl)
        health = full_hp
        self.xp = 5 * lvl
        self.money = 30 * lvl
        super().__init__(monster_type,fist,health,strenght,defence,lvl, full_hp,speed, base_strenght, base_defence, base_full_hp, base_speed )

      else :
        speed = base_speed
        full_hp = base_health
        strenght = base_strenght
        defence = base_defence
        health = full_hp
        super().__init__(monster_type,fist,health,strenght,defence,lvl, full_hp,speed, base_strenght, base_defence, base_full_hp, base_speed )



    elif monster_type == "Orc":
      base_full_hp = 30
      base_health = base_full_hp
      base_strenght = 6
      base_defence = 7
      base_speed = 2
      self.xp = 10
      self.money = 300

      if lvl > 1 :
        full_hp = base_health + round(lvl/(lvl-1) * base_health/4 + lvl)
        strenght = base_strenght + round(lvl/(lvl-1) * base_strenght/4 + lvl)
        defence = base_defence + round(lvl/(lvl-1) * base_defence/4 + lvl)
        speed = base_speed + round(lvl/(lvl-1) * base_speed/4 + lvl)
        health = full_hp
        self.xp = 10 * lvl
        self.money = 30 * lvl
        super().__init__(monster_type,fist,health,strenght,defence,lvl, full_hp,speed, base_strenght, base_defence, base_full_hp, base_speed )

      else :
        speed = base_speed
        full_hp = base_health
        strenght = base_strenght
        defence = base_defence
        health = full_hp
        super().__init__(monster_type,fist,health,strenght,defence,lvl, full_hp,speed, base_strenght, base_defence, base_full_hp, base_speed )

        
  
    elif monster_type == "Boss":

      base_full_hp = 2000
      base_health = base_full_hp
      base_strenght = 500
      base_defence = 500
      base_speed = 500
      self.xp = 10000000
      self.money = 3000000


      speed = base_speed
      full_hp = base_health
      strenght = base_strenght
      defence = base_defence
      health = full_hp
      super().__init__(monster_type,fist,health,strenght,defence,lvl, full_hp,speed, base_strenght, base_defence, base_full_hp, base_speed )

        
    



  def loose_hp(self,hp):
    super().loose_hp(hp)


player = person("Bob",5,0)

player.add_object(fist, "weapon")
player.add_object(blade, "weapon")

player.add_object(blade, "shop")
player.add_object(blade_lvl_2, "shop")
player.add_object(blade_lvl_3, "shop")
player.add_object(blade_lvl_4, "shop")

player.add_object(cut, "shop")
player.add_object(cut_lvl_2, "shop")
player.add_object(cut_lvl_3, "shop")
player.add_object(cut_lvl_4, "shop")

player.add_object(railgun, "shop")
player.add_object(railgun_lvl_2, "shop")
player.add_object(railgun_lvl_3, "shop")
player.add_object(railgun_lvl_4, "shop")


player.add_object(heal_potion, "shop")
player.add_object(heal_potion_lvl_2, "shop")
player.add_object(heal_potion_lvl_3, "shop")
player.add_object(heal_potion_lvl_4, "shop")

player.add_object(strenght_potion, "shop")
player.add_object(strenght_potion_lvl_2, "shop")
player.add_object(strenght_potion_lvl_3, "shop")
player.add_object(strenght_potion_lvl_4, "shop")

player.add_object(defence_potion, "shop")
player.add_object(defence_potion_lvl_2, "shop")
player.add_object(defence_potion_lvl_3, "shop")
player.add_object(defence_potion_lvl_4, "shop")

player.add_object(speed_potion, "shop")
player.add_object(speed_potion_lvl_2, "shop")
player.add_object(speed_potion_lvl_3, "shop")
player.add_object(speed_potion_lvl_4, "shop")















