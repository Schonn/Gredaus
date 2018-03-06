import bge
import math
scene = bge.logic.getCurrentScene()
owner = bge.logic.getCurrentController().owner

#def removeConstraintHitScanObject():
#	if(playerCamera["pickConstraint"] != None):
#		bge.constraints.removeConstraint(playerCamera["pickConstraint"].getConstraintId())
#		playerCamera["pickConstraint"] = None
#
#def constrainHitScanObject(hitObject):
#	removeConstraintHitScanObject()
#	playerCamera["pickConstraint"] = bge.constraints.createConstraint(scene.objects["playerCameraPhysics"].getPhysicsId(), hitObject.getPhysicsId(), 
#					bge.constraints.GENERIC_6DOF_CONSTRAINT, 
#                                	scene.objects["playerCameraPhysics"].worldPosition[0], 
#                                	scene.objects["playerCameraPhysics"].worldPosition[1], 
#                                	scene.objects["playerCameraPhysics"].worldPosition[2], 
#                                	0, 0, 0, 0)
#	for constraintParameter in range(0,6):
#		playerCamera["pickConstraint"].setParam(constraintParameter,0,0)
#	previousHitObject = hitObject

def mouseMoveObject():
	if("currentHitObject" in scene.active_camera):
		if(scene.active_camera["currentHitObject"] != None):
			forceTrajectory = scene.objects["playerCameraPhysics"].worldPosition - scene.active_camera["currentHitObject"].worldPosition
			if(scene.active_camera["currentHitObject"].mass < 10000):
				scene.active_camera["currentHitObject"].worldLinearVelocity *= 0
				scene.active_camera["currentHitObject"].applyForce(forceTrajectory * scene.active_camera["currentHitObject"].mass * 1000)
			else:
				scene.active_camera["currentHitObject"].worldLinearVelocity *= 0.5
				scene.active_camera["currentHitObject"].applyForce(forceTrajectory * scene.active_camera["currentHitObject"].mass * 10)
				

def mouseMoveObjectHitScan():
	scene.active_camera["currentHitObject"] = scene.active_camera.getScreenRay(0.5, 0.5, 10000)
	print(scene.active_camera["currentHitObject"])

def mouseMoveObjectClear():
	scene.active_camera["currentHitObject"] = None
	
#	hitObject = playerCamera.getScreenRay(0.5, 0.5, 10000)
#	print(hitObject)
#	if(hitObject == None):
#		removeConstraintHitScanObject()
#	else:
#		if("pickConstraint" not in playerCamera):
#			playerCamera["pickConstraint"] = None
#		else:
#			constrainHitScanObject(hitObject)
	
				
	
