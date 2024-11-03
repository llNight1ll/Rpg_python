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

  def attack(self):
    pass
    
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

    super().__init__(name,"poing",10,10,10, 1, 10,10,10,10,10,10)
    #self.inventory.append(health_potion("vie","health",1))
  
  def gain_xp(self, xp):
    self.current_xp += xp

    if self.current_xp >= self.xp_to_next_lvl :
      while self.current_xp >= self.xp_to_next_lvl:
        self.current_xp -= self.xp_to_next_lvl
        self.level_up()
        print(self.lvl, "lvl")
        print("current xp ", self.current_xp)
        print("xp needeed", self.xp_to_next_lvl)
      
    
 
  def level_up(self):
    super().level_up()

  def use_inventory (self, id):
    for item in self.inventory:
      print(item)
    choice = int(input())
    self.inventory[choice].use(self)
    self.inventory.pop(choice)



  def add_object(self,name, quantity, lvl):

    object_name = (name, lvl)

    if object_name in self.inventory:
        self.inventory[object_name] += quantity
    else:
        self.inventory[object_name] = quantity

  def delet_object(self, name, quantity, lvl):
    object_name = (name, lvl)
    if object_name in self.inventory:
        self.inventory[object_name] -= quantity
        if self.inventory[object_name] <= 0:
            del self.nventory[object_name]
    else:
        print("This object isn't in the inventory")

  def show_inventory(self):
    for (name, lvl), quantity in self.inventory.items():
        print(f"{name} (Lvl {lvl}) - Quantity: {quantity}")












  def loose_hp(self,hp):
    super().loose_hp(hp)

player = person("Bob",5,0)
player.add_object("Heal Potion", 3, 1)
player.add_object("Heal Potion", 2, 2)
player.add_object("Strenght Potion", 1, 1)
player.delet_object("Speed Potion", 1, 1)




class monster(Entity) :
  def __init__(self, monster_type, lvl):

    self.monster_type = monster_type



    if monster_type == "Orc":
      base_full_hp = 20
      base_health = base_full_hp
      base_strenght = 2
      base_defence = 5
      base_speed = 3
      self.xp = 5

      if lvl > 1 :
        full_hp = base_health + round(lvl/(lvl-1) * base_health/4 + lvl)
        strenght = base_strenght + round(lvl/(lvl-1) * base_strenght/4 + lvl)
        defence = base_defence + round(lvl/(lvl-1) * base_defence/4 + lvl)
        speed = base_speed + round(lvl/(lvl-1) * base_speed/4 + lvl)
        health = full_hp
        self.xp = 5 * lvl
        super().__init__(monster_type,"massue",health,strenght,defence,lvl, full_hp,speed, base_strenght, base_defence, base_full_hp, base_speed )

      else :
        speed = base_speed
        full_hp = base_health
        strenght = base_strenght
        defence = base_defence
        health = full_hp
        super().__init__(monster_type,"massue",health,strenght,defence,lvl, full_hp,speed, base_strenght, base_defence, base_full_hp, base_speed )



  def loose_hp(self,hp):
    super().loose_hp(hp)

class Potion :
      
  def __init__(self, name, lvl):
    self.name = name
    self.effect = ""
    self.lvl = lvl

    if self.name == "Heal Potion" :

      self.effect = self.heal_effect

    if self.name == "Strenght Potion" :

      self.effect = self.strength_effect
    
    if self.name == " Speed Potion" :

      self.effect = self.speed_effect

    if self.name == "Defence Potion" :
      self.effect = self.defence_effect


  def heal_effect(self, player):

    heal =  round(player.full_hp * 0.2) * self.lvl

    player.health += heal
    if player.health > player.full_hp :
      player.health = player.full_hp

  def strength_effect(self, player):

    strenght =  round(player.strenght * 0.2)  * self.lvl

    player.strength += strenght

  def speed_effect(self, player):
  
    speed =  round(player.speed * 0.2)  * self.lvl

    player.speed += speed

  def defence_effect(self, player):
  
    defence =  round(player.defence * 0.2)  * self.lvl

    player.defence += defence


