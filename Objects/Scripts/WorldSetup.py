import bge
scene = bge.logic.getCurrentScene()
owner = bge.logic.getCurrentController().owner

def importAllObjects():
	gredausBlendList = bge.logic.getBlendFileList("//Objects/")
	for blendFile in gredausBlendList:
	    print("Bringing in " + blendFile + ".")
	    bge.logic.LibLoad("//Objects/" + blendFile, "Scene", load_actions=True, verbose=False, load_scripts=False, async=False)

def setupGredaus():
	importAllObjects()
	createConstraints()

def createConstraints():
    #find constraint set objects for all characters in the scene
    for possibleConstraintSet in scene.objects:
        if(str(possibleConstraintSet).find("constraintSet_") != -1):
            constraintSetName = str(possibleConstraintSet)
            owner[constraintSetName] = scene.objects[constraintSetName]
            constraintSetObject = scene.objects[constraintSetName]
            constraintSetObject["characterName"] = constraintSetName[14:]
            for possibleConstraint in scene.objects:
                if(scene.objects[str(possibleConstraint)].name.find(constraintSetObject["characterName"]+"con_") != -1):
                    constraintObjects = scene.objects[str(possibleConstraint)].name[len(constraintSetObject["characterName"]+"con_"):]
                    objectSeparatorStart = constraintObjects.find("_")
                    objectName1 = constraintObjects[:objectSeparatorStart]
                    objectName2 = constraintObjects[objectSeparatorStart + 1:]
                    object1PhysID = scene.objects[objectName1].getPhysicsId()
                    object2PhysID = scene.objects[objectName2].getPhysicsId()
                    constraintSetObject[str(possibleConstraint)] = bge.constraints.createConstraint(object1PhysID, object2PhysID, 
                                                                bge.constraints.GENERIC_6DOF_CONSTRAINT, 
                                                               scene.objects[str(possibleConstraint)].worldPosition[0] - scene.objects[objectName1].worldPosition[0], 
                                                               scene.objects[str(possibleConstraint)].worldPosition[1] - scene.objects[objectName1].worldPosition[1], 
                                                               scene.objects[str(possibleConstraint)].worldPosition[2] - scene.objects[objectName1].worldPosition[2], 
                                                               0, 0, 0, 0)
                    for constraintParam in range(0,6):
                        constraintSetObject[str(possibleConstraint)].setParam(constraintParam,0,0)
#owner["Constraint"].setParam(0, 0.0, 0.0) #X translation
#owner["Constraint"].setParam(1, 0.0, 0.0) #Y translation
#owner["Constraint"].setParam(2, 0.0, 0.0) #Z translation                     
#owner["Constraint"].setParam(3, 0, 0) #X Rotation
#owner["Constraint"].setParam(4, 0, 0) #Y Rotation
#owner["Constraint"].setParam(5, 0, 0) #Z rotation


