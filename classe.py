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

  def level_up(self,nb_lvl):
    self.strenght += (2 * self.base_strenght * nb_lvl )/100 + nb_lvl + 10
    self.full_hp += ( (2 * self.base_full_hp + 40 )* nb_lvl )/100 + nb_lvl + 10
    self.health = self.full_hp
    self.speed += (2 * self.base_speed * nb_lvl )/100 + nb_lvl + 10

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
    super().__init__(name,"poing",10,10,10, 1, 10,10,10,10,10,10)
    #self.inventory.append(health_potion("vie","health",1))
    self.inventory = []
  
  def gain_xp(self, xp):
    self.current_xp += xp

    if self.current_xp >= self.xp_to_next_lvl :
      while self.current_xp >= self.xp_to_next_lvl:
        self.current_xp -= self.xp_to_next_lvl
        self.level_up()
        print(self.lvl, "lvl")
        print("current xp ", self.current_xp)
        print("xp needeed", self.xp_to_next_lvl)
      
    
 
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

player = person("Bob",5,0)



class monster(Entity) :
  def __init__(self, monster_type, lvl):

    self.monster_type = monster_type


    if monster_type == "Orc":
      base_full_hp = 20
      base_health = base_full_hp
      base_strenght = 2
      base_defence = 5
      base_speed = 3
      if lvl > 1 :
        full_hp = base_health + round(lvl/(lvl-1) * base_health/4 + lvl)
        strenght = base_strenght + round(lvl/(lvl-1) * base_strenght/4 + lvl)
        defence = base_defence + round(lvl/(lvl-1) * base_defence/4 + lvl)
        speed = base_speed + round(lvl/(lvl-1) * base_speed/4 + lvl)

        health = full_hp
        super().__init__(monster_type,"massue",health,strenght,defence,lvl, full_hp,speed, base_strenght, base_defence, base_full_hp, base_speed )

      else :
        speed = base_speed
        full_hp = base_health
        strenght = base_strenght
        defence = base_defence
        health = full_hp
        super().__init__(monster_type,"massue",health,strenght,defence,lvl, full_hp,speed)



  def loose_hp(self,hp):
    super().loose_hp(hp)

1.