#fbx export script.

import maya.cmds as cmds
import maya.mel as mel
import sys

functionLibrary = 'C:/Users/Wesley/Documents/maya/scripts/ww_fbx_export'

# appending the file path to the sys.path if its not already a part
if not functionLibrary in sys.path:
    sys.path.append(functionLibrary)
# if the module and it's path are already loaded, then we should delete it all
for each in sys.modules.keys():
    if 'ww_fbx_export' in each:
        del sys.modules[each]
# importing
from ww_fbx_export import *

"""
|||||||||
"""
#work work work#
"""
|||||||||
"""

#find the files we wanna work with
currentProj = cmds.workspace(q = True, fn = True)
inFiles = []
FBX_v1_list = []
FBX_v2_list = []
atomFile_list = []
animDuration_list = []
findFile = ww_fbx_export_funcLib.GetFiles(currentProj)
while (not findFile == None):
    inFiles.append(findFile[0])
    findFile = ww_fbx_export_funcLib.GetFiles(currentProj)
    
#open up file
for inFile in inFiles:
    cmds.file(inFile, o = True, f = True)
    
    #build path for fbx export 01
    newFile = ww_fbx_export_funcLib.NewFilePath_01(inFile)
    FBX_v1_list.append(newFile)
    print "With this file as input: " + inFile
    print "This would be the new file: " + newFile
    mel.eval('string $new_FileName = `python "newFile"`;')
    
    #import references
    ww_fbx_export_funcLib.ImportReferencedRigs()
    
    #remove namespaces
    ww_fbx_export_funcLib.RemoveAllNamespaces()
    
    sel_jnts = ww_fbx_export_funcLib.GetSelectionForBake_Joints()
    sel_ctrls = ww_fbx_export_funcLib.GetSelectionForBake_Ctrls()
    startFrame = ww_fbx_export_funcLib.GetStartFrame(sel_ctrls)
    endFrame = ww_fbx_export_funcLib.GetEndFrame(sel_ctrls)
    mel.eval('float $new_StartFrame = `python startFrame`;')
    mel.eval('float $new_EndFrame = `python endFrame`;')
    
    #bake simulation
    ww_fbx_export_funcLib.BakeAnimation(sel_jnts, startFrame, endFrame)
    
    #select export objects
    exportSel = ww_fbx_export_funcLib.GetExportSelection()
    cmds.select(exportSel)
    
    #setup export properties
    mel.eval('FBXExportBakeComplexAnimation -v true')
    mel.eval('FBXExportBakeComplexEnd -v $new_StartFrame')
    mel.eval('FBXExportBakeComplexStart -v $new_EndFrame')
    mel.eval('FBXExportSkins -v true')
    mel.eval('FBXExportInputConnections -v true')
    mel.eval('FBXExportInAscii -v false') #much smaller than ascii.  i should automagically build an accopmyaing txt file with clip duration info.
    
    #pull the trigger
    mel.eval('FBXExport -f $new_FileName -s')
    

# round 2 - we need to ATOM bake all this keyframe data to an ATOM file and clean up our initial FBX's and re-export them with no controls (and possibly no geo)
for fbx in FBX_v1_list:
    cmds.file(new = True, f = True)
    fbxFile = ww_fbx_export_funcLib.GetFbxForImport(fbx)
    mel.eval('string $new_inFileName = `python "fbxFile"`;')
    
    #build path for fbx export 02
    newExportFile = ww_fbx_export_funcLib.NewFilePath_02(fbx)
    FBX_v2_list.append(newExportFile)
    print "With this file as input: " + fbx
    print "This would be the new file: " + newExportFile
    mel.eval('string $new_outFileName = `python "newExportFile"`;')
    
    #setup import properties
    mel.eval('FBXImportConstraints -v true')
    mel.eval('FBXImportMode -v merge')
    mel.eval('FBXImportSkins -v true')
    
    #pull the trigger
    mel.eval('FBXImport -file $new_inFileName')
    
    #change hierarchy and remove nurbs controls
    ww_fbx_export_funcLib.ReorganizeCharacterHierarchy()
    ww_fbx_export_funcLib.ReorganizePropHierarchy('gun01')
    
    #select all joints and export ATOM animation
    sel_jnts = ww_fbx_export_funcLib.GetSelectionForBake_Joints()
    new_startFrame = ww_fbx_export_funcLib.GetStartFrame(sel_jnts)
    new_endFrame = ww_fbx_export_funcLib.GetEndFrame(sel_jnts)
    animDuration_list.append("%i-%i"%(new_startFrame, new_endFrame))
    mel.eval('float $new_new_StartFrame = `python new_startFrame`;')
    mel.eval('float $new_new_EndFrame = `python new_endFrame`;')
    
    cmds.select(sel_jnts)
    atomExportFile = ww_fbx_export_funcLib.GetAtomFileName(fbx)
    atomFile_list.append(atomExportFile)
    ww_fbx_export_funcLib.ExportAtom(atomExportFile)
    
    #select export objects
    exportSel = ww_fbx_export_funcLib.GetExportSelection()
    cmds.select(exportSel)
    
    #setup export properties
    mel.eval('FBXExportBakeComplexAnimation -v true')
    mel.eval('FBXExportBakeComplexEnd -v $new_new_StartFrame')
    mel.eval('FBXExportBakeComplexStart -v $new_new_EndFrame')
    mel.eval('FBXExportSkins -v true')
    mel.eval('FBXExportInputConnections -v true')
    mel.eval('FBXExportInAscii -v false')
    
    #pull the trigger
    mel.eval('FBXExport -f $new_outFileName -s')
    
# home stretch - make the alltogether fbx with every fbx we included in this operation
# also output the duration and clip info to some arbitrary yaml document.

# new File with no animations
cmds.file(new = True, f = True)
fbxFile = ww_fbx_export_funcLib.GetFbxForImport(FBX_v2_list[0])
mel.eval('string $final_inFileName = `python "fbxFile"`;')

#setup import properties
mel.eval('FBXImportConstraints -v true')
mel.eval('FBXImportMode -v merge')
mel.eval('FBXImportSkins -v true')

#pull the trigger
mel.eval('FBXImport -file $final_inFileName')

#remove all keys
cmds.currentTime(1, edit = True)
allKeys = cmds.ls(type = 'animCurve')
for key in allKeys:
    cmds.delete(key)
    
timeOffset = 1

#lists to contain json data
json_animName_list = []
json_animDurationS_list = []
json_animDurationE_list = []
json_animPasteTimeS_list = []
json_animPasteTimeE_list = []

for i in range(len(FBX_v2_list)):
    #find duration and then import this animation
    sourceStart = int(animDuration_list[i].split("-")[0])
    sourceEnd = int(animDuration_list[i].split("-")[1])
    duration_start = timeOffset
    duration_end = timeOffset + sourceEnd
    
    print""
    print"We are working with: " + FBX_v2_list[i]
    print"Associated ATOM file: " + atomFile_list[i]
    print"sourceStart = %i" %sourceStart
    print"sourceEnd = %i" %sourceEnd
    print"duration_start = %i" %duration_start
    print"duration_end = %i" %duration_end
    print""
    
    #save to json data list
    json_animName_list.append(FBX_v2_list[i])
    json_animDurationS_list.append(sourceStart)
    json_animDurationE_list.append(sourceEnd)
    json_animPasteTimeS_list.append(duration_start)
    json_animPasteTimeE_list.append(duration_end)
    
    #import animation and update timeOffset
    sel_jnts = ww_fbx_export_funcLib.GetSelectionForBake_Joints()
    cmds.select(sel_jnts)
    ww_fbx_export_funcLib.ImportAtom(atomFile_list[i], sourceStart, sourceEnd, duration_start, duration_end)
    timeOffset += sourceEnd
    
#create FBX filepath and selSet for export
finalFbxFilename = ww_fbx_export_funcLib.NewFilePath_03(FBX_v2_list[0], 'allTogether')
mel.eval('string $final_outFileName = `python "finalFbxFilename"`;')
mel.eval('float $final_animStart = `python duration_start`;')
mel.eval('float $final_animEnd = `python duration_end`;')

finalFbxExportSel = []
allAssemblies = cmds.ls(assemblies = True)
for each in allAssemblies:
    if '_grp' in each:
        finalFbxExportSel.append(each)

#clean data for json export, define file name, and export json file
json_data = ww_fbx_export_funcLib.FormatDataJson(json_animName_list, json_animDurationS_list, json_animDurationE_list, json_animPasteTimeS_list, json_animPasteTimeE_list)
json_fileName = '%s.txt' %finalFbxFilename.split('.fbx')[0].replace('@','_')
ww_fbx_export_funcLib.SaveJson(json_data, json_fileName)

#export final FBX file
cmds.select(cl = True)
for each in finalFbxExportSel:
    cmds.select(each, add = True)
    
#declare export settings fbx
mel.eval('FBXExportBakeComplexAnimation -v true')
mel.eval('FBXExportBakeComplexEnd -v $final_animStart')
mel.eval('FBXExportBakeComplexStart -v $final_animEnd')
mel.eval('FBXExportSkins -v true')
mel.eval('FBXExportInputConnections -v true')
mel.eval('FBXExportInAscii -v false')

#pull the trigger
mel.eval('FBXExport -f $final_outFileName -s')