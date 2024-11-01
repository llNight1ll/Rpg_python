class Entity :
  def __init__(self, name, weapon, health, strength, defence, lvl, full_hp):
    self.name = name
    self.weapon = weapon
    self.health = health
    self.strength = strength
    self.defence = defence
    self.lvl = lvl
    self.full_hp = full_hp
  

  def __str__(self):
    return self.name

  def level_up(self,nb_lvl, base_strenght, base_health):
    self.strength += (2 * base_strenght * nb_lvl )/100 + nb_lvl + 10
    self.full_hp += ( (2 * base_health + 40 )* nb_lvl )/100 + nb_lvl + 10
    self.health = self.full_hp

  def attack(self):
    pass
    
  def loose_hp(self, hp):
    self.health -= hp
    if self.health < 0 :
      self.health = 0

  



class person(Entity) :

  def __init__(self,name, position_x, position_y, lvl):
    self.lvl = lvl
    self.position_x = position_x
    self.position_y = position_y
    super().__init__(name,"poing",10,10,10, 1, 10)
    #self.inventory.append(health_potion("vie","health",1))
    self.inventory = []

 
  def level_up(nb_lvl):
    super().level_up(nb_lvl)

  def use_inventory (self, id):
    for item in self.inventory:
      print(item)
    choice = int(input())
    self.inventory[choice].use(self)
    self.inventory.pop(choice)

  def loose_hp(self,hp):
    super().loose_hp(hp)

player = person("Bob",5,0,1)



class monster(Entity) :
  def __init__(self, monster_type, lvl):

    self.monster_type = monster_type
    self.lvl = lvl
    self.weapon = "massue"


    if monster_type == "Orc":
      base_health = 20
      base_strenght = 1
      base_defence = 10
      if lvl > 1 :
        self.full_hp = base_health + round(lvl/(lvl-1) * base_health/4 + lvl)
        self.strenght = base_strenght + round(lvl/(lvl-1) * base_strenght/4 + lvl)
        self.defence = base_defence + round(lvl/(lvl-1) * base_defence/4 + lvl)
        self.health = self.full_hp
      else :
        self.full_hp = base_health
        self.strenght = base_strenght
        self.defence = base_defence
        self.health = self.full_hp


  def loose_hp(self,hp):
    super().loose_hp(hp)
