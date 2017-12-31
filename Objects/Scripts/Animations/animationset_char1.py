import bge
import random
from Objects.Scripts.Animations import animationControl
owner = bge.logic.getCurrentController().owner
animationControl.setAnimationState(owner.name, 0, 1)

def leanforwards():
	animationControl.snapJointRotate(owner.name,"spine1","spine2","x",10)
	animationControl.snapJointRotate(owner.name,"spine3","head","x",-10)

def spinestraight():
	animationControl.snapJointRotate(owner.name,"spine1","spine2","x",0)
	animationControl.snapJointRotate(owner.name,"spine3","head","x",0)

def leftarmbend():
	animationControl.snapJointRotate(owner.name,"lowerarmleft","upperarmleft","z",-80)
	animationControl.snapJointRotate(owner.name,"upperarmleft","spine3","z",-50)
	animationControl.snapJointRotate(owner.name,"upperarmleft","spine3","y",80)

def rightarmbend():
	animationControl.snapJointRotate(owner.name,"lowerarmright","upperarmright","z",80)
	animationControl.snapJointRotate(owner.name,"upperarmright","spine3","z",-50)
	animationControl.snapJointRotate(owner.name,"upperarmright","spine3","y",-80)


def leftarmstraight():
	animationControl.snapJointRotate(owner.name,"lowerarmleft","upperarmleft","z",0)
	animationControl.snapJointRotate(owner.name,"upperarmleft","spine3","z",0)
	animationControl.snapJointRotate(owner.name,"upperarmleft","spine3","y",80)

def rightarmstraight():
	animationControl.snapJointRotate(owner.name,"lowerarmright","upperarmright","z",0)
	animationControl.snapJointRotate(owner.name,"upperarmright","spine3","y",-80)
	animationControl.snapJointRotate(owner.name,"upperarmright","spine3","z",0)

def legsstraight():
	animationControl.snapJointRotate(owner.name,"spine1","spine2","y",0)
	animationControl.snapJointRotate(owner.name,"thighleft","spine1","x",0)
	animationControl.snapJointRotate(owner.name,"calfleft","thighleft","x",0)
	animationControl.snapJointRotate(owner.name,"thighright","spine1","x",0)
	animationControl.snapJointRotate(owner.name,"thighright","calfright","x",0)
	animationControl.snapJointRotate(owner.name,"calfright","footright","x",0)
	animationControl.snapJointRotate(owner.name,"thighleft","spine1","y",-5)
	animationControl.snapJointRotate(owner.name,"thighright","spine1","y",5)

def legsclosestraight():
	animationControl.snapJointRotate(owner.name,"spine1","spine2","y",0)
	animationControl.snapJointRotate(owner.name,"thighleft","spine1","x",0)
	animationControl.snapJointRotate(owner.name,"calfleft","thighleft","x",0)
	animationControl.snapJointRotate(owner.name,"thighright","spine1","x",0)
	animationControl.snapJointRotate(owner.name,"thighright","calfright","x",0)
	animationControl.snapJointRotate(owner.name,"calfright","footright","x",0)
	animationControl.snapJointRotate(owner.name,"thighleft","spine1","y",10)
	animationControl.snapJointRotate(owner.name,"thighright","spine1","y",-10)

def legsarchedstraight():
	animationControl.snapJointRotate(owner.name,"spine1","spine2","y",0)
	animationControl.snapJointRotate(owner.name,"thighleft","spine1","x",0)
	animationControl.snapJointRotate(owner.name,"calfleft","thighleft","x",0)
	animationControl.snapJointRotate(owner.name,"thighright","spine1","x",0)
	animationControl.snapJointRotate(owner.name,"thighright","calfright","x",0)
	animationControl.snapJointRotate(owner.name,"calfright","footright","x",0)
	animationControl.snapJointRotate(owner.name,"thighleft","spine1","y",-30)
	animationControl.snapJointRotate(owner.name,"thighright","spine1","y",30)

def walkleft():
	animationControl.snapJointRotate(owner.name,"thighleft","spine1","x",-30)
	animationControl.snapJointRotate(owner.name,"calfleft","thighleft","x",90)
	animationControl.snapJointRotate(owner.name,"thighright","spine1","x",60)
	animationControl.snapJointRotate(owner.name,"calfright","thighright","x",0)
	animationControl.snapJointRotate(owner.name,"thighleft","spine1","y",5)
	animationControl.snapJointRotate(owner.name,"thighright","spine1","y",-30)

	#animationControl.setObjectMass(owner.name,"calfleft",5.111)
	#animationControl.setObjectMass(owner.name,"footleft",10)
	#animationControl.setObjectMass(owner.name,"calfright",70.111)
	#animationControl.setObjectMass(owner.name,"footright",100)
	animationControl.haltObject(owner.name,"footright")
	animationControl.haltObject(owner.name,"spine1")
	animationControl.haltObject(owner.name,"spine2")
	animationControl.haltObject(owner.name,"spine3")
	animationControl.haltObject(owner.name,"head")
	animationControl.applyForceToObject(owner.name,"calfright",0,-1000,0,5)
	#animationControl.applyForceToObject(owner.name,"spine1",0,-1000,0,5)
	#animationControl.applyForceToObject(owner.name,"spine2",0,-1000,0,5)
	#animationControl.applyForceToObject(owner.name,"spine3",0,-1000,0,5)
	animationControl.applyForceToObject(owner.name,"head",0,-1000,0,5)

def walkright():
	animationControl.snapJointRotate(owner.name,"thighleft","spine1","x",60)
	animationControl.snapJointRotate(owner.name,"calfleft","thighleft","x",0)
	animationControl.snapJointRotate(owner.name,"thighright","spine1","x",-30)
	animationControl.snapJointRotate(owner.name,"calfright","thighright","x",90)
	animationControl.snapJointRotate(owner.name,"thighleft","spine1","y",30)
	animationControl.snapJointRotate(owner.name,"thighright","spine1","y",-5)

	#animationControl.setObjectMass(owner.name,"calfleft",70.111)
	#animationControl.setObjectMass(owner.name,"footleft",100)
	#animationControl.setObjectMass(owner.name,"calfright",5.111)
	#animationControl.setObjectMass(owner.name,"footright",10)
	animationControl.haltObject(owner.name,"footleft")
	animationControl.haltObject(owner.name,"spine1")
	animationControl.haltObject(owner.name,"spine2")
	animationControl.haltObject(owner.name,"spine3")
	animationControl.haltObject(owner.name,"head")
	animationControl.applyForceToObject(owner.name,"calfright",0,-1000,0,5)
	#animationControl.applyForceToObject(owner.name,"spine1",0,-1000,0,5)
	#animationControl.applyForceToObject(owner.name,"spine2",0,-1000,0,5)
	#animationControl.applyForceToObject(owner.name,"spine3",0,-1000,0,5)
	animationControl.applyForceToObject(owner.name,"head",0,-1000,0,5)

def animationlayer1():
	if(animationControl.checkAnimationState(owner.name, 0, 0)):
		randomImpulseWalk = random.randint(0,8)
		if(randomImpulseWalk == 0):
			legsstraight()
			leftarmstraight()
			rightarmstraight()
		elif(randomImpulseWalk == 1):
			walkleft()
			rightarmbend()
		elif(randomImpulseWalk == 2):
			walkright()
			leftarmbend()
		elif(randomImpulseWalk == 3):
			legsarchedstraight()
		elif(randomImpulseWalk == 4):
			legsstraight()
	elif(animationControl.checkAnimationState(owner.name, 0, 1)):
		randomImpulseIdle = random.randint(0,6)
		if(randomImpulseIdle == 0):
			spinestraight()
		elif(randomImpulseIdle == 1):
			legsstraight()
		elif(randomImpulseIdle == 2):
			leftarmstraight()
		elif(randomImpulseIdle == 3):
			rightarmstraight()
		elif(randomImpulseIdle == 4):
			legsclosestraight()
		elif(randomImpulseIdle == 5):
			legsarchedstraight()
		elif(randomImpulseIdle == 6):
			leanforwards()
	elif(animationControl.checkAnimationState(owner.name, 0, -1)):
		animationControl.snapJointRotate(owner.name,"thighleft","spine1","y",30)
		animationControl.snapJointRotate(owner.name,"thighright","spine1","y",-30)

def run():
	animationlayer1()
	
