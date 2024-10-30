class Entity :
  def __init__(self, name, weapon, health, strength, defence, lvl):
    self.name = name
    self.weapon = weapon
    self.health = health
    self.strength = strength
    self.defence = defence
    self.lvl = lvl
  

  def __str__(self):
    return self.name

  def level_up(self,nb_lvl, base_strenght, base_health):
    self.strength += (2 * base_strenght * nb_lvl )/100 + nb_lvl + 10
    self.health += ( (2 * base_health + 40 )* nb_lvl )/100 + nb_lvl + 10

  def attack(self):
    pass
  



class person(Entity) :

  def __init__(self,name, position_x, position_y):
    self.position_x = position_x
    self.position_y = position_y
    super().__init__(name,"poing",10,10,10, 1)
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

player = person("Bob",5,0)



class monster(Entity) :
  def __init__(self, monster_type, lvl):

    self.monster_type = monster_type


    if monster_type == "Orc":
      base_health = 20
      base_strenght = 5
      base_defence = 10
      if lvl > 1 :
        hp = base_health + round(lvl/(lvl-1) * base_health/4 + lvl)
        strenght = base_strenght + round(lvl/(lvl-1) * base_strenght/4 + lvl)
        defence = base_defence + round(lvl/(lvl-1) * base_defence/4 + lvl)
      else :
        hp = base_health
        strenght = base_strenght
        defence = base_defence


      super().__init__(monster_type,"massue",hp,strenght,defence, lvl)
    else :
      super().__init__(name,5,10,1)

