#AIGLOBALHUB PYTHON COURSE - FINAL PROJECT
#TARIK AVCI - tarikaavci@gmail.com
#Company Management System

class Employee:

   def __init__(self,name,age):
      self.name = name
      self.age=age
      self.language = []

   def addlanguages(self,newlanguage):
      self.language.append(newlanguage)

   def showinfo(self):
      print("Name: ",self.name,"\n","Age: ",self.age,"\n","Languages: ",*self.language)
      
      
      
class Manager(Employee):

   pass


print("Company Management System")      
print("--------------------------")

#inputs are employee and manager

en = input("Employee name: ")
eage = input("Employee age: ")
elang = input("Employee Language(use space between languages): ")
print(list(elang.split(" ")))

mn = input("Manager name: ")
mage = input("Manager age: ")
mlang = input("Manager Language(use space between languages): ")


print(list(mlang.split(" ")))
print("\n",("\n"))
print("Employee Information")
E1 = Employee(en,eage)
E1.addlanguages(elang)
E1.showinfo()
print("---------------------------")


print("Manager Information")
M1 = Manager(mn,mage)
M1.addlanguages(mlang)
M1.showinfo()

print("---------------------------")
#we can create information of employee this way too.
E2=Employee("Tarik","24")
E2.addlanguages("english")
E2.addlanguages("turkish")
E2.showinfo()