import maya.cmds as cmds
import maya.mel as mel
import os
import os.path
import json

def MelStringFunction(inVar_string, melVar_string):
	mel.eval('string %s = `python "inVar_string"`;'%melVar_string)
	mel.eval('print %s' %melVar_string)

def MelFloatFunction(inVar_float, melVar_float):
	print inVar
	mel.eval('float %s = `python inVar_float`;' %melVar_float)
	mel.eval('print %s' %melVar_float)

def GetFiles(currentProj, *args):
	return (cmds.fileDialog2(dir = currentProj + '\scenes', ds = 2, okc = "Add", cc = "Done"))
	
def NewFilePath_01(inFile):
	#fileName = cmds.file(q = True, sn = True)
	fileName = inFile
	rootDir = fileName.split("scenes")[0]
	endDir = fileName.split("scenes")[1]
	pathChop = endDir.split("/")
	newFile = rootDir + "assets/" + pathChop [1] + "/" + pathChop[2] + "s/" + pathChop[3] + "/"
	allSubDir = [x[0] for x in os.walk(newFile)]
	for i in range (len(allSubDir)):
		if i == (len(allSubDir)-1):
			numFolder = int(allSubDir[i][-2:])
			testPath = allSubDir[i][:-2] + "%02i" %(numFolder + 1)
			if not os.path.isdir(testPath):
				os.makedirs(testPath)
			return testPath + "/tpx_" + pathChop[1] + "_" + pathChop[3] + "_anim.fbx"

def NewFilePath_02(inFile):
	oldFile = inFile.split("/")[-1]
	newPath = ""
	for each in inFile.split("/")[:-1]:
		newPath += each + "/"
	newPath += oldFile.split('_')[1] + '@' + oldFile.split('_')[2] + '.fbx'
	return newPath
	
def GetSelectionForBake_Joints():
	selectionList = []
	allCtrlShapes = cmds.ls(type = "joint")
	for i in range(len(allCtrlShapes)):
		selectionList.append(cmds.listRelatives(allCtrlShapes[i], parent = True)[0])
	return selectionList
	
def GetSelectionForBake_Ctrls():
	selectionList = []
	allCtrlShapes = cmds.ls(type = "nurbsCurve")
	for i in range(len(allCtrlShapes)):
		selectionList.append(cmds.listRelatives(allCtrlShapes[i], parent = True)[0])
	return selectionList

def GetStartFrame(sel):
	cmds.select(sel)
	return cmds.findKeyframe( which = "first" )
	
def GetEndFrame(sel):
	cmds.select(sel)
	return cmds.findKeyframe( which = "last" )
	
def BakeAnimation(sel,startFrame, endFrame):
	cmds.bakeSimulation( sel, t = (startFrame, endFrame), at = ["tx","ty","tz","rx","ry","rz","sx","sy","sz"], hi = "none")
	
def GetExportSelection():
	allAssemblies = cmds.ls(assemblies = True)
	exportSel = []
	for thing in allAssemblies:
		if "_grp" in thing:
			exportSel.append(thing)
	return exportSel
	
def ImportReferencedRigs():
	allFiles = cmds.file(q = True, l = True)
	for ref in allFiles:
		if '_rig.' in ref:
			cmds.file(ref, importReference = True)
			
def RemoveAllNamespaces():
	nSpaces = []
	topLevel_objs = cmds.ls(assemblies = True)
	for topLevel_obj in topLevel_objs:
		if ':' in topLevel_obj:
			nSpaces.append(topLevel_obj.split(':')[0])
	for nSpace in nSpaces:
		cmds.namespace(mv = (nSpace, ':'), f = True)
		cmds.namespace(rm = nSpace)
		
def WriteDurationInfo(animName, startFrame, endFrame, startFrame_all, endFrame_all):
	print("I don't do anything, yet.") 
	print("Soon.")
	
def ReorganizeCharacterHierarchy():
	cmds.parent('joints_grp', 'global1Offset_grp')
	cmds.delete('global1_ctl')
	#cmds.delete('model_grp')
	
def ReorganizePropHierarchy(propName):
	allAssemblies = cmds.ls(assemblies = True)
	for each in allAssemblies:
		if propName in each:
			propObj = each
	propObjChildren = cmds.listRelatives(propObj, children = True)
	for every in propObjChildren:
		if '_ctrl' in every:
			cmds.delete(every)
		'''
		if '_geo_' in every:
			cmds.delete(every)
		'''
	
def GetFbxForImport(inFile):
	#not sure what this should do...
	return inFile
	
def GetAtomFileName(inFile):
	rootDir = inFile.split('assets')[0]
	oldFileName = inFile.split('/')[-1]
	atomFile = rootDir + 'data/'
	#add "anim/"
	if not os.path.isdir(atomFile + 'anim/'):
		os.makedirs(atomFile + 'anim/')
	atomFile += 'anim/'
	#add "pug/"
	if not os.path.isdir(atomFile + oldFileName.split('_')[1] + '/'):
		os.makedirs(atomFile + oldFileName.split('_')[1] + '/')
	atomFile += oldFileName.split('_')[1] + '/'
	#add "run/" or "walk/"
	if not os.path.isdir(atomFile + oldFileName.split('_')[2] + '/'):
		os.makedirs(atomFile + oldFileName.split('_')[2] + '/')
	atomFile += oldFileName.split('_')[2] + '/'
	#determine number
	newFileNum = 001
	allFilesInDir = os.listdir(atomFile)
	newFileNum += len(allFilesInDir)
	#file name
	atomFile += "%s_%s_%03i.atom" %(oldFileName.split('_')[1], oldFileName.split('_')[2], newFileNum)
	return atomFile
	
def ExportAtom(fileName):
	cmds.file(fileName, exportAnim = True, type = "atomExport", prompt = False)
	
def ImportAtom(fileName, sourceStart, sourceEnd, duration_start, duration_end):
	cmds.file(fileName, i = True, type = "atomImport", options = ";;targetTime=1;srcTime=%i:%i;dstTime=%i:%i;option=scaleInsert;match=string;;selected=selectedOnly;search=;replace=;prefix=;suffix=;"%(sourceStart, sourceEnd, duration_start, duration_end))

def NewFilePath_03(inFile, allTogether_string):
	directory = inFile.split('anims')[0] + 'anims/%s/' %allTogether_string
	oldFileName = inFile.split('/')[-1]
	allSubDir = [x[0] for x in os.walk(directory)]
	for i in range (len(allSubDir)):
		if i == (len(allSubDir)-1):
			numFolder = int(allSubDir[i][-2:])
			testPath = allSubDir[i][:-2] + "%02i" %(numFolder + 1)
			if not os.path.isdir(testPath):
				os.makedirs(testPath)
	return '%s/%s@%s.fbx' %(testPath, oldFileName.split('@')[0], allTogether_string)
	
def LoadJson(data, filePath):
	with open(filePath) as data_file:    
		data = json.load(data_file)
	
def SaveJson(data, filePath):
	toBeSaved = json.dumps(data, sort_keys = True, indent = 4, ensure_ascii = False)
	f = open(filePath, 'w')
	f.write(toBeSaved)
	f.close()

def FormatDataJson(animName, animStart, animEnd, pasteStart, pasteEnd):
	subKeys = ['name','length','final_location']
	endDict = {}
	for i in range(len(animName)):
		newDict = {}
		newDict[subKeys[0]] = animName[i].split('@')[1][:-4]
		newDict[subKeys[1]] = [animStart[i], animEnd[i]]
		newDict[subKeys[2]] = [pasteStart[i], pasteEnd[i]]
		endDict[(i+1)] = newDict	
	return endDict
		
		
		