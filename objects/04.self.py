# Podemos utilzar el método especial  __init__ (conocido como constructor)
# y el objeto actual self para hacer un creador de objetos del tipo definido con la
# palabra reservada class
# 

first_dict = {
  "name": "student",
  "position": "Fullstack Developer",
  "skills": ["Python", "Git", "HTML","CSS","Javascript"]
}

class student:
    def __init__(self,name,position,skills):
        self.name = name
        self.position = position
        self.skills = skills
    def say_name(self):
        print("mi nombre es",self.name,"mi cargo es",self.position,"mis habilidades son",self.skills)

Alice = student("Alice","Fullstack Developer",["Python", "Git", "Html","CSS","javastrip"])
Bob_el_chef = student("Bob el chef","kitchen helper",["pastry chef international and cake shop"])
Alice.say_name()
Bob_el_chef.say_name()
Abel = student("Abel","futbolista",["juego de centro miron"])
Abel.say_name()