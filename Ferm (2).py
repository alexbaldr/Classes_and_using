class Animals:
    #общие мотоды всех животных
   # weight = "250 кг" #вес животного
   # name = "Манька" # имя животного
   # sound = "Муууу" # голос животного
  eating = "голодный"

  def __init__(self, weight, name, sound):
    self.weight = weight
    self.name = name
    self.sound = sound

  def fed(self):
    self.eating = "сытый"
    print("покормить")


class Guse(Animals):
    def __init__(self, weight, name, sound):
        Animals.__init__(self, weight, name, sound)
        print(f"Необходимо собрать яйца у {name}")
    
    def take_eggs(self):
      self.take_eggs = "Яйца собраны"
      print("Собрать яйца")


class Cow (Animals):
  def __init__ (self,weight, name, sound):
    Animals.__init__(self,weight, name, sound)
    print(f"Необходимо подоить {name}")

  def take_milk(self):
    self.take_milk = "Молоко получено"
    print("Подоить")
  

class Sheep (Animals):
  def __init__ (self,weight, name, sound):
    Animals.__init__(self,weight, name, sound)
    print(f"Нужно подстричь {name}")

  def shear(self):
    self.shear = "Постричь"  
   
class Chik (Guse, Animals):
  pass

class Goat (Cow, Animals): 
  pass

#  def get_name(self):
#    return self.name

class Duck (Guse, Animals):
  pass

cow_manka = Cow(250,"Манька","Муууу")
sheep1 = Sheep(50, "Барашек", "Бееее")
sheep2 = Sheep(53, "Кудрявый", "Бееее")
chik_ku_ku = Chik(5, "Ку-Ку", "Кудах")
chik_kukareku = Chik(5, "Кукареку", "Кудах")   
goat_horns = Goat(48, "Рога", "Мееее")
goat_hoofs = Goat(49, "Копыта", "Мееее")    
duck1 = Duck(8, "Кряква", "Гааа")
guse_white = Guse(8, "Белый", "Кряя")
guse_grey = Guse(6, "Серый", "Кряя")

animals=[cow_manka,sheep1,sheep2,chik_ku_ku,chik_kukareku,goat_horns,goat_hoofs,duck1,guse_white,guse_grey]

for animal in animals: 
    print(f'{animal.name} {animal.eating}')
    animal.fed()
    print(f'{animal.name} {animal.eating}')
    print(f'Когда он сытый, он говорит "{animal.sound}"')


#cow_manka.take_milk()
    #print(f"{cow_manka.take_milk} y {cow_manka.name})


birds= [guse_grey,guse_white,chik_ku_ku,chik_kukareku,duck1]
for bird in birds:
  aa=bird.name
  bird.take_eggs()
  print(f'{bird.take_eggs} y {aa}')

print(f"\n Общий вес животных: {cow_manka.weight+sheep1.weight+sheep2.weight+chik_ku_ku.weight+chik_kukareku.weight+goat_hoofs.weight+goat_horns.weight+duck1.weight+guse_grey.weight+guse_white.weight} кг" )


max_weight = 0
for animal in animals:
  if animal.weight > max_weight:
    max_weight = animal.weight
print(f'максимальный вес - {max_weight} кг') 

