#AIGLOBALHUB PYTHON COURSE - DAY-5 HW-4
#TARIK AVCI - tarikaavci@gmail.com

class Animals:

   def __init__(self,name,leg,age):
      self.name = name
      self.leg = leg
      self.age=age
   def printname(self):
      print("The animal is",self.name,"and it has" , self.leg,"legs","and it's",self.age,"years old.")
      
class Cats:

   def __init__(self, name, type):
      self.name = name
      self.type = type
   def printnamecat(self):
      print("The cat is",self.name,"and its a ",self.type," cat.")

class Dogs:
      def __init__(self, name, type):
         self.name = name
         self.type = type
      def printnamedog(self):
         print("The dog is",self.name,"and its a ",self.type," dog.")


x = Animals("Tiger",4,4)
x.printname()
print("*****************************")
y = Cats("Boncuk","British")
y.printnamecat()
print("*****************************")
y = Dogs("Torres","Pitbull")
y.printnamedog()