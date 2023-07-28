#Compute gravitational force between two objects.

mass1 = float(input("m1: "))
mass2 = float(input("m2: "))
 
r = float(input("distance: "))
 
G = 6.673*(10**-11)
force =(G*mass1*mass2)/(r**2)
 
print("The gravitational force is:", round(force, 5),"N")