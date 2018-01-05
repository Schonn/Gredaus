import bge
import random
from Objects.Scripts.Animations import animationControl
owner = bge.logic.getCurrentController().owner
previousActionType = 1

def performActions():
	global previousActionType
	actionType = random.randint(0,1)
	if(actionType != previousActionType):
		if(actionType == 0): #walk
			animationControl.setAnimationState(owner.name, 0, 0)
		elif(actionType == 1): #idle
			animationControl.setAnimationState(owner.name, 0, 1)
		previousActionType = actionType

def run():
	#animationControl.setAnimationState(owner.name, 0, 0)
	performActions()
	
