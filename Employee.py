class Employee:
	def __init__(self,name,surname):
		self.name=name
		self.surname=surname
	def __str__( self ):
		 print(" %s %s"%(self.name,  self.surname))
 
 
print("---------------------------------------")

p=Employee("Tom", "Jones")
p.__str__()
print("---------------------------------------")

class HourlyEmployee(Employee):
	def __init__(self,name,surname,initialhours,initialwage):
		Employee.__init__(self,name,surname)
		self.initialhours=initialhours
		self.initialwage=initialwage
	def paymentcalculation(self):
		return self.initialhours*self.initialwage
		
print("---------------------------------------")		
hemployee= HourlyEmployee("Katherine", "Papa",8,2)

print ("The wage of the employee is %d euros "%(hemployee.paymentcalculation()))



