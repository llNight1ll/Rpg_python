class Entity :
  def __init__(self, name, weapon, health, strength, position_x ,position_y):
    self.name = name
    self.weapon = weapon
    self.health = health
    self.strength = strength
    self.inventory = []
    self.position_x = position_x
    self.position_y = position_y
  

  def __str__(self):
    return self.name

  def level_up(self,nb_lvl):
    self.strength += nb_lvl
    self.health += nb_lvl

  def attack(self):
    pass
  



class person(Entity) :

  def __init__(self,name,age,job, position_x,position_y):
    super().__init__(name,3,10,1, position_x, position_y)
    self.age = age
    self.job = job
    #self.inventory.append(health_potion("vie","health",1))
    self.position_x = position_x
    self.position_y = position_y

  def level_up(self, nb_lvl):
    age += 1
    super().level_up(nb_lvl)

  def use_inventory (self, id):
    for item in self.inventory:
      print(item)
    choice = int(input())
    self.inventory[choice].use(self)
    self.inventory.pop(choice)

player = person("Bob",25,"Guerrier",5,0)
#Player2 = person("Bobby",45,"Mage")
#player.level_up(5)

#print(player.health)
#print(Player2.health)


class monster(Entity) :
  def __init__(self,name, monster_type):

    self.monster_type = monster_type
    self.inventory.append(health_potion("vie","health",1))

    if monster_type == "Dragon":
      super().__init__(name,50,100,10)
    else :
      super().__init__(name,5,10,1)

#Monster1 = monster("Gloub","Dragon")
#Monster2 = monster("Glouby","Gobelin")