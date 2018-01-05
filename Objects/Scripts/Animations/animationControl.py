import bge
scene = bge.logic.getCurrentScene()

#owner["Constraint"].setParam(0, 0.0, 0.0) #X translation
#owner["Constraint"].setParam(1, 0.0, 0.0) #Y translation
#owner["Constraint"].setParam(2, 0.0, 0.0) #Z translation                     
#owner["Constraint"].setParam(3, 0, 0) #X Rotation
#owner["Constraint"].setParam(4, 0, 0) #Y Rotation
#owner["Constraint"].setParam(5, 0, 0) #Z rotation

#check if the defined frame state is the current frame state
def checkAnimationState(ownerName, animationLayer, stateNumber):
	if(scene.objects[ownerName]["animationState_Layer" + str(animationLayer)] == stateNumber):
		return True
	else:
		return False

#apply a force directly to a joint object
def applyForceToObject(ownerName,jointName,forceAmountX,forceAmountY,forceAmountZ,ticks):
	characterNameStart = ownerName.find("_AnimationManager")
	characterName = ownerName[:characterNameStart]
	jointObject = scene.objects[characterName + jointName]
	forceAmount = [forceAmountX,forceAmountY,forceAmountZ]
	for impulse in range(ticks):
		jointObject.applyForce(forceAmount,True)

#set the current frame state of the animation for the character
def setAnimationState(ownerName, animationLayer, stateNumber):
	scene.objects[ownerName]["animationState_Layer" + str(animationLayer)] = stateNumber

#increment the animation state for an animation layer of a character
def incrementAnimationState(ownerName, animationLayer):
	scene.objects[ownerName]["animationState_Layer" + str(animationLayer)] += 1

#iterate up or down the rotation of a joint to get to an angle
def tweenJointRotate(ownerName, firstJointObject,secondJointObject,axis,rotation):
	characterNameStart = ownerName.find("_AnimationManager")
	characterName = ownerName[:characterNameStart]
	jointName = getJointName(characterName,firstJointObject,secondJointObject)
	constraintSetObject = scene.objects["constraintSet_" + characterName]
	movementAmount = 0
	currentRotation = getRotation(constraintSetObject,jointName,axis)
	if(rotation / 57 > currentRotation):
		setRotationLimit(constraintSetObject,jointName,axis,currentRotation + 0.1,currentRotation + 0.1)
	elif(rotation / 57 < currentRotation):
		setRotationLimit(constraintSetObject,jointName,axis,currentRotation - 0.1,currentRotation - 0.1)

#snap a joint to a rotation
def snapJointRotate(ownerName, firstJointObject,secondJointObject,axis,rotation):
	characterNameStart = ownerName.find("_AnimationManager")
	characterName = ownerName[:characterNameStart]
	jointName = getJointName(characterName,firstJointObject,secondJointObject)
	constraintSetObject = scene.objects["constraintSet_" + characterName]
	setRotationLimit(constraintSetObject,jointName,axis,rotation / 57,rotation / 57)

#set a min and max translate along an axis for a joint
def setJointLooseTranslate(ownerName, firstJointObject,secondJointObject,axis,lowerlimit,upperlimit):
	characterNameStart = ownerName.find("_AnimationManager")
	characterName = ownerName[:characterNameStart]
	jointName = getJointName(characterName,firstJointObject,secondJointObject)
	constraintSetObject = scene.objects["constraintSet_" + characterName]
	setLocationLimit(constraintSetObject,jointName,axis,lowerlimit,upperlimit)

#set a min and max translate along an axis for a joint
def setJointLooseRotate(ownerName, firstJointObject,secondJointObject,axis,lowerlimit,upperlimit):
	characterNameStart = ownerName.find("_AnimationManager")
	characterName = ownerName[:characterNameStart]
	jointName = getJointName(characterName,firstJointObject,secondJointObject)
	constraintSetObject = scene.objects["constraintSet_" + characterName]
	setRotationLimit(constraintSetObject,jointName,axis,lowerlimit / 57,upperlimit / 57)

#set the gravity for a specific object
def setObjectMass(ownerName,jointName,newMass):
	characterNameStart = ownerName.find("_AnimationManager")
	characterName = ownerName[:characterNameStart]
	jointObject = scene.objects[characterName + jointName]
	jointObject.mass = newMass

#halt an object on the spot, good for walk cycles
def haltObject(ownerName,jointName):
	characterNameStart = ownerName.find("_AnimationManager")
	characterName = ownerName[:characterNameStart]
	jointObject = scene.objects[characterName + jointName]
	jointObject.worldLinearVelocity *= 0

#get the rotation limit of a specific axis of a joint
def getRotation(constraintSetObject,constraintName,axis):
	if(axis == "x"):
		return constraintSetObject[constraintName].getParam(3)
	elif(axis == "y"):
		return constraintSetObject[constraintName].getParam(4)
	elif(axis == "z"):
		return constraintSetObject[constraintName].getParam(5)

#set the rotation limit for a specific axis (or all) of a joint
def setRotationLimit(constraintSetObject,constraintName,axis,minimum,maximum):
	if(axis == "x"):
		constraintSetObject[constraintName].setParam(3,minimum,maximum)
	elif(axis == "y"):
		constraintSetObject[constraintName].setParam(4,minimum,maximum)
	elif(axis == "z"):
		constraintSetObject[constraintName].setParam(5,minimum,maximum)
	elif(axis == "all"):
		constraintSetObject[constraintName].setParam(3,minimum,maximum)
		constraintSetObject[constraintName].setParam(4,minimum,maximum)
		constraintSetObject[constraintName].setParam(5,minimum,maximum)
        
#set the location limit for a specific axis (or all) of a joint
def setLocationLimit(constraintSetObject,constraintName,axis,minimum,maximum):
	if(axis == "x"):
		constraintSetObject[constraintName].setParam(0,minimum,maximum)
	elif(axis == "y"):
		constraintSetObject[constraintName].setParam(1,minimum,maximum)
	elif(axis == "z"):
		constraintSetObject[constraintName].setParam(2,minimum,maximum)
	elif(axis == "all"):
		constraintSetObject[constraintName].setParam(0,minimum,maximum)
		constraintSetObject[constraintName].setParam(1,minimum,maximum)
		constraintSetObject[constraintName].setParam(2,minimum,maximum)

#return the name of a joint connecting two objects
def getJointName(characterName,firstJointObject,secondJointObject):
	concatenatedJointName = characterName + "con_" + characterName + firstJointObject + "_" + characterName + secondJointObject
	concatenatedJointNameReversed = characterName + "con_" + characterName + secondJointObject + "_" + characterName + firstJointObject
	if(concatenatedJointName in scene.objects):
		return concatenatedJointName
	elif(concatenatedJointNameReversed in scene.objects):
		return concatenatedJointNameReversed
	

#def pose1():
#    setRotationLimit("char1con_char1upperarmleft_char1spine3","y",-5,-5)
#    setRotationLimit("char1con_char1upperarmright_char1spine3","y",5,5)
#    setRotationLimit("char1con_char1lowerarmleft_char1upperarmleft","z",-90,-90)
#    setRotationLimit("char1con_char1lowerarmright_char1upperarmright","z",90,90)

#def relax():
#    for individualConstraint in owner.getPropertyNames():
#        if(individualConstraint != "characterName"):
#            owner[individualConstraint].setParam(3,-0.3,0.3)
#            owner[individualConstraint].setParam(4,-0.3,0.3)
#            owner[individualConstraint].setParam(5,-0.3,0.3)
        
#def stiffen():
#    for individualConstraint in owner.getPropertyNames():
#        if(individualConstraint != "characterName"):
#            owner[individualConstraint].setParam(3,0,0)
#            owner[individualConstraint].setParam(4,0,0)
#            owner[individualConstraint].setParam(5,0,0)

#def copyObjectRotation():
#    for constraintSet in owner.getPropertyNames():
#        for individualConstraint in scene.objects[constraintSet].getPropertyNames():
#            if(individualConstraint != "characterName"):
#                xRotation = scene.objects[individualConstraint].worldOrientation.to_euler()[0]
#                yRotation = scene.objects[individualConstraint].worldOrientation.to_euler()[1]
#                zRotation = scene.objects[individualConstraint].worldOrientation.to_euler()[2]
#                setRotationLimit(scene.objects[constraintSet],str(individualConstraint),"x",xRotation,xRotation)
#                setRotationLimit(scene.objects[constraintSet],str(individualConstraint),"y",yRotation,yRotation)
#                setRotationLimit(scene.objects[constraintSet],str(individualConstraint),"z",zRotation,zRotation)
