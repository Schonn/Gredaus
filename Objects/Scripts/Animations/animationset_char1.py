import bge
import random
from Objects.Scripts.Animations import animationControl
owner = bge.logic.getCurrentController().owner
animationControl.setAnimationState(owner.name, 0, 1)
currentFrame = 0

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
	animationControl.snapJointRotate(owner.name,"upperarmright","spine3","z",50)
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
	animationControl.snapJointRotate(owner.name,"thighleft","spine1","y",-10)
	animationControl.snapJointRotate(owner.name,"thighright","spine1","y",10)

def walkleft():
	animationControl.snapJointRotate(owner.name,"thighleft","spine1","x",-30)
	animationControl.snapJointRotate(owner.name,"thighright","spine1","x",30)
	animationControl.snapJointRotate(owner.name,"thighright","calfright","x",0)
	animationControl.snapJointRotate(owner.name,"thighleft","calfleft","x",0)

	animationControl.snapJointRotate(owner.name,"thighleft","spine1","y",5)
	animationControl.snapJointRotate(owner.name,"thighright","spine1","y",-5)

	animationControl.applyForceToObject(owner.name,"head",0,-500,0,1)
	animationControl.applyForceToObject(owner.name,"footleft",0,-1000,0,1)

	#animationControl.snapJointRotate(owner.name,"thighleft","spine1","x",-30)

	#animationControl.setObjectMass(owner.name,"calfleft",5.111)

	#animationControl.haltObject(owner.name,"head")

	#animationControl.applyForceToObject(owner.name,"head",0,-1000,0,5)

def walkright():
	animationControl.snapJointRotate(owner.name,"thighleft","spine1","x",10)
	animationControl.snapJointRotate(owner.name,"thighright","spine1","x",-30)
	animationControl.snapJointRotate(owner.name,"thighright","calfright","x",0)
	animationControl.snapJointRotate(owner.name,"thighleft","calfleft","x",0)

	animationControl.snapJointRotate(owner.name,"thighleft","spine1","y",5)
	animationControl.snapJointRotate(owner.name,"thighright","spine1","y",-5)

	animationControl.applyForceToObject(owner.name,"head",0,-500,0,1)
	animationControl.applyForceToObject(owner.name,"footright",0,-1000,0,1)

def kneeupright():
	animationControl.snapJointRotate(owner.name,"thighleft","spine1","x",10)
	animationControl.snapJointRotate(owner.name,"thighright","spine1","x",-60)

	animationControl.snapJointRotate(owner.name,"thighleft","spine1","y",0)
	animationControl.snapJointRotate(owner.name,"thighright","spine1","y",0)

	animationControl.snapJointRotate(owner.name,"thighright","calfright","x",60)
	animationControl.snapJointRotate(owner.name,"thighleft","calfleft","x",0)
	animationControl.applyForceToObject(owner.name,"head",0,-1000,0,1)
	animationControl.applyForceToObject(owner.name,"footright",0,-500,0,1)

def kneeupleft():
	animationControl.snapJointRotate(owner.name,"thighleft","spine1","x",-60)
	animationControl.snapJointRotate(owner.name,"thighright","spine1","x",10)

	animationControl.snapJointRotate(owner.name,"thighleft","spine1","y",0)
	animationControl.snapJointRotate(owner.name,"thighright","spine1","y",0)

	animationControl.snapJointRotate(owner.name,"thighleft","calfleft","x",60)
	animationControl.snapJointRotate(owner.name,"thighright","calfright","x",0)
	animationControl.applyForceToObject(owner.name,"head",0,-1000,0,1)
	animationControl.applyForceToObject(owner.name,"footright",0,-500,0,1)

def animationlayer1():
	global currentFrame
	if(animationControl.checkAnimationState(owner.name, 0, 0)):
		if(currentFrame == 0):
			legsstraight()
			leftarmstraight()
			rightarmstraight()
		elif(currentFrame == 1):
			legsstraight()
			kneeupright()
			leftarmstraight()
			rightarmstraight()
		elif(currentFrame == 2):
			walkright()
			leftarmbend()
			rightarmstraight()
		elif(currentFrame == 3):
			legsstraight()
			kneeupleft()
			leftarmstraight()
			rightarmstraight()
		else:
			walkleft()
			rightarmbend()
			leftarmstraight()
			currentFrame = 0
		currentFrame += 1
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
	
