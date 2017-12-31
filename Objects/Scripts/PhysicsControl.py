import bge
import math
scene = bge.logic.getCurrentScene()
owner = bge.logic.getCurrentController().owner

def findPhysicsObjects():
	planetMassThreshold = 10000 #how much mass must it have before it becomes
	negativeGravityTrigger = 0.111 #how much mass float triggers negative gravity on an object
	noGravityTrigger = 0.222 #how much mass float triggers no gravity on an object
	for potentialPhysicsObjectName in scene.objects:
		potentialPhysicsObject = scene.objects[str(potentialPhysicsObjectName)]
		if(potentialPhysicsObject.mass > 0 and potentialPhysicsObject.mass < planetMassThreshold):
			print("normal physics object " + potentialPhysicsObject.name)
			#use a specific float of the mass mass to trigger negative or no gravity
			triggerFloatComponent = round(math.modf(potentialPhysicsObject.mass)[0],3)
			if(triggerFloatComponent == negativeGravityTrigger):
				owner[potentialPhysicsObject.name] = -1
				print("negative physics!")
			elif(triggerFloatComponent == noGravityTrigger):
				owner[potentialPhysicsObject.name] = 0
				print("no physics!")
			else:
				owner[potentialPhysicsObject.name] = 1 #number represents how much gravity force is applied
		#if it's got a big enough mass, mark it as a planet
		if(potentialPhysicsObject.mass >= planetMassThreshold):
			print("planet physics object " + potentialPhysicsObject.name)
			#how much the gravity trajectory is divided down, higher number is less gravity
			owner["planet_" + potentialPhysicsObject.name] = 1

def forceGravityObjects():
	#look through all physics objects
	for physicsObjectName in owner.getPropertyNames():
		#if the object is not a planet
		if(physicsObjectName.find("planet_") == -1):
			physicsObject = scene.objects[physicsObjectName]
			#find the nearest planet for this object to gravitate to
			nearestPlanet = "NONE" #by default, assume no planet with an acceptance falloff of 100
			nearestPlanetDistance = 1000
			finalGravityTrajectory = "NONE"
			#look through all potential planet names stored in owner
			for potentialPlanetName in owner.getPropertyNames():
				if(potentialPlanetName.find("planet_") != -1): #if it's a planet, get it's object name
					consideredPlanet = scene.objects[potentialPlanetName[7:]]
					#get the trajectory from the object position difference
					consideredPlanetTrajectory = consideredPlanet.worldPosition - physicsObject.worldPosition
					#if the distance between the planet and the object is less than the current nearest planet, make this planet the new choice planet
					planetDistance = abs(consideredPlanetTrajectory[0]) + abs(consideredPlanetTrajectory[1]) + abs(consideredPlanetTrajectory[2])
					if(planetDistance < nearestPlanetDistance):
						finalGravityTrajectory = consideredPlanetTrajectory #this will be the new trajectory unless a better planet is found
						nearestPlanet = consideredPlanet.name
						nearestPlanetDistance = planetDistance #new record short distance, planets will now have to do better than this to be used
		#apply the force as the distance trajectory divided by the planet's gravity divider, then the object's mass added and everything multiplied by the object's gravity influence
		if(finalGravityTrajectory != "NONE"):
			physicsObject.applyForce(((finalGravityTrajectory / abs(owner[potentialPlanetName])) * physicsObject.mass) * owner[physicsObjectName]) 
		    
		    
