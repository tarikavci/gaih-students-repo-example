#AIGLOBALHUB PYTHON COURSE - FINAL PROJECT
#TARIK AVCI - tarikaavci@gmail.com
#Company Management System

class Employees():

    def __init__(self,name,age,language):
      self.name = name
      self.age=age
      self.language = language

    def languages(self):
      for lang in self.language:
          print(lang)
  
class Manager(Employees):

   pass



dict_emp = {"em1": Employees("Tarık", 24, ("Turkish", "English")),
            "em2": Employees("Tayfun", 41, ("Turkish", "English",)),
            "em3": Employees("Ümran", 32, ("Turkish", "English", "German"))}

dict_man ={ "man1": Manager("Joe", 61, ("Turkish", "Spanish", "English")),
            "man2": Manager("Donald", 40, ("Turkish", "Spanish", "French", "English","Arabic")),
            "man3": Manager("Vladimir", 38, ("Spanish", "English","Dutch","Russian"))}

set1 = set()  #set for employees
set2= set()   #set for manager


def Employees_Languages():
    
    print("\nEmployees can speaks :")
    print("----------------------------")

   
    for i in dict_emp:
        if True:
            for language in dict_emp[i].language:
                set1.add(language)
   
    for language in set1:
        print(language)
    
def Manager_Languages():
    
    print("\nManagers can speaks :")
    print("----------------------------")

   
    for i in dict_man:
        if True:
            for language in dict_man[i].language:
                set2.add(language)
               
    for language in set2:
        print(language)    



print("-------------------------")
print("Company Management System")      
print("-------------------------")

Employees_Languages()
Manager_Languages()



#Thanks for the course.
