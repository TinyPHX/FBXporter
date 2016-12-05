file -f -new;
optionVar -sv colorManagementColorPickerColorSpaceSelection "Rendering Space";
optionVar -iv colorManagementColorPickerColorMgtEnabled 1;
// Warning: file: F:/Autodesk/Maya2016/scripts/startup/rememberViewportSettings.mel line 43: Active stereo does not work with Aero enabled. Active stereo has been disabled. // 
optionVar -sv colorManagementColorPickerColorSpaceSelection "Rendering Space";
optionVar -iv colorManagementColorPickerColorMgtEnabled 1;
// untitled // 
commandPort -securityWarning -name commandportDefault;
// AbcBullet v1.0 using Alembic 1.5.4 (built May  8 2014 13:47:10)
// cgfxShader 4.5 for Maya 2016.1 (Mar 18 2016)
// AbcExport v1.0 using Alembic 1.5.4 (built May  8 2014 13:47:10)
// AbcImport v1.0 using Alembic 1.5.4 (built May  8 2014 13:47:10)
file -f -options "v=0;"  -ignoreVersion  -typ "mayaAscii" -o "F:/maya/projects/TESTING/scenes/stretchy_joints_testing/02/stretchyJoints_midPointSnapping_test_003.ma";addRecentFile("F:/maya/projects/TESTING/scenes/stretchy_joints_testing/02/stretchyJoints_midPointSnapping_test_003.ma", "mayaAscii");
closeAllNodeEditors;
closeHypershade;
updateRenderOverride;
updateRendererUI;
+++++++ Turtle for Maya registered successfully ++++++
optionVar -sv colorManagementColorPickerColorSpaceSelection "Rendering Space";
optionVar -iv colorManagementColorPickerColorMgtEnabled 1;
// Warning: line 2000: The default image may not be modified. Use the -i/image flag instead. // 
// File read in  1.7 seconds.
optionVar -sv colorManagementColorPickerColorSpaceSelection "Rendering Space";
optionVar -iv colorManagementColorPickerColorMgtEnabled 1;
updateRendererUI;
select -r ikChain_scale_cond ;
select -r multiplyDivide1 ;
select -r ikChain_scale_cond ;
select -r blendTwoAttr2 ;
select -cl  ;
// Undo: select -cl  
// Undo: rename "blendTwoAttr2" "lowArm_choice_b2a"
// Undo: select -r blendTwoAttr2 
// Undo: nodeEdKeyPressCommand "nodeEditorPanel1NodeEditorEd" "Del"
select -r blendTwoAttr2 ;
select -cl  ;
disconnectAttr ikChain_scale_cond.outColorR blendTwoAttr2.input[0];
// Disconnect ikChain_scale_cond.outColor.outColorR from blendTwoAttr2.input. // 
disconnectAttr ikChain_scale_cond.outColorR upArm_choice_b2a.input[0];
// Disconnect ikChain_scale_cond.outColor.outColorR from upArm_choice_b2a.input. // 
// Undo: nodeEdKeyPressCommand "nodeEditorPanel1NodeEditorEd" "Del"
select -r blendTwoAttr2 ;
select -r ikChain_scale_cond ;
select -r shouldJnt_to_wrsitCtrl_distShape ;
select -r shouldJnt_to_wrsitCtrl_should_distLoc ;
select -r shouldJnt_to_wrsitCtrl_should_distLoc elbow_ctrl wrist_ctrl ;
select -cl  ;
select -r shouldJnt_to_elbowCtrl_should_distLoc ;
select -r shoulder_jnt.rotatePivot ;
select -add wrist_jnt.rotatePivot ;
ikHandle -sol ikRPsolver;
// ikHandle1 effector1 // 
select -cl  ;
spaceLocator;
// locator1 // 
select -r ikHandle1 ;
select -r locator1 ;
setAttr "locatorShape1.localScaleX" 0.1;
setAttr "locatorShape1.localScaleY" 0.1;
setAttr "locatorShape1.localScaleZ" 0.1;
setAttr "locatorShape1.localScaleX" 0.3;
setAttr "locatorShape1.localScaleY" 0.3;
setAttr "locatorShape1.localScaleZ" 0.3;
select -cl  ;
select -r locator1 ;
move -r -0.0333323 0.0130389 0.0100824 ;
select -add locator1 ;
// Undo: select -add locator1 
setAttr "locator1.translateZ" 0;
setAttr "locator1.translateX" 0;
setAttr "locator1.translateY" 0;
select -cl  ;
select -r locator1 ;
move -r 0 0 -1.379211 ;
select -r wrist_jnt ;
select -r elbow_jnt ;
setAttr "elbow_jnt.rotateY" 0;
select -r shoulder_jnt ;
setAttr "shoulder_jnt.rotateY" 0;
select -cl  ;
select -r ikHandle1 ;
doDelete;
select -r elbow_jnt ;
select -r shoulder_jnt ;
select -r wrist_jnt ;
select -cl  ;
select -r shoulder_jnt.rotatePivot ;
select -add wrist_jnt.rotatePivot ;
ikHandle -sol ikRPsolver;
// ikHandle1 effector1 // 
select -r ikHandle1 ;
rename "ikHandle1" "test_ikh";
// test_ikh // 
select -r locator1 ;
select -r locator1 ;
select -r locator1 ;
rename "locator1" "elbow_ctrl";
// elbow_ctrl // 
select -r test_ikh ;
select -r elbow_ctrl ;
select -r elbow_ctrl ;
select -r test_ikh ;
select -r elbow_ctrl ;
spaceLocator;
// locator1 // 
select -r locator1 ;
rename "locator1" "wrist_ctrl";
// wrist_ctrl // 
select -r test_ikh ;
select -r wrist_ctrl ;
setAttr "wrist_ctrlShape.localScaleX" 0.3;
setAttr "wrist_ctrlShape.localScaleY" 0.3;
setAttr "wrist_ctrlShape.localScaleZ" 0.3;
select -cl  ;
select -r wrist_ctrl ;
move -r 1.278216 0 0 ;
move -r 0.0318506 0.00800387 0.0122127 ;
move -rpr 1.312 0 0 ;
select -cl  ;
select -r wrist_ctrl ;
move -rpr 1.319078 0 0 ;
dR_paintPress;
selectPref -paintSelectRefine 1 -paintSelect 1;
dR_paintRelease;
selectPref -paintSelectRefine 0 -paintSelect 0;
dR_paintPress;
selectPref -paintSelectRefine 1 -paintSelect 1;
dR_paintRelease;
selectPref -paintSelectRefine 0 -paintSelect 0;
dR_paintPress;
selectPref -paintSelectRefine 1 -paintSelect 1;
dR_paintRelease;
selectPref -paintSelectRefine 0 -paintSelect 0;
dR_paintPress;
selectPref -paintSelectRefine 1 -paintSelect 1;
dR_paintRelease;
selectPref -paintSelectRefine 0 -paintSelect 0;
select -cl  ;
select -r test_ikh wrist_ctrl ;
select -r test_ikh ;
parent test_ikh wrist_ctrl ;
// test_ikh // 
select -r test_ikh ;
setAttr "test_ikh.visibility" 0;
select -cl  ;
select -r elbow_ctrl ;
select -add test_ikh ;
poleVectorConstraint -weight 1;
// test_ikh_poleVectorConstraint1 // 
select -cl  ;
select -r elbow_ctrl ;
move -r -0.0453288 0 0.0189613 ;
// Undo: move -r -0.0453288 0 0.0189613 
move -r 0 0.101581 0 ;
// Undo: move -r 0 0.101581 0 
select -d elbow_ctrl ;
distanceDimension -sp -0.458083 0 1.159132 -ep 0.540239 0 0.891142 ;
// distanceDimension1 distanceDimensionShape1 // 
distanceDimension -sp -2.471741 0 -1.036183 -ep -1.28597 0 -1.493015 ;
// distanceDimension2 distanceDimensionShape2 // 
distanceDimension -sp 1.060634 0 -1.394441 -ep 1.84872 0 -0.713077 ;
// distanceDimension3 distanceDimensionShape3 // 
select -r locator1 ;
select -r locator1 ;
rename "locator1" "shouldJnt_to_wristCtrl_should_distLoc";
// shouldJnt_to_wristCtrl_should_distLoc // 
select -r shouldJnt_to_wristCtrl_should_distLoc ;
select -r locator2 ;
rename "locator2" "shouldJnt_to_wristCtrl_wrist_distLoc";
// shouldJnt_to_wristCtrl_wrist_distLoc // 
select -r shouldJnt_to_wristCtrl_wrist_distLoc ;
select -r distanceDimension1 ;
rename "distanceDimension1" "shouldJnt_to_wristCtrl_dist";
// shouldJnt_to_wristCtrl_dist // 
select -r locator3 ;
rename "locator3" "shouldJnt_to_elbowCtrl_should_distLoc";
// shouldJnt_to_elbowCtrl_should_distLoc // 
select -r shouldJnt_to_elbowCtrl_should_distLoc ;
select -r locator4 ;
rename "locator4" "shouldJnt_to_elbowCtrl_elbow_distLoc";
// shouldJnt_to_elbowCtrl_elbow_distLoc // 
select -r distanceDimension2 ;
rename "distanceDimension2" "shouldJnt_to_elbowCtrl_dist";
// shouldJnt_to_elbowCtrl_dist // 
select -r locator5 ;
rename "locator5" "elbowCtrl_to_wristCtrl_elbow_distLoc";
// elbowCtrl_to_wristCtrl_elbow_distLoc // 
select -r elbowCtrl_to_wristCtrl_elbow_distLoc ;
select -r elbowCtrl_to_wristCtrl_elbow_distLoc ;
select -r elbowCtrl_to_wristCtrl_elbow_distLoc ;
select -r locator6 ;
rename "locator6" "elbowCtrl_to_wristCtrl_wrist_distLoc";
// elbowCtrl_to_wristCtrl_wrist_distLoc // 
select -r distanceDimension3 ;
rename "distanceDimension3" "elbowCtrl_to_wristCtrl_dist";
// elbowCtrl_to_wristCtrl_dist // 
select -r shouldJnt_to_wristCtrl_should_distLoc ;
SnapToPoint; dR_enterForSnap;
SnapToPoint; dR_enterForSnap;
SnapToPoint; dR_enterForSnap;
move -rpr -1.5 0 0 ;
SnapToPoint; dR_enterForSnap;
select -r shouldJnt_to_wristCtrl_wrist_distLoc ;
move -rpr 1.319078 0 0 ;
SnapToPoint; dR_enterForSnap;
select -r shouldJnt_to_elbowCtrl_should_distLoc ;
move -rpr -1.5 0 0 ;
SnapToPoint; dR_enterForSnap;
select -r shouldJnt_to_elbowCtrl_elbow_distLoc ;
move -rpr 0 0 -1.379211 ;
SnapToPoint; dR_enterForSnap;
select -r elbowCtrl_to_wristCtrl_elbow_distLoc ;
move -rpr 0 0 -1.379211 ;
SnapToPoint; dR_enterForSnap;
select -r elbowCtrl_to_wristCtrl_wrist_distLoc ;
move -rpr 1.319078 0 0 ;
SnapToPoint; dR_enterForSnap;
select -cl  ;
select -r shouldJnt_to_elbowCtrl_elbow_distLoc ;
select -add elbowCtrl_to_wristCtrl_elbow_distLoc ;
parent shouldJnt_to_elbowCtrl_elbow_distLoc elbow_ctrl ;
// shouldJnt_to_elbowCtrl_elbow_distLoc // 
parent elbowCtrl_to_wristCtrl_elbow_distLoc elbow_ctrl ;
// elbowCtrl_to_wristCtrl_elbow_distLoc // 
select -r shouldJnt_to_elbowCtrl_elbow_distLoc elbowCtrl_to_wristCtrl_elbow_distLoc ;
select -r shouldJnt_to_elbowCtrl_elbow_distLoc ;
select -r shouldJnt_to_elbowCtrl_elbow_distLoc elbowCtrl_to_wristCtrl_elbow_distLoc ;
select -r shouldJnt_to_elbowCtrl_elbow_distLoc ;
setAttr "shouldJnt_to_elbowCtrl_elbow_distLocShape.localScaleX" 0.1;
setAttr "shouldJnt_to_elbowCtrl_elbow_distLocShape.localScaleY" 0.1;
setAttr "shouldJnt_to_elbowCtrl_elbow_distLocShape.localScaleZ" 0.1;
select -r elbowCtrl_to_wristCtrl_elbow_distLoc ;
setAttr "elbowCtrl_to_wristCtrl_elbow_distLocShape.localScaleX" 0.1;
setAttr "elbowCtrl_to_wristCtrl_elbow_distLocShape.localScaleY" 0.1;
setAttr "elbowCtrl_to_wristCtrl_elbow_distLocShape.localScaleZ" 0.1;
select -cl  ;
select -r elbow_ctrl ;
move -r 0 0.17153 -0.0819487 ;
// Undo: move -r 0 0.17153 -0.0819487 
select -r shouldJnt_to_wristCtrl_wrist_distLoc elbowCtrl_to_wristCtrl_wrist_distLoc ;
move -r 0.200869 0 -0.298432 ;
// Undo: move -r 0.200869 0 -0.298432 
parent shouldJnt_to_wristCtrl_wrist_distLoc wrist_ctrl ;
// shouldJnt_to_wristCtrl_wrist_distLoc // 
parent elbowCtrl_to_wristCtrl_wrist_distLoc wrist_ctrl ;
// elbowCtrl_to_wristCtrl_wrist_distLoc // 
select -r shouldJnt_to_wristCtrl_wrist_distLoc ;
setAttr "shouldJnt_to_wristCtrl_wrist_distLocShape.localScaleX" 0.1;
setAttr "shouldJnt_to_wristCtrl_wrist_distLocShape.localScaleY" 0.1;
setAttr "shouldJnt_to_wristCtrl_wrist_distLocShape.localScaleZ" 0.1;
select -r elbowCtrl_to_wristCtrl_wrist_distLoc ;
setAttr "elbowCtrl_to_wristCtrl_wrist_distLocShape.localScaleX" 0.1;
setAttr "elbowCtrl_to_wristCtrl_wrist_distLocShape.localScaleY" 0.1;
setAttr "elbowCtrl_to_wristCtrl_wrist_distLocShape.localScaleZ" 0.1;
select -r shouldJnt_to_wristCtrl_should_distLoc ;
setAttr "shouldJnt_to_wristCtrl_should_distLocShape.localScaleX" 0.1;
setAttr "shouldJnt_to_wristCtrl_should_distLocShape.localScaleY" 0.1;
setAttr "shouldJnt_to_wristCtrl_should_distLocShape.localScaleZ" 0.1;
select -r shouldJnt_to_elbowCtrl_should_distLoc ;
setAttr "shouldJnt_to_elbowCtrl_should_distLocShape.localScaleX" 0.1;
setAttr "shouldJnt_to_elbowCtrl_should_distLocShape.localScaleY" 0.1;
setAttr "shouldJnt_to_elbowCtrl_should_distLocShape.localScaleZ" 0.1;
spaceLocator;
// locator1 // 
select -r locator1 ;
rename "locator1" "shoulder_ctrl";
// shoulder_ctrl // 
setAttr "shoulder_ctrlShape.localScaleX" 0.3;
setAttr "shoulder_ctrlShape.localScaleY" 0.3;
setAttr "shoulder_ctrlShape.localScaleZ" 0;
setAttr "shoulder_ctrlShape.localScaleZ" 0.3;
select -cl  ;
select -r shoulder_ctrl ;
move -rpr -1.5 0 0 ;
SnapToPoint; dR_enterForSnap;
select -r shouldJnt_to_elbowCtrl_should_distLoc ;
select -add shouldJnt_to_wristCtrl_should_distLoc ;
parent shouldJnt_to_wristCtrl_should_distLoc shoulder_ctrl ;
// shouldJnt_to_wristCtrl_should_distLoc // 
parent shouldJnt_to_elbowCtrl_should_distLoc shoulder_ctrl ;
// shouldJnt_to_elbowCtrl_should_distLoc // 
select -r shouldJnt_to_elbowCtrl_should_distLoc shouldJnt_to_wristCtrl_should_distLoc ;
select -r shoulder_jnt ;
parent shoulder_jnt shoulder_ctrl ;
// shoulder_jnt // 
select -r shoulder_ctrl ;
rotate -r -oa 0rad 0rad 0rad -ws -fo 6.878963 -5.881785 12.70856 ;
// Undo: rotate -r -oa 0rad 0rad 0rad -ws -fo 6.878963 -5.881785 12.70856 
rotate -r -oa 0rad 0rad 0rad -ws -fo 0 0 11.710249 ;
// Undo: rotate -r -oa 0rad 0rad 0rad -ws -fo 0 0 11.710249 
move -r 1.006937 0.400943 0 ;
// Undo: move -r 1.006937 0.400943 0 
select -r elbow_ctrl ;
move -r 0 0.0677309 -0.00765393 ;
// Undo: move -r 0 0.0677309 -0.00765393 
select -r wrist_ctrl ;
move -r 0.0496697 0 -0.394511 ;
// Undo: move -r 0.0496697 0 -0.394511 
select -r shoulder_ctrl ;
move -r -1.284068 0 0 ;
// Undo: move -r -1.284068 0 0 
move -r -1.513767 -0.372292 0 ;
// Undo: move -r -1.513767 -0.372292 0 
select -cl  ;
select -r elbow_ctrl ;
file -f -save  -options "v=0;";
// F:/maya/projects/TESTING/scenes/stretchy_joints_testing/02/stretchyJoints_midPointSnapping_test_004.ma // 
select -r shouldJnt_to_wristCtrl_dist ;
select -r shouldJnt_to_wristCtrl_dist shouldJnt_to_elbowCtrl_dist ;
select -r shouldJnt_to_wristCtrl_dist shouldJnt_to_elbowCtrl_dist elbowCtrl_to_wristCtrl_dist ;
select -r shouldJnt_to_wristCtrl_dist ;
select -r shoulder_jnt ;
select -add elbow_jnt ;
select -add wrist_jnt ;
select -add shouldJnt_to_wristCtrl_dist ;
select -r shoulder_jnt ;
select -r shoulder_jnt elbow_jnt ;
select -r shoulder_jnt elbow_jnt shouldJnt_to_wristCtrl_dist ;
select -cl  ;
select -r shoulder_jnt ;
select -r elbow_jnt ;
select -r wrist_jnt ;
select -r shouldJnt_to_wristCtrl_distShape ;
select -r MayaNodeEditorSavedTabsInfo ;
select -r shouldJnt_to_wristCtrl_dist ;
select -r shouldJnt_to_wristCtrl_distShape ;
select -r MayaNodeEditorSavedTabsInfo ;
select -r elbow_jnt ;
move -r -ls -wd -0.0253327 -0.125501 0.0130887 ;
// Undo: move -r -ls -wd -0.0253327 -0.125501 0.0130887 
select -tgl wrist_ctrl ;
// Undo: select -tgl wrist_ctrl 
select -cl  ;
select -r wrist_jnt ;
select -tgl elbow_jnt ;
move -r -ls -wd 0.522269 0 0 ;
// Undo: move -r -ls -wd 0.522269 0 0 
move -r -ls -wd 0.232421 0 0 ;
// Undo: move -r -ls -wd 0.232421 0 0 
select -cl  ;
shadingNode -asUtility blendTwoAttr;
// blendTwoAttr1 // 
select -cl  ;
select -r blendTwoAttr1 ;
select -r shouldJnt_to_wristCtrl_distShape ;
select -r blendTwoAttr1 ;
select -cl  ;
select -r upArm_choice_b2a ;
duplicate -rr;select -cl  ;
select -r lowArm_choice_b2a ;
select -r upArm_choice_b2a ;
select -r lowArm_choice_b2a ;
select -r elbowCtrl_to_wristCtrl_dist ;
select -r shouldJnt_to_elbowCtrl_dist ;
select -r upArm_choice_b2a ;
select -r upArm_choice_b2a lowArm_choice_b2a ;
select -r -ne lowArm_choice_b2a upArm_choice_b2a MayaNodeEditorSavedTabsInfo ikSplineSolver ikSCsolver hikSolver defaultViewColorManager time1 strokeGlobals shaderGlow1 sequenceManager1 uiConfigurationScriptNode sceneConfigurationScriptNode defaultResolution defaultRenderQuality renderLayerManager defaultRenderLayer renderGlobalsList1 defaultRenderGlobals postProcessList1 renderPartition characterPartition particleCloud1 initialMaterialInfo lightList1 lightLinker1 lambert1 TurtleUIOptions TurtleRenderOptions TurtleBakeLayerManager ikSystem ikRPsolver hyperGraphLayout hyperGraphInfo defaultHardwareRenderGlobals hardwareRenderingGlobals hardwareRenderGlobals globalCacheControl dynController1 dof1 layerManager defaultLayer defaultTextureList1 defaultShaderList1 defaultRenderingList1 defaultRenderUtilityList1 defaultLightList1 defaultColorMgtGlobals defaultObjectSet defaultLightSet TurtleDefaultBakeLayer effector1 wrist_jnt elbow_jnt shoulder_jnt shouldJnt_to_elbowCtrl_should_distLoc shouldJnt_to_wristCtrl_should_distLoc shoulder_ctrl elbowCtrl_to_wristCtrl_dist shouldJnt_to_elbowCtrl_dist ;
select -cl  ;
select -r upArm_choice_b2a ;
select -r lowArm_choice_b2a ;
select -r lowArm_choice_b2a upArm_choice_b2a ;
select -add shouldJnt_to_elbowCtrl_dist ;
select -add elbowCtrl_to_wristCtrl_dist ;
select -r lowArm_choice_b2a ;
select -r lowArm_choice_b2a upArm_choice_b2a ;
select -cl  ;
select -r shouldJnt_to_elbowCtrl_distShape ;
connectAttr -f shouldJnt_to_elbowCtrl_distShape.distance lowArm_choice_b2a.attributesBlender;
// Connected shouldJnt_to_elbowCtrl_distShape.distance to lowArm_choice_b2a.attributesBlender. // 
select -cl  ;
disconnectAttr shouldJnt_to_elbowCtrl_distShape.distance lowArm_choice_b2a.attributesBlender;
// Disconnect shouldJnt_to_elbowCtrl_distShape.distance from lowArm_choice_b2a.attributesBlender. // 
import maya.cmds as cmds
cmds.connectAttr('shouldJnt_to_elbowCtrl_distShape.distance', 'upArm_choice_b2a.input[0]', f = True)
import maya.cmds as cmds
cmds.connectAttr('elbowCtrl_to_wristCtrl_distShape.distance', 'lowArm_choice_b2a.input[0]', f = True)
#cmds.connectAttr('elbowCtrl_to_wristCtrl_distShape.distance', 'blendTwoAttr2.input[1]', f = True)
select -r elbow_ctrl ;
move -r -0.13239 0 -0.168878 ;
// Undo: move -r -0.13239 0 -0.168878 
select -r lowArm_choice_b2a ;
file -f -save  -options "v=0;";
// F:/maya/projects/TESTING/scenes/stretchy_joints_testing/02/stretchyJoints_midPointSnapping_test_005.ma // 
select -r shoulder_jnt ;
select -tgl elbow_jnt ;
select -tgl wrist_jnt ;
select -add shouldJnt_to_wristCtrl_dist ;
select -cl  ;
select -r shouldJnt_to_wristCtrl_distShape ;
select -cl  ;
shadingNode -asUtility condition;
// condition1 // 
connectAttr -f shouldJnt_to_wristCtrl_distShape.distance condition1.firstTerm;
// Connected shouldJnt_to_wristCtrl_distShape.distance to condition1.firstTerm. // 
select -r elbow_jnt ;
select -r wrist_jnt ;
select -r condition1 ;
setAttr "condition1.secondTerm" 3;
select -cl  ;
select -r condition1 ;
select -r shouldJnt_to_wristCtrl_distShape ;
select -r condition1 ;
select -r shouldJnt_to_wristCtrl_distShape ;
select -r condition1 ;
setAttr "condition1.operation" 2;
setAttr "condition1.colorIfFalseR" 1.5;
connectAttr -f condition1.outColorR elbow_jnt.translateX;
// Connected condition1.outColor.outColorR to elbow_jnt.translate.translateX. // 
connectAttr -f condition1.outColorR wrist_jnt.translateX;
// Connected condition1.outColor.outColorR to wrist_jnt.translate.translateX. // 
select -cl  ;
select -r condition1 ;
select -r wrist_ctrl ;
move -r 0.0181787 0 0 ;
// Undo: move -r 0.0181787 0 0 
select -r condition1 ;
select -cl  ;
shadingNode -asUtility multiplyDivide;
// multiplyDivide1 // 
connectAttr -f shouldJnt_to_wristCtrl_distShape.distance multiplyDivide1.input1X;
// Connected shouldJnt_to_wristCtrl_distShape.distance to multiplyDivide1.input1.input1X. // 
setAttr "multiplyDivide1.input2X" 2;
setAttr "multiplyDivide1.operation" 2;
connectAttr -f multiplyDivide1.outputX condition1.colorIfTrueR;
// Connected multiplyDivide1.output.outputX to condition1.colorIfTrue.colorIfTrueR. // 
select -cl  ;
select -r condition1 ;
select -r wrist_ctrl ;
move -r -0.388255 0 0 ;
// Undo: move -r -0.388255 0 0 
select -r shoulder_ctrl ;
move -r -1.082408 0 0 ;
// Undo: move -r -1.082408 0 0 
select -r wholeArm_scale_cond ;
select -r wholeArm_halfDist_multDiv ;
select -r wholeArm_scale_cond ;
select -r shouldJnt_to_wristCtrl_distShape ;
select -r wholeArm_scale_cond ;
select -add lowArm_choice_b2a ;
select -add upArm_choice_b2a ;
select -r wholeArm_scale_cond ;
select -r lowArm_choice_b2a ;
select -r upArm_choice_b2a ;
select -r lowArm_choice_b2a ;
select -r upArm_choice_b2a ;
select -cl  ;
disconnectAttr wholeArm_scale_cond.outColorR elbow_jnt.translateX;
// Disconnect wholeArm_scale_cond.outColor.outColorR from elbow_jnt.translate.translateX. // 
disconnectAttr wholeArm_scale_cond.outColorR wrist_jnt.translateX;
// Disconnect wholeArm_scale_cond.outColor.outColorR from wrist_jnt.translate.translateX. // 
connectAttr -f wholeArm_scale_cond.outColorR lowArm_choice_b2a.input[1];
// Connected wholeArm_scale_cond.outColor.outColorR to lowArm_choice_b2a.input. // 
connectAttr -f wholeArm_scale_cond.outColorR upArm_choice_b2a.input[1];
// Connected wholeArm_scale_cond.outColor.outColorR to upArm_choice_b2a.input. // 
select -r lowArm_choice_b2a ;
select -r upArm_choice_b2a ;
connectAttr -f lowArm_choice_b2a.output elbow_jnt.translateX;
// Connected lowArm_choice_b2a.output to elbow_jnt.translate.translateX. // 
connectAttr -f upArm_choice_b2a.output wrist_jnt.translateX;
// Connected upArm_choice_b2a.output to wrist_jnt.translate.translateX. // 
select -r elbow_ctrl ;
select -r lowArm_choice_b2a ;
select -r elbow_ctrl ;
addAttr -ln "stretchTo"  -at double  -min 0 -max 1 -dv 0 |elbow_ctrl;
setAttr -e-keyable true |elbow_ctrl.stretchTo;
select -r elbow_ctrl ;
connectAttr -f elbow_ctrl.stretchTo lowArm_choice_b2a.attributesBlender;
// Connected elbow_ctrl.stretchTo to lowArm_choice_b2a.attributesBlender. // 
connectAttr -f elbow_ctrl.stretchTo upArm_choice_b2a.attributesBlender;
// Connected elbow_ctrl.stretchTo to upArm_choice_b2a.attributesBlender. // 
setAttr "elbow_ctrl.stretchTo" 1;
setAttr "elbow_ctrl.stretchTo" 1;
select -r wrist_ctrl ;
move -r 2.342957 0 -0.0607946 ;
select -r elbow_ctrl ;
setAttr "elbow_ctrl.stretchTo" 0;
select -r elbow_ctrl ;
move -r 0.120647 0 0.34397 ;
// Undo: move -r 0.120647 0 0.34397 
select -r lowArm_choice_b2a ;
select -r upArm_choice_b2a ;
select -r elbow_ctrl ;
// Undo: select -r elbow_ctrl 
// Undo: select -r upArm_choice_b2a 
// Undo: select -r lowArm_choice_b2a 
// Undo: select -r elbow_ctrl 
// Undo: setAttr
// Undo: select -r elbow_ctrl 
// Undo: move -r 2.342957 0 -0.0607946 
// Undo: select -r wrist_ctrl 
// Undo: setAttr
select -cl  ;
select -r wholeArm_scale_cond ;
select -r lowArm_choice_b2a ;
select -r upArm_choice_b2a ;
select -r lowArm_choice_b2a ;
select -cl  ;
disconnectAttr elbowCtrl_to_wristCtrl_distShape.distance lowArm_choice_b2a.input[0];
// Disconnect elbowCtrl_to_wristCtrl_distShape.distance from lowArm_choice_b2a.input. // 
disconnectAttr wholeArm_scale_cond.outColorR lowArm_choice_b2a.input[1];
// Disconnect wholeArm_scale_cond.outColor.outColorR from lowArm_choice_b2a.input. // 
select -r upArm_choice_b2a ;
select -cl  ;
select -r upArm_choice_b2a ;
select -cl  ;
disconnectAttr shouldJnt_to_elbowCtrl_distShape.distance upArm_choice_b2a.input[0];
// Disconnect shouldJnt_to_elbowCtrl_distShape.distance from upArm_choice_b2a.input. // 
disconnectAttr wholeArm_scale_cond.outColorR upArm_choice_b2a.input[1];
// Disconnect wholeArm_scale_cond.outColor.outColorR from upArm_choice_b2a.input. // 
select -r upArm_choice_b2a ;
select -r lowArm_choice_b2a ;
select -cl  ;
disconnectAttr lowArm_choice_b2a.output elbow_jnt.translateX;
// Disconnect lowArm_choice_b2a.output from elbow_jnt.translate.translateX. // 
disconnectAttr upArm_choice_b2a.output wrist_jnt.translateX;
// Disconnect upArm_choice_b2a.output from wrist_jnt.translate.translateX. // 
select -r upArm_choice_b2a ;
select -r lowArm_choice_b2a ;
select -r wholeArm_scale_cond ;
connectAttr -f wholeArm_scale_cond.outColorR upArm_choice_b2a.attributesBlender;
// Connected wholeArm_scale_cond.outColor.outColorR to upArm_choice_b2a.attributesBlender. // 
select -cl  ;
disconnectAttr wholeArm_scale_cond.outColorR upArm_choice_b2a.attributesBlender;
// Disconnect wholeArm_scale_cond.outColor.outColorR from upArm_choice_b2a.attributesBlender. // 
import maya.cmds as cmds
cmds.connectAttr('elbowCtrl_to_wristCtrl_distShape.distance', 'lowArm_choice_b2a.input[1]', f = True)
cmds.connectAttr('shouldCtrl_to_elbowCtrl_distShape.distance', 'upArm_choice_b2a.input[1]', f = True)
# Error: RuntimeError: file <maya console> line 3: The source attribute 'shouldCtrl_to_elbowCtrl_distShape.distance' cannot be found. # 
import maya.cmds as cmds
cmds.connectAttr('elbowCtrl_to_wristCtrl_distShape.distance', 'lowArm_choice_b2a.input[1]', f = True)
cmds.connectAttr('shouldJnt_to_elbowCtrl_distShape.distance', 'upArm_choice_b2a.input[1]', f = True)
# Warning: 'elbowCtrl_to_wristCtrl_distShape.distance' is already connected to 'lowArm_choice_b2a.input[1]'. # 
# Error: RuntimeError: file <maya console> line 2: Maya command error # 
select -r lowArm_choice_b2a ;
select -cl  ;
disconnectAttr elbowCtrl_to_wristCtrl_distShape.distance lowArm_choice_b2a.input[1];
// Disconnect elbowCtrl_to_wristCtrl_distShape.distance from lowArm_choice_b2a.input. // 
import maya.cmds as cmds
cmds.connectAttr('elbowCtrl_to_wristCtrl_distShape.distance', 'lowArm_choice_b2a.input[1]', f = True)
cmds.connectAttr('shouldJnt_to_elbowCtrl_distShape.distance', 'upArm_choice_b2a.input[1]', f = True)
select -r lowArm_choice_b2a ;
select -r wholeArm_scale_cond ;
select -r lowArm_choice_b2a ;
select -r wholeArm_scale_cond ;
select -r upArm_choice_b2a ;
select -cl  ;
disconnectAttr shouldJnt_to_elbowCtrl_distShape.distance upArm_choice_b2a.input[1];
// Disconnect shouldJnt_to_elbowCtrl_distShape.distance from upArm_choice_b2a.input. // 
disconnectAttr elbowCtrl_to_wristCtrl_distShape.distance lowArm_choice_b2a.input[1];
// Disconnect elbowCtrl_to_wristCtrl_distShape.distance from lowArm_choice_b2a.input. // 
.
# Error: invalid syntax # 
import maya.cmds as cmds
cmds.connectAttr('wholeArm_scale_cond.outColor.outColorR', 'upArm_choice_b2a.input[0]', f = True)
cmds.connectAttr('wholeArm_scale_cond.outColor.outColorR', 'lowArm_choice_b2a.input[0]', f = True)
cmds.connectAttr('elbowCtrl_to_wristCtrl_distShape.distance', 'lowArm_choice_b2a.input[1]', f = True)
cmds.connectAttr('shouldJnt_to_elbowCtrl_distShape.distance', 'upArm_choice_b2a.input[1]', f = True)
select -r upArm_choice_b2a ;
connectAttr -f upArm_choice_b2a.output elbow_jnt.translateX;
// Connected upArm_choice_b2a.output to elbow_jnt.translate.translateX. // 
connectAttr -f lowArm_choice_b2a.output wrist_jnt.translateX;
// Connected lowArm_choice_b2a.output to wrist_jnt.translate.translateX. // 
select -r elbow_ctrl ;
setAttr "elbow_ctrl.stretchTo" 0;
setAttr "elbow_ctrl.stretchTo" 1;
select -r elbow_ctrl ;
move -r -0.25365 0 -0.149188 ;
// Undo: move -r -0.25365 0 -0.149188 
// Undo: select -r elbow_ctrl 
// Undo: setAttr
select -r wrist_ctrl ;
move -r -0.0058386 0 0.00688466 ;
move -r 1.332024 0 -0.422464 ;
select -r elbow_ctrl ;
setAttr "elbow_ctrl.stretchTo" 1;
select -r wrist_ctrl ;
move -r 0.244846 0 0.876759 ;
select -r elbow_ctrl ;
setAttr "elbow_ctrl.stretchTo" 0;
setAttr "elbow_ctrl.stretchTo" 0.01;
select -r wrist_ctrl ;
move -r -0.228682 0 -0.144898 ;
// Undo: move -r -0.228682 0 -0.144898 
select -r elbow_ctrl ;
setAttr "elbow_ctrl.stretchTo" 0;
select -cl  ;
// Undo: select -cl  
// Undo: setAttr
// Undo: select -r elbow_ctrl 
// Undo: select -r wrist_ctrl 
// Undo: setAttr "elbow_ctrl.stretchTo" 0.01;
// Undo: setAttr
// Undo: select -r elbow_ctrl 
// Undo: move -r 0.244846 0 0.876759 
// Undo: select -r wrist_ctrl 
// Undo: setAttr
// Undo: select -r elbow_ctrl 
// Undo: move -r 1.332024 0 -0.422464 
// Undo: move -r -0.0058386 0 0.00688466 
select -cl  ;
select -r wrist_ctrl ;
setAttr "wrist_ctrl.translateX" 1.5;
move -r -0.166846 0 0 ;
setAttr "wrist_ctrl.translateX" 1.3;
select -r shoulder_ctrl ;
select -r shouldJnt_to_wristCtrl_dist shouldJnt_to_elbowCtrl_dist shoulder_ctrl shouldJnt_to_wristCtrl_should_distLoc shouldJnt_to_elbowCtrl_should_distLoc shoulder_jnt ;
// Undo: select -r shouldJnt_to_wristCtrl_dist shouldJnt_to_elbowCtrl_dist shoulder_ctrl shouldJnt_to_wristCtrl_should_distLoc shouldJnt_to_elbowCtrl_should_distLoc shoulder_jnt 
move -r -1.894967 0 0 ;
// Undo: move -r -1.894967 0 0 
move -r -0.155994 0 0.289045 ;
// Undo: move -r -0.155994 0 0.289045 
select -r elbow_ctrl ;
move -r 0 0.0708125 -0.214001 ;
// Undo: move -r 0 0.0708125 -0.214001 
move -r 0 -0.617335 -0.155327 ;
// Undo: move -r 0 -0.617335 -0.155327 
currentTime 1 ;
setAttr "elbow_ctrl.stretchTo" 1;
select -r wrist_ctrl ;
move -r 0.710639 0 0 ;
setAttr "wrist_ctrl.translateX" 0;
select -cl  ;
select -r elbow_ctrl ;
setAttr "elbow_ctrl.translateZ" 0;
select -cl  ;
// Undo: select -cl  
// Undo: setAttr "elbow_ctrl.translateZ" 0;
// Undo: select -r elbow_ctrl 
// Undo: select -cl  
// Undo: setAttr "wrist_ctrl.translateX" 0;
// Undo: move -r 0.710639 0 0 
// Undo: select -r wrist_ctrl 
// Undo: setAttr
select -cl  ;
// Undo: select -cl  
// Undo: select -r elbow_ctrl 
// Undo: select -r shoulder_ctrl 
// Undo: setAttr "wrist_ctrl.translateX" 1.3;
// Undo: move -r -0.166846 0 0 
// Undo: setAttr "wrist_ctrl.translateX" 1.5;
select -cl  ;
select -r elbow_ctrl ;
move -r -0.153275 0 0 ;
setAttr "elbow_ctrl.stretchTo" 1;
select -r elbow_ctrl ;
select -r elbow_ctrl ;
move -r -0.763802 0 0 ;
// Undo: move -r -0.763802 0 0 
// Undo: select -r elbow_ctrl 
// Undo: select -r elbow_ctrl 
// Undo: setAttr
select -cl  ;
currentTime 1 ;
select -r shouldJnt_to_wristCtrl_dist ;
select -r shouldJnt_to_wristCtrl_dist shouldJnt_to_elbowCtrl_dist elbowCtrl_to_wristCtrl_dist ;
setAttr "elbowCtrl_to_wristCtrl_dist.visibility" 0;
setAttr "shouldJnt_to_wristCtrl_dist.visibility" 0;
setAttr "shouldJnt_to_elbowCtrl_dist.visibility" 0;
select -cl  ;
select -r elbow_ctrl shouldJnt_to_elbowCtrl_elbow_distLoc elbowCtrl_to_wristCtrl_elbow_distLoc ;
select -r elbow_ctrl elbow_jnt ;
// Undo: select -r elbow_ctrl elbow_jnt 
move -r 0 0 0.872217 ;
// Undo: move -r 0 0 0.872217 
select -cl  ;
select -r elbow_ctrl ;
move -r 0 0 0.885478 ;
// Undo: move -r 0 0 0.885478 
select -r wrist_ctrl ;
scale -r 0.106751 0.106751 0.106751 ;
scale -r 0.666962 0.666962 0.666962 ;
FreezeTransformations;
makeIdentity -apply true -t 1 -r 1 -s 1 -n 0 -pn 1;
select -cl  ;
select -r sphere1 ;
select -r sphere1 ;
rename "sphere1" "wrist_anim_ctrl";
// wrist_anim_ctrl // 
select -r effector1 ;
select -r wrist_anim_ctrl ;
duplicate -rr;
// Result: wrist_anim_ctrl1 //
select -r wrist_anim_ctrl1 ;
select -r elbow_jnt ;
scale -r 1 1 1 ;
select -r wrist_ctrl ;
select -r elbow_ctrl ;
setAttr "elbow_ctrl.stretchTo" 1;
select -r wrist_ctrl ;
move -r -0.0325498 0 -0.02638 ;
setAttr "wrist_ctrl.translateZ" 0;
setAttr "wrist_ctrl.translateX" 0;
setAttr "wrist_ctrl.translateY" 0;
select -cl  ;
// Undo: select -cl  
// Undo: setAttr "wrist_ctrl.translateZ" 0;
setAttr "wrist_ctrl.translateX" 0;
setAttr "wrist_ctrl.translateY" 0;
select -r elbow_ctrl shouldJnt_to_elbowCtrl_elbow_distLoc elbowCtrl_to_wristCtrl_elbow_distLoc ;
select -cl  ;
select -r elbow_ctrl ;
setAttr "elbow_ctrl.stretchTo" 0;
select -cl  ;
select -r wrist_anim_ctrl ;
// Undo: select -r wrist_anim_ctrl 
// Undo: select -cl  
// Undo: setAttr
// Undo: select -r elbow_ctrl 
// Undo: select -cl  
// Undo: select -r elbow_ctrl shouldJnt_to_elbowCtrl_elbow_distLoc elbowCtrl_to_wristCtrl_elbow_distLoc 
// Undo: move -r -0.0325498 0 -0.02638 
select -r elbow_ctrl shouldJnt_to_elbowCtrl_elbow_distLoc elbowCtrl_to_wristCtrl_elbow_distLoc ;
select -cl  ;
select -r elbow_ctrl ;
setAttr "elbow_ctrl.stretchTo" 0;
select -r wrist_ctrl ;
select -add wrist_ctrl ;
duplicate -rr;
// Result: wrist_ctrl1 //
select -r wrist_ctrl1|test_ikh ;
select -r wrist_ctrl1|test_ikh wrist_ctrl1|test_ikh|test_ikh_poleVectorConstraint1 wrist_ctrl1|shouldJnt_to_wristCtrl_wrist_distLoc wrist_ctrl1|elbowCtrl_to_wristCtrl_wrist_distLoc ;
select -r wrist_ctrl1 ;
select -r wrist_ctrl ;
move -r -0.0301533 0 -0.0363267 ;
// Undo: move -r -0.0301533 0 -0.0363267 
select -r wrist_ctrl1 ;
rename "wrist_ctrl1" "elbow_snapTO_loc";
// elbow_snapTO_loc // 
select -r elbow_ctrl ;
addAttr -ln "snapTo"  -at double  -min 0 -max 1 -dv 0 |elbow_ctrl;
setAttr -e-keyable true |elbow_ctrl.snapTo;
select -r elbow_snapTO_loc ;
parent elbow_snapTO_loc wrist_ctrl ;
// elbow_snapTO_loc // 
select -r elbow_snapTO_loc ;
select -r elbow_ctrl ;
rotate -r -oa 0rad 0rad 0rad -ws -fo 47.885823 5.571797 13.64582 ;
// Undo: rotate -r -oa 0rad 0rad 0rad -ws -fo 47.885823 5.571797 13.64582 
move -r 0.290013 0 -0.101571 ;
// Undo: move -r 0.290013 0 -0.101571 
select -r elbow_snapTO_loc ;
parent elbow_snapTO_loc elbow_ctrl ;
// elbow_snapTO_loc // 
select -cl  ;
select -r elbow_ctrl ;
move -r -0.00137518 0 -0.00311796 ;
// Undo: move -r -0.00137518 0 -0.00311796 
move -r 0.0222198 0 -0.0103042 ;
// Undo: move -r 0.0222198 0 -0.0103042 
rotate -r -oa 0rad 0rad 0rad -ws -fo 0 -26.190878 0 ;
// Undo: rotate -r -oa 0rad 0rad 0rad -ws -fo 0 -26.190878 0 
select -cl  ;
select -r wrist_anim_ctrl ;
select -r wrist_anim_ctrl1 ;
select -r wrist_anim_ctrl ;
select -add elbow_snapTO_loc ;
select -add wrist_ctrl ;
doCreateParentConstraintArgList 1 { "0","0","0","0","0","0","0","1","","1" };
parentConstraint -weight 1;
// wrist_ctrl_parentConstraint1 // 
select -r wrist_anim_ctrl ;
select -cl  ;
select -r wrist_anim_ctrl ;
move -r -0.0363653 0 0.122914 ;
// Undo: move -r -0.0363653 0 0.122914 
select -r elbow_snapTO_loc ;
setAttr "elbow_snapTO_loc.visibility" 0;
select -r elbow_ctrl ;
move -r -0.00356878 0 0.00091542 ;
select -add elbow_snapTO_loc ;
select -add wrist_anim_ctrl ;
NodeEditorWindow;
select -r elbow_ctrl ;
select -r elbow_snapTO_loc ;
select -r elbow_ctrl ;
select -r elbow_snapTO_loc ;
select -r wrist_anim_ctrl ;
select -r elbow_ctrl ;
select -r wrist_ctrl_parentConstraint1 ;
select -r wrist_ctrl ;
select -r elbow_ctrl ;
shadingNode -asUtility reverse;
// reverse1 // 
// Error: The attribute 'elbow_ctrl.snapTo' cannot be connected to 'reverse1.input'. // 
// Error: The attribute 'elbow_ctrl.snapTo' cannot be connected to 'reverse1.input'. // 
cmds.connectAttr('elbow_ctrl.snapTo', 'reverse1.input.inputX', f = True)
# Connected elbow_ctrl.snapTo to reverse1.input.inputX. # 
connectAttr -f reverse1.outputX wrist_ctrl_parentConstraint1.wrist_anim_ctrlW0;
// Connected reverse1.output.outputX to wrist_ctrl_parentConstraint1.wrist_anim_ctrlW0. // 
select -r elbow_ctrl ;
connectAttr -f elbow_ctrl.snapTo wrist_ctrl_parentConstraint1.elbow_snapTO_locW1;
// Connected elbow_ctrl.snapTo to wrist_ctrl_parentConstraint1.elbow_snapTO_locW1. // 
select -r wrist_ctrl_parentConstraint1 ;
select -r wrist_anim_ctrl ;
move -r -0.329479 0 0.226567 ;
// Undo: move -r -0.329479 0 0.226567 
select -cl  ;
select -r elbow_ctrl ;
setAttr "elbow_ctrl.snapTo" 1;
select -r wrist_anim_ctrl ;
move -r -0.227168 0 0.0709024 ;
// Undo: move -r -0.227168 0 0.0709024 
select -r elbow_ctrl ;
rotate -r -oa 0rad 0rad 0rad -ws -fo 0 -19.81493 0 ;
// Undo: rotate -r -oa 0rad 0rad 0rad -ws -fo 0 -19.81493 0 
select -r wrist_anim_ctrl ;
select -r elbow_ctrl ;
setAttr "elbow_ctrl.snapTo" 0;
select -cl  ;
select -r wrist_anim_ctrl ;
rotate -r -ws -fo 44.730951 -25.073826 17.562695 ;
setAttr "wrist_anim_ctrl.rotateZ" 0;
setAttr "wrist_anim_ctrl.rotateX" 0;
setAttr "wrist_anim_ctrl.rotateY" 0;
select -cl  ;
select -r wrist_anim_ctrl ;
move -r 0 0.384101 -0.220018 ;
// Undo: move -r 0 0.384101 -0.220018 
move -r -1.377562 0 1.014218 ;
select -r elbow_ctrl ;
setAttr "elbow_ctrl.snapTo" 1;
// Undo: setAttr
// Undo: select -r elbow_ctrl 
// Undo: move -r -1.377562 0 1.014218 
select -r elbow_snapTO_loc ;
select -r elbowCtrl_to_wristCtrl_elbow_distLoc ;
select -r elbow_snapTO_loc ;
select -r elbow_ctrl ;
setAttr "elbow_ctrl.stretchTo" 1;
setAttr "elbow_ctrl.snapTo" 1;
select -r elbow_ctrl ;
rotate -r -oa 0rad 0rad 0rad -ws -fo 0 -17.423782 0 ;
// Undo: rotate -r -oa 0rad 0rad 0rad -ws -fo 0 -17.423782 0 
rotate -r -oa 0rad 0rad 0rad -ws -fo 9.646798 -2.928913 7.278865 ;
// Undo: rotate -r -oa 0rad 0rad 0rad -ws -fo 9.646798 -2.928913 7.278865 
// Undo: select -r elbow_ctrl 
// Undo: setAttr
// Undo: setAttr
select -cl  ;
select -r wrist_anim_ctrl ;
rotate -r -ws -fo 22.384764 3.040413 63.534014 ;
// Undo: rotate -r -ws -fo 22.384764 3.040413 63.534014 
move -r -0.471093 0 -0.326647 ;
// Undo: move -r -0.471093 0 -0.326647 
currentTime 1 ;
select -cl  ;
select -r wrist_anim_ctrl ;
move -r 0.386245 0 -0.521122 ;
// Undo: move -r 0.386245 0 -0.521122 
select -r elbow_ctrl ;
setAttr "elbow_ctrl.stretchTo" 1;
setAttr "elbow_ctrl.stretchTo" 1;
select -r elbow_jnt ;
select -r wrist_anim_ctrl ;
select -cl  ;
select -r elbow_jnt ;
move -r -ls -wd 0 -2.528181 0 ;
// Undo: move -r -ls -wd 0 -2.528181 0 
move -r -ls -wd 0 0 -1.305233 ;
// Undo: move -r -ls -wd 0 0 -1.305233 
select -r elbow_ctrl ;
select -cl  ;
select -r wrist_jnt ;
select -r elbow_jnt ;
select -r elbow_ctrl ;
select -r elbow_ctrl ;
select -r lowArm_choice_b2a ;
select -r elbow_ctrl ;
select -r elbow_jnt ;
select -r elbow_ctrl ;
setAttr "elbow_ctrl.stretchTo" 0;
select -r elbow_jnt ;
select -r upArm_choice_b2a ;
select -r elbow_jnt ;
select -r upArm_choice_b2a ;
select -r elbow_jnt ;
select -r upArm_choice_b2a ;
select -r elbow_ctrl ;
select -r upArm_choice_b2a ;
select -tgl elbow_ctrl ;
select -r upArm_choice_b2a ;
select -r elbow_ctrl ;
select -r lowArm_choice_b2a ;
select -r elbow_ctrl ;
connectAttr -f elbow_ctrl.stretchTo upArm_choice_b2a.attributesBlender;
// Connected elbow_ctrl.stretchTo to upArm_choice_b2a.attributesBlender. // 
select -cl  ;
select -r elbow_ctrl ;
setAttr "elbow_ctrl.stretchTo" 1;
select -r elbow_ctrl ;
rotate -r -oa 0rad 0rad 0rad -ws -fo 14.197484 11.365551 27.845683 ;
// Undo: rotate -r -oa 0rad 0rad 0rad -ws -fo 14.197484 11.365551 27.845683 
move -r -0.48799 0 0.455854 ;
// Undo: move -r -0.48799 0 0.455854 
move -r -0.128678 0 0.234145 ;
select -r shoulder_ctrl ;
move -r 0 0.463397 0 ;
// Undo: move -r 0 0.463397 0 
move -r -0.176276 0.341146 0 ;
// Undo: move -r -0.176276 0.341146 0 
select -cl  ;
select -r elbow_ctrl ;
setAttr "elbow_ctrl.snapTo" 1;
select -r wrist_anim_ctrl ;
move -r 0.175793 0 0.113648 ;
// Undo: move -r 0.175793 0 0.113648 
select -r elbow_ctrl ;
rotate -r -oa 0rad 0rad 0rad -ws -fo -12.086441 -4.131916 -3.934157 ;
// Undo: rotate -r -oa 0rad 0rad 0rad -ws -fo -12.086441 -4.131916 -3.934157 
setAttr "elbow_ctrl.stretchTo" 0;
setAttr "elbow_ctrl.snapTo" 0;
select -cl  ;
select -r wrist_anim_ctrl ;
select -r test_ikh ;
select -r elbow_snapTO_loc ;
setAttr "elbow_snapTO_loc.visibility" 1;
setAttr "elbow_snapTO_loc.translateZ" 0;
setAttr "elbow_snapTO_loc.translateX" 0;
setAttr "elbow_snapTO_loc.translateY" 0;
select -cl  ;
select -r elbow_snapTO_loc ;
move -rpr 1.319078 0 0 elbow_snapTO_loc.scalePivot elbow_snapTO_loc.rotatePivot ;
SnapToPoint; dR_enterForSnap;
select -r shouldJnt_to_elbowCtrl_elbow_distLoc ;
select -r wrist_anim_ctrl ;
move -r -2.106918 0 0.89537 ;
select -cl  ;
select -r elbow_ctrl shouldJnt_to_elbowCtrl_elbow_distLoc elbowCtrl_to_wristCtrl_elbow_distLoc elbow_snapTO_loc ;
select -add elbow_ctrl ;
setAttr "elbow_ctrl.stretchTo" 1;
setAttr "elbow_ctrl.snapTo" 1;
setAttr "elbow_ctrl.snapTo" 1;
select -cl  ;
// Undo: select -cl  
// Undo: setAttr
// Undo: setAttr
// Undo: select -add elbow_ctrl 
// Undo: select -r elbow_ctrl shouldJnt_to_elbowCtrl_elbow_distLoc elbowCtrl_to_wristCtrl_elbow_distLoc elbow_snapTO_loc 
// Undo: select -cl  
// Undo: move -r -2.106918 0 0.89537 
// Undo: select -r wrist_anim_ctrl 
// Undo: select -r shouldJnt_to_elbowCtrl_elbow_distLoc 
// Undo: move -rpr 1.319078 0 0 elbow_snapTO_loc.scalePivot elbow_snapTO_loc.rotatePivot 
// Undo: select -r elbow_snapTO_loc 
select -r wrist_ctrl ;
select -r elbow_snapTO_loc ;
select -r elbowCtrl_to_wristCtrl_elbow_distLoc ;
select -r elbow_snapTO_loc ;
select -r wrist_ctrl ;
move -r -0.00138146 0 0.0152174 ;
// Undo: move -r -0.00138146 0 0.0152174 
select -r wrist_anim_ctrl ;
move -r -0.611425 0 0.0443298 ;
// Undo: move -r -0.611425 0 0.0443298 
select -r elbow_ctrl ;
move -r 0 -1.795273 1.847119 ;
// Undo: move -r 0 -1.795273 1.847119 
move -rpr -0.0904611 0 -0.51303 ;
SnapToPoint; dR_enterForSnap;
select -cl  ;
select -r elbow_ctrl ;
setAttr "elbow_ctrl.stretchTo" 1;
select -r elbow_ctrl ;
move -r -0.797261 0 -0.644799 ;
// Undo: move -r -0.797261 0 -0.644799 
select -r shoulder_ctrl ;
rotate -r -oa 0rad 0rad 0rad -ws -fo 0 0 -34.514759 ;
// Undo: rotate -r -oa 0rad 0rad 0rad -ws -fo 0 0 -34.514759 
move -r 0.906235 0.982265 0 ;
select -r elbow_ctrl ;
setAttr "elbow_ctrl.snapTo" 1;
rotate -r -oa 0rad 0rad 0rad -ws -fo 4.132557 -3.425841 5.579857 ;
// Undo: rotate -r -oa 0rad 0rad 0rad -ws -fo 4.132557 -3.425841 5.579857 
// Undo: setAttr
// Undo: select -r elbow_ctrl 
select -r elbow_snapTO_loc ;
// Undo: select -r elbow_snapTO_loc 
// Undo: move -r 0.906235 0.982265 0 
// Undo: select -r shoulder_ctrl 
// Undo: select -r elbow_ctrl 
// Undo: setAttr
// Undo: select -r elbow_ctrl 
// Undo: select -cl  
// Undo: move -rpr -0.0904611 0 -0.51303 
file -save;
// F:/maya/projects/TESTING/scenes/stretchy_joints_testing/02/stretchyJoints_midPointSnapping_test_005.ma // 
select -cl  ;
#make IK elbow_ctrl attributes for snapping IK_jnts to the IK elbow_ctrl and building the IK mock FK control setup 
import maya.cmds as cmds
'''
cmds.connectAttr('wholeArm_scale_cond.outColor.outColorR', 'upArm_choice_b2a.input[0]', f = True)
cmds.connectAttr('wholeArm_scale_cond.outColor.outColorR', 'lowArm_choice_b2a.input[0]', f = True)
cmds.connectAttr('elbowCtrl_to_wristCtrl_distShape.distance', 'lowArm_choice_b2a.input[1]', f = True)
cmds.connectAttr('shouldJnt_to_elbowCtrl_distShape.distance', 'upArm_choice_b2a.input[1]', f = True)
cmds.connectAttr('elbow_ctrl.snapTo', 'reverse1.input.inputX', f = True)
'''

#make IK elbow_ctrl attributes for stretching to and mock FK
ikElbowCtrl = 'elbow_ctrl'
cmds.select(ikElbowCtrl)
newStretchAttr = cmds.addAttr(longName = 'hokeypokey', dv = 1.0, minValue = 0, maxValue = 2)

#make IK elbow_ctrl attributes for snapping IK_jnts to the IK elbow_ctrl and building the IK mock FK control setup 
import maya.cmds as cmds
'''
cmds.connectAttr('wholeArm_scale_cond.outColor.outColorR', 'upArm_choice_b2a.input[0]', f = True)
cmds.connectAttr('wholeArm_scale_cond.outColor.outColorR', 'lowArm_choice_b2a.input[0]', f = True)
cmds.connectAttr('elbowCtrl_to_wristCtrl_distShape.distance', 'lowArm_choice_b2a.input[1]', f = True)
cmds.connectAttr('shouldJnt_to_elbowCtrl_distShape.distance', 'upArm_choice_b2a.input[1]', f = True)
cmds.connectAttr('elbow_ctrl.snapTo', 'reverse1.input.inputX', f = True)
'''

#make IK elbow_ctrl attributes for stretching to and mock FK
ikElbowCtrl = 'elbow_ctrl'
cmds.select(ikElbowCtrl)
newStretchAttr = cmds.addAttr(longName = 'hokeypokey', dv = 1.0, minValue = 0, maxValue = 2, k = True)

# Warning: Name 'hokeypokey' of new attribute clashes with an existing attribute of node 'elbow_ctrl'. # 
# Error: RuntimeError: file <maya console> line 14: Found no valid items to add the attribute to. # 
file -f -options "v=0;"  -ignoreVersion  -typ "mayaAscii" -o "F:/maya/projects/TESTING/scenes/stretchy_joints_testing/02/stretchyJoints_midPointSnapping_test_005.ma";addRecentFile("F:/maya/projects/TESTING/scenes/stretchy_joints_testing/02/stretchyJoints_midPointSnapping_test_005.ma", "mayaAscii");
closeAllNodeEditors;
closeHypershade;
optionVar -sv colorManagementColorPickerColorSpaceSelection "Rendering Space";
optionVar -iv colorManagementColorPickerColorMgtEnabled 1;
// Warning: line 2003: The default image may not be modified. Use the -i/image flag instead. // 
// File read in  0.26 seconds.
#make IK elbow_ctrl attributes for snapping IK_jnts to the IK elbow_ctrl and building the IK mock FK control setup 
import maya.cmds as cmds
'''
cmds.connectAttr('wholeArm_scale_cond.outColor.outColorR', 'upArm_choice_b2a.input[0]', f = True)
cmds.connectAttr('wholeArm_scale_cond.outColor.outColorR', 'lowArm_choice_b2a.input[0]', f = True)
cmds.connectAttr('elbowCtrl_to_wristCtrl_distShape.distance', 'lowArm_choice_b2a.input[1]', f = True)
cmds.connectAttr('shouldJnt_to_elbowCtrl_distShape.distance', 'upArm_choice_b2a.input[1]', f = True)
cmds.connectAttr('elbow_ctrl.snapTo', 'reverse1.input.inputX', f = True)
'''

#make IK elbow_ctrl attributes for stretching to and mock FK
ikElbowCtrl = 'elbow_ctrl'
cmds.select(ikElbowCtrl)
newStretchAttr = cmds.addAttr(longName = 'hokeypokey', dv = 1.0, minValue = 0, maxValue = 2, k = True)

setAttr "elbow_ctrl.hokeypokey" 0;
setAttr "elbow_ctrl.hokeypokey" 1;
file -f -options "v=0;"  -ignoreVersion  -typ "mayaAscii" -o "F:/maya/projects/TESTING/scenes/stretchy_joints_testing/02/stretchyJoints_midPointSnapping_test_005.ma";addRecentFile("F:/maya/projects/TESTING/scenes/stretchy_joints_testing/02/stretchyJoints_midPointSnapping_test_005.ma", "mayaAscii");
closeAllNodeEditors;
closeHypershade;
optionVar -sv colorManagementColorPickerColorSpaceSelection "Rendering Space";
optionVar -iv colorManagementColorPickerColorMgtEnabled 1;
// Warning: line 2003: The default image may not be modified. Use the -i/image flag instead. // 
// File read in  0.27 seconds.
#make IK elbow_ctrl attributes for snapping IK_jnts to the IK elbow_ctrl and building the IK mock FK control setup 
import maya.cmds as cmds
'''
cmds.connectAttr('wholeArm_scale_cond.outColor.outColorR', 'upArm_choice_b2a.input[0]', f = True)
cmds.connectAttr('wholeArm_scale_cond.outColor.outColorR', 'lowArm_choice_b2a.input[0]', f = True)
cmds.connectAttr('elbowCtrl_to_wristCtrl_distShape.distance', 'lowArm_choice_b2a.input[1]', f = True)
cmds.connectAttr('shouldJnt_to_elbowCtrl_distShape.distance', 'upArm_choice_b2a.input[1]', f = True)
cmds.connectAttr('elbow_ctrl.snapTo', 'reverse1.input.inputX', f = True)
'''

#make IK elbow_ctrl attributes for stretching to and mock FK
ikElbowCtrl = 'elbow_ctrl'
cmds.select(ikElbowCtrl)
newStretchAttr = cmds.addAttr(longName = 'hokeypokey', dv = 1.0, minValue = 0, maxValue = 2, k = True)
newSnapAttr = cmds.addAttr(longName = 'honkeytonk', dv = 0, minValue = 0, maxValue = 10, k = True)

setAttr "elbow_ctrl.honkeytonk" 0;
select -cl  ;
select -r elbow_ctrl ;
shouldToElbowDistNode = cmds.createNode('distance')
# Warning: Unrecognized node type 'distance'; preserving node information during this session. # 
select -r MayaNodeEditorSavedTabsInfo ;
select -r unknown1 ;
select -r MayaNodeEditorSavedTabsInfo ;
select -r shouldJnt_to_wristCtrl_dist ;
shouldToElbowDistNode = cmds.createNode('distanceTool')

# Warning: Unrecognized node type 'distanceTool'; preserving node information during this session. # 
select -r MayaNodeEditorSavedTabsInfo ;
select -r unknown1 ;
select -r lowArm_choice_b2a ;
select -r upArm_choice_b2a ;
select -r shouldJnt_to_wristCtrl_dist ;
shouldToElbowDistNode = cmds.createNode('measureTool')

# Warning: Unrecognized node type 'measureTool'; preserving node information during this session. # 
select -r MayaNodeEditorSavedTabsInfo ;
select -r unknown1 ;
distanceDimension -sp 0.877556 0 1.045501 -ep -0.504701 0 0.266541 ;
// distanceDimension1 distanceDimensionShape1 // 
select -r locator1 locator2 distanceDimension1 ;
doDelete;
shouldToElbowDistNode = cmds.createNode('distanceDimension')
# Warning: Unrecognized node type 'distanceDimension'; preserving node information during this session. # 
select -r MayaNodeEditorSavedTabsInfo ;
select -r unknown1 ;
select -r shouldJnt_to_wristCtrl_dist ;
select -r shouldJnt_to_elbowCtrl_dist ;
select -r elbowCtrl_to_wristCtrl_dist ;
select -r shouldJnt_to_wristCtrl_dist ;
select -r shouldJnt_to_elbowCtrl_dist ;
select -r elbowCtrl_to_wristCtrl_dist ;
select -r shouldJnt_to_wristCtrl_dist ;
select -r shouldJnt_to_elbowCtrl_dist ;
select -r elbowCtrl_to_wristCtrl_dist ;
select -r shouldJnt_to_wristCtrl_dist ;
select -r shouldJnt_to_elbowCtrl_dist ;
select -r elbowCtrl_to_wristCtrl_dist ;
select -r shouldJnt_to_wristCtrl_dist ;
select -r shouldJnt_to_elbowCtrl_dist ;
select -r shouldJnt_to_wristCtrl_dist ;
select -r shouldJnt_to_elbowCtrl_dist ;
select -r shouldJnt_to_wristCtrl_dist ;
select -r shouldJnt_to_elbowCtrl_dist ;
select -r shouldJnt_to_wristCtrl_dist ;
select -r elbow_ctrl ;
shouldToElbowDistNode = cmds.distanceDimension(sp = (0.0,0.0,0.0), ep = (1.0,0.0,0.0))
select -r locator1 ;
select -r locator2 ;
select -r distanceDimension1 ;
select -r locator2 ;
select -r locator1 ;
select -r distanceDimension1 ;
select -r distanceDimension1 locator2 locator1 ;
shouldToElbowDistNode = cmds.distanceDimension(sp = (0.0,0.0,0.0), ep = (1.0,0.0,0.0))
print shouldToElbowDistNode
distanceDimensionShape1
select -r distanceDimension1 locator2 locator1 ;
print cmds.xform(ikElbowCtrl, t = True)
# Error: TypeError: file <maya console> line 1: Invalid arguments for flag 't'.  Expected ( distance, distance, distance ), got bool # 
select -r elbow_ctrl shouldJnt_to_elbowCtrl_elbow_distLoc elbowCtrl_to_wristCtrl_elbow_distLoc elbow_snapTO_loc ;
rotate -r -oa 0rad 0rad 0rad -ws -fo -4.823614 14.971762 35.096268 ;
// Undo: rotate -r -oa 0rad 0rad 0rad -ws -fo -4.823614 14.971762 35.096268 
select -cl  ;
select -r elbow_ctrl ;
rotate -r -oa 0rad 0rad 0rad -ws -fo 10.086264 6.097023 11.143928 ;
// Undo: rotate -r -oa 0rad 0rad 0rad -ws -fo 10.086264 6.097023 11.143928 
print cmds.xform(ikElbowCtrl, t = True, os = True)
# Error: TypeError: file <maya console> line 1: Invalid arguments for flag 't'.  Expected ( distance, distance, distance ), got bool # 
cmds.select(ikElbowCtrl)
print cmds.xform(t = True, os = True)
# Error: TypeError: file <maya console> line 2: Invalid arguments for flag 't'.  Expected ( distance, distance, distance ), got bool # 
cmds.select(ikElbowCtrl)
print cmds.xform(q = True, t = True, os = True)
[-0.28552088507569817, 0.0, -1.1441502399059793]
select -r shoulder_jnt ;
cmds.select(ikElbowCtrl)
ikElbowCtrl_trans = cmds.xform(q = True, t = True, os = True)
cmds.select('shoulder_jnt')
shouldJnt_trans = cmds.xform(q = True, t = True, os = True)
shouldToElbowDistNode_shape = cmds.distanceDimension(sp = shouldJnt_trans, ep = ikElbowCtrl_trans)
select -cl  ;
select -r shoulder_jnt ;
select -add wrist_anim_ctrl ;
select -d wrist_anim_ctrl ;
select -add distanceDimension1 ;
select -add locator1 ;
cmds.select(ikElbowCtrl)
ikElbowCtrl_trans = cmds.xform(q = True, t = True, os = True)
cmds.select('shoulder_jnt')
shouldJnt_trans = cmds.xform(q = True, t = True, a = True)
shouldToElbowDistNode_shape = cmds.distanceDimension(sp = shouldJnt_trans, ep = ikElbowCtrl_trans)
print shouldToElbowDistNode_shape
# Error: ValueError: file <maya console> line 3: No object matches name: shoulder_jnt # 
select -cl  ;
// Undo: select -cl  
// Undo: cmds.select(ikElbowCtrl)
ikElbowCtrl_trans = cmds.xform(q = True, t = True, os = True)
cmds.select('shoulder_jnt')
shouldJnt_trans = cmds.xform(q = True, t = True, a = True)
shouldToElbowDistNode_shape = cmds.distanceDimension(sp = shouldJnt_trans, ep = ikElbowCtrl_trans)
print shouldToElbowDistNode_shape
// Undo: doDelete
select -r locator1 ;
select -cl  ;
select -r distanceDimension1 ;
select -r locator1 ;
select -r shoulder_ctrl ;
select -cl  ;
select -r elbow_ctrl ;
move -r -0.0101679 0 0.0513091 ;
// Undo: move -r -0.0101679 0 0.0513091 
cmds.select(ikElbowCtrl)
ikElbowCtrl_trans = cmds.xform(q = True, t = True, os = True)
cmds.select('shoulder_jnt')
shouldJnt_trans = cmds.xform(q = True, t = True,  = True)
shouldToElbowDistNode_shape = cmds.distanceDimension(sp = 'shoulder_jnt', ep = ikElbowCtrl_trans)
print shouldToElbowDistNode_shape
# Error: invalid syntax # 
select -r wrist_anim_ctrl ;
select -r distanceDimension1 ;
select -add locator1 ;
#make distance measure nodes snapping to shoulder_jnt and ik_elbow_ctrl
cmds.select(ikElbowCtrl)
ikElbowCtrl_trans = cmds.xform(q = True, t = True, os = True)
cmds.select('shoulder_jnt')
shouldJnt_trans = cmds.xform(q = True, t = True,  = True)
shouldToElbowDistNode_shape = cmds.distanceDimension(sp = 'shoulder_jnt', ep = ikElbowCtrl_trans)
print shouldToElbowDistNode_shape
# Error: invalid syntax # 
#make distance measure nodes snapping to shoulder_jnt and ik_elbow_ctrl
cmds.select(ikElbowCtrl)
ikElbowCtrl_trans = cmds.xform(q = True, t = True, os = True)
cmds.select('shoulder_jnt')
shouldJnt_trans = cmds.xform(q = True, t = True,  = True)
shouldToElbowDistNode_shape = cmds.distanceDimension(sp = shouldJnt_trans, ep = ikElbowCtrl_trans)
print shouldToElbowDistNode_shape
# Error: invalid syntax # 
cmds.select(ikElbowCtrl)
ikElbowCtrl_trans = cmds.xform(q = True, t = True, os = True)
cmds.select('shoulder_jnt')
shouldJnt_trans = cmds.xform(q = True, t = True,  = True)
shouldToElbowDistNode_shape = cmds.distanceDimension(sp = shouldJnt_trans, ep = ikElbowCtrl_trans)
# Error: invalid syntax # 
cmds.select(ikElbowCtrl)
ikElbowCtrl_trans = cmds.xform(q = True, t = True, os = True)
cmds.select('shoulder_jnt')
shouldJnt_trans = cmds.xform(q = True, t = True,  a = True)
shouldToElbowDistNode_shape = cmds.distanceDimension(sp = shouldJnt_trans, ep = ikElbowCtrl_trans)
select -r locator1 ;
select -add distanceDimension1 ;
cmds.select(ikElbowCtrl)
ikElbowCtrl_trans = cmds.xform(q = True, t = True, os = True)
cmds.select('shoulder_jnt')
shouldJnt_trans = cmds.xform(q = True, t = True,  ws = True)
shouldToElbowDistNode_shape = cmds.distanceDimension(sp = shouldJnt_trans, ep = ikElbowCtrl_trans)
print shouldToElbowDistNode_shape
distanceDimensionShape1
select -r elbow_ctrl ;
move -r -0.0751695 0 -0.00784847 ;
// Undo: move -r -0.0751695 0 -0.00784847 
select -r shoulder_ctrl ;
select -r wrist_anim_ctrl ;
select -r distanceDimension1 ;
select -r wrist_anim_ctrl ;
select -r distanceDimension1 ;
select -r wrist_anim_ctrl ;
select -r distanceDimension1 ;
select -r wrist_anim_ctrl ;
select -r distanceDimension1 ;
move -r -0.486669 0 -0.0435101 ;
// Undo: move -r -0.486669 0 -0.0435101 
select -r wrist_anim_ctrl ;
select -r distanceDimension1 ;
select -r wrist_anim_ctrl ;
select -r shoulder_ctrl ;
select -r wrist_ctrl ;
select -r elbow_ctrl ;
select -r elbow_snapTO_loc ;
select -r elbowCtrl_to_wristCtrl_elbow_distLoc ;
select -r shouldJnt_to_elbowCtrl_elbow_distLoc ;
select -r elbow_snapTO_loc ;
select -r wrist_ctrl ;
select -r shoulder_ctrl ;
shouldToElbowDistNode_shape = cmds.distanceDimension(sp = (0.0,0.0,0.0), ep = (1.0,0.0,0.0))
print shouldToElbowDistNode_shape
distanceDimensionShape2
shouldToElbowDistNode_shape = cmds.distanceDimension(sp = (0.0,0.0,0.0), ep = (1.0,0.0,0.0))
print shouldToElbowDistNode_shape
shouldToElbowDistNode = cmds.listRelatives(shouldToElbowDistNode_shape, p = True)
print shouldToElbowDistNode
distanceDimensionShape3
[u'distanceDimension3']
print cmds.listConnections(shouldToElbowDistNode_shape)
[u'locator1', u'locator2']
file -f -options "v=0;"  -ignoreVersion  -typ "mayaAscii" -o "F:/maya/projects/TESTING/scenes/stretchy_joints_testing/02/stretchyJoints_midPointSnapping_test_005.ma";addRecentFile("F:/maya/projects/TESTING/scenes/stretchy_joints_testing/02/stretchyJoints_midPointSnapping_test_005.ma", "mayaAscii");
closeAllNodeEditors;
closeHypershade;
optionVar -sv colorManagementColorPickerColorSpaceSelection "Rendering Space";
optionVar -iv colorManagementColorPickerColorMgtEnabled 1;
// Warning: line 2003: The default image may not be modified. Use the -i/image flag instead. // 
// File read in  0.29 seconds.
#make IK elbow_ctrl attributes for snapping IK_jnts to the IK elbow_ctrl and building the IK mock FK control setup 
import maya.cmds as cmds
'''
cmds.connectAttr('wholeArm_scale_cond.outColor.outColorR', 'upArm_choice_b2a.input[0]', f = True)
cmds.connectAttr('wholeArm_scale_cond.outColor.outColorR', 'lowArm_choice_b2a.input[0]', f = True)
cmds.connectAttr('elbowCtrl_to_wristCtrl_distShape.distance', 'lowArm_choice_b2a.input[1]', f = True)
cmds.connectAttr('shouldJnt_to_elbowCtrl_distShape.distance', 'upArm_choice_b2a.input[1]', f = True)
cmds.connectAttr('elbow_ctrl.snapTo', 'reverse1.input.inputX', f = True)
'''

#make IK elbow_ctrl attributes for stretching to and mock FK
ikElbowCtrl = 'elbow_ctrl'
cmds.select(ikElbowCtrl)
newStretchAttr = cmds.addAttr(longName = 'hokeypokey', dv = 1.0, minValue = 0, maxValue = 2, k = True)
newMockFkAttr = cmds.addAttr(longName = 'honkeytonk', dv = 0, minValue = 0, maxValue = 10, k = True)

#make distance measure nodes snapping to shoulder_jnt and ik_elbow_ctrl
shouldToElbowDistNode_shape = cmds.distanceDimension(sp = (0.0,0.0,0.0), ep = (1.0,0.0,0.0))
print shouldToElbowDistNode_shape
shouldToElbowDistNode = cmds.listRelatives(shouldToElbowDistNode_shape, p = True)[0]
print shouldToElbowDistNode
shouldToElbowDistNode_locs = cmds.listConnections(shouldToElbowDistNode_shape)
shouldToElbowDistNode_locA_raw = shouldToElbowDistNode_locs[0]
shouldToElbowDistNode_locB_raw = shouldToElbowDistNode_locs[1]
shouldToElbowDistNode_locA = cmds.rename(shouldToElbowDistNode_locs[0], 'shouldJnt_to_elbowCtrl_should_distLoc')
shouldToElbowDistNode_locB = cmds.rename(shouldToElbowDistNode_locs[1], 'shouldJnt_to_elbowCtrl_elbow_distLoc')
cmds.parentConstraint(ikElbowCtrl, shouldToElbowDistNode_locB, mo = False)
cmds.delete(cmds.parentConstraint('shoudler_jnt', shouldToElbowDistNode_locA, mo = False))

distanceDimensionShape1
distanceDimension1
# Error: ValueError: file <maya console> line 28: No object matches name: shoudler_jnt # 
file -f -options "v=0;"  -ignoreVersion  -typ "mayaAscii" -o "F:/maya/projects/TESTING/scenes/stretchy_joints_testing/02/stretchyJoints_midPointSnapping_test_005.ma";addRecentFile("F:/maya/projects/TESTING/scenes/stretchy_joints_testing/02/stretchyJoints_midPointSnapping_test_005.ma", "mayaAscii");
closeAllNodeEditors;
closeHypershade;
optionVar -sv colorManagementColorPickerColorSpaceSelection "Rendering Space";
optionVar -iv colorManagementColorPickerColorMgtEnabled 1;
// Warning: line 2003: The default image may not be modified. Use the -i/image flag instead. // 
// File read in  0.22 seconds.
#make IK elbow_ctrl attributes for snapping IK_jnts to the IK elbow_ctrl and building the IK mock FK control setup 
import maya.cmds as cmds
'''
cmds.connectAttr('wholeArm_scale_cond.outColor.outColorR', 'upArm_choice_b2a.input[0]', f = True)
cmds.connectAttr('wholeArm_scale_cond.outColor.outColorR', 'lowArm_choice_b2a.input[0]', f = True)
cmds.connectAttr('elbowCtrl_to_wristCtrl_distShape.distance', 'lowArm_choice_b2a.input[1]', f = True)
cmds.connectAttr('shouldJnt_to_elbowCtrl_distShape.distance', 'upArm_choice_b2a.input[1]', f = True)
cmds.connectAttr('elbow_ctrl.snapTo', 'reverse1.input.inputX', f = True)
'''

#make IK elbow_ctrl attributes for stretching to and mock FK
ikElbowCtrl = 'elbow_ctrl'
cmds.select(ikElbowCtrl)
newStretchAttr = cmds.addAttr(longName = 'hokeypokey', dv = 1.0, minValue = 0, maxValue = 2, k = True)
newMockFkAttr = cmds.addAttr(longName = 'honkeytonk', dv = 0, minValue = 0, maxValue = 10, k = True)

#make distance measure nodes snapping to shoulder_jnt and ik_elbow_ctrl
shouldToElbowDistNode_shape = cmds.distanceDimension(sp = (0.0,0.0,0.0), ep = (1.0,0.0,0.0))
print shouldToElbowDistNode_shape
shouldToElbowDistNode = cmds.listRelatives(shouldToElbowDistNode_shape, p = True)[0]
print shouldToElbowDistNode
shouldToElbowDistNode_locs = cmds.listConnections(shouldToElbowDistNode_shape)
shouldToElbowDistNode_locA_raw = shouldToElbowDistNode_locs[0]
shouldToElbowDistNode_locB_raw = shouldToElbowDistNode_locs[1]
shouldToElbowDistNode_locA = cmds.rename(shouldToElbowDistNode_locs[0], 'shouldJnt_to_elbowCtrl_should_distLoc')
shouldToElbowDistNode_locB = cmds.rename(shouldToElbowDistNode_locs[1], 'shouldJnt_to_elbowCtrl_elbow_distLoc')
cmds.parentConstraint(ikElbowCtrl, shouldToElbowDistNode_locB, mo = False)
cmds.delete(cmds.parentConstraint('shoulder_jnt', shouldToElbowDistNode_locA, mo = False))

distanceDimensionShape1
distanceDimension1
select -cl  ;
select -r elbow_ctrl ;
move -r 0.202255 0 -0.0414158 ;
// Undo: move -r 0.202255 0 -0.0414158 
select -r shoulder_ctrl ;
move -r 0.00733082 0 0.0396926 ;
// Undo: move -r 0.00733082 0 0.0396926 
select -r |shouldJnt_to_elbowCtrl_should_distLoc ;
select -r shoulder_ctrl ;
select -r |shouldJnt_to_elbowCtrl_should_distLoc ;
select -r wrist_ctrl ;
move -r -1.106313 0 0.117101 ;
// Undo: move -r -1.106313 0 0.117101 
select -cl  ;
select -r wrist_anim_ctrl ;
move -r -0.0877985 0 -0.00566226 ;
// Undo: move -r -0.0877985 0 -0.00566226 
select -r shoulder_ctrl ;
select -r |shouldJnt_to_elbowCtrl_should_distLoc ;
select -r |shouldJnt_to_elbowCtrl_elbow_distLoc ;
select -r wrist_ctrl ;
select -r wrist_ctrl_parentConstraint1 ;
select -r elbowCtrl_to_wristCtrl_wrist_distLoc ;
select -r shouldJnt_to_wristCtrl_wrist_distLoc ;
select -r elbowCtrl_to_wristCtrl_wrist_distLoc ;
select -r elbowCtrl_to_wristCtrl_wrist_distLoc ;
select -r shouldJnt_to_wristCtrl_wrist_distLoc ;
select -r elbowCtrl_to_wristCtrl_wrist_distLoc ;
select -r shouldJnt_to_wristCtrl_wrist_distLoc ;
select -r elbowCtrl_to_wristCtrl_wrist_distLoc ;
select -r shouldJnt_to_wristCtrl_wrist_distLoc ;
select -r elbowCtrl_to_wristCtrl_wrist_distLoc ;
file -save;
// F:/maya/projects/TESTING/scenes/stretchy_joints_testing/02/stretchyJoints_midPointSnapping_test_005.ma // 
file -f -options "v=0;"  -ignoreVersion  -typ "mayaAscii" -o "F:/maya/projects/tinyPhx_isoShooter/scenes/pugRocket/anim/flyLoop/tpx_pugRocket_flyLoop_anim.ma";addRecentFile("F:/maya/projects/tinyPhx_isoShooter/scenes/pugRocket/anim/flyLoop/tpx_pugRocket_flyLoop_anim.ma", "mayaAscii");
closeAllNodeEditors;
closeHypershade;
optionVar -sv colorManagementColorPickerColorSpaceSelection "Rendering Space";
optionVar -iv colorManagementColorPickerColorMgtEnabled 1;
// Warning: file: F:/maya/projects/tinyPhx_isoShooter/scenes/pugRocket/rig/tp_isoShoot_pugRocket_rig.ma line 4974: You must either select the affected nodes or specify them on the command line. // 
// Warning: file: F:/maya/projects/tinyPhx_isoShooter/scenes/pugRocket/rig/tp_isoShoot_pugRocket_rig.ma line 4977: You must either select the affected nodes or specify them on the command line. // 
// Warning: file: F:/maya/projects/tinyPhx_isoShooter/scenes/pugRocket/rig/tp_isoShoot_pugRocket_rig.ma line 4980: You must either select the affected nodes or specify them on the command line. // 
// Warning: file: F:/maya/projects/tinyPhx_isoShooter/scenes/pugRocket/rig/tp_isoShoot_pugRocket_rig.ma line 4983: You must either select the affected nodes or specify them on the command line. // 
// Warning: line 1999: The default image may not be modified. Use the -i/image flag instead. // 
// Read 2 files in  0.93 seconds.
select -r tp_isoShoot_pugRocket_rig:rocket_COG_ctrl ;
selectKey -clear ;
selectKey -add -k rocket_COG_ctrl_rotateX ;
keyframe -animation keys -relative -valueChange (0 - 90) ;
// 1 // 
keyframe -animation keys -relative -valueChange (0 + 180) ;
// 1 // 
currentTime 1 ;
// Press the ESC key to stop playback.
currentTime 4 ;
currentTime 1 ;
selectKey -clear ;
// 1 // 
selectKey -clear ;
selectKey -add -k rocket_COG_ctrl_rotateX ;
keyframe -e -iub true -r -o over -vc -1.999663 -t 9 rocket_COG_ctrl_rotateX ;
keyframe -e -iub true -r -o over -vc -1.999663 -t 24 -t 30 rocket_COG_ctrl_rotateX ;
keyframe -e -iub true -r -o over -vc -1.999663 -t 1 rocket_COG_ctrl_rotateX ;
selectKey -clear ;
selectKey -add -k -t 1 rocket_COG_ctrl_rotateX ;
selectKey -tgl -k -t 30 rocket_COG_ctrl_rotateX ;
keyframe -animation keys -absolute -valueChange 0 ;
// 1 // 
selectKey -clear ;
selectKey -clear ;
selectKey -add -k -t 1 -t 30 rocket_COG_ctrl_rotateX ;
selectKey -clear ;
currentTime 1 ;
// Press the ESC key to stop playback.
currentTime 28 ;
file -f -save  -options "v=0;";
// F:/maya/projects/tinyPhx_isoShooter/scenes/pugRocket/anim/flyLoop/tpx_pugRocket_flyLoop_anim.ma // 
file -f -options "v=0;"  -ignoreVersion  -typ "mayaAscii" -o "F:/maya/projects/tinyPhx_isoShooter/scenes/pugRocket/anim/land/tpx_pugRocket_land_anim.ma";addRecentFile("F:/maya/projects/tinyPhx_isoShooter/scenes/pugRocket/anim/land/tpx_pugRocket_land_anim.ma", "mayaAscii");
closeAllNodeEditors;
closeHypershade;
optionVar -sv colorManagementColorPickerColorSpaceSelection "Rendering Space";
optionVar -iv colorManagementColorPickerColorMgtEnabled 1;
// Warning: file: F:/maya/projects/tinyPhx_isoShooter/scenes/pugRocket/rig/tp_isoShoot_pugRocket_rig.ma line 4974: You must either select the affected nodes or specify them on the command line. // 
// Warning: file: F:/maya/projects/tinyPhx_isoShooter/scenes/pugRocket/rig/tp_isoShoot_pugRocket_rig.ma line 4977: You must either select the affected nodes or specify them on the command line. // 
// Warning: file: F:/maya/projects/tinyPhx_isoShooter/scenes/pugRocket/rig/tp_isoShoot_pugRocket_rig.ma line 4980: You must either select the affected nodes or specify them on the command line. // 
// Warning: file: F:/maya/projects/tinyPhx_isoShooter/scenes/pugRocket/rig/tp_isoShoot_pugRocket_rig.ma line 4983: You must either select the affected nodes or specify them on the command line. // 
// Warning: line 2004: The default image may not be modified. Use the -i/image flag instead. // 
// Read 2 files in  0.26 seconds.
currentTime 41 ;
currentTime 10 ;
select -r tp_isoShoot_pugRocket_rig:rocket_ROOT_ctrl ;
selectKey -clear ;
selectKey -add -k rocket_ROOT_ctrl_translateY ;
selectKey -clear ;
selectKey -add -k rocket_ROOT_ctrl_translateY ;
selectKey -clear ;
selectKey -add -k -t 1 rocket_ROOT_ctrl_translateY ;
selectKey -clear ;
selectKey -add -k -t "1:25" rocket_ROOT_ctrl_translateY ;
scaleKey -iub false -ts 1 -tp 49 -fs 1 -fp 49 -vs 0.06 -vp 0 -animation keys ;
currentTime 1 ;
// Press the ESC key to stop playback.
currentTime 45 ;
currentTime 1 ;
file -f -save  -options "v=0;";
// F:/maya/projects/tinyPhx_isoShooter/scenes/pugRocket/anim/land/tpx_pugRocket_land_anim.ma // 
file -f -options "v=0;"  -ignoreVersion  -typ "mayaAscii" -o "F:/maya/projects/tinyPhx_isoShooter/scenes/pugRocket/anim/takeOff/tpx_pugRocket_takeOff_anim.ma";addRecentFile("F:/maya/projects/tinyPhx_isoShooter/scenes/pugRocket/anim/takeOff/tpx_pugRocket_takeOff_anim.ma", "mayaAscii");
closeAllNodeEditors;
closeHypershade;
optionVar -sv colorManagementColorPickerColorSpaceSelection "Rendering Space";
optionVar -iv colorManagementColorPickerColorMgtEnabled 1;
// Warning: file: F:/maya/projects/tinyPhx_isoShooter/scenes/pugRocket/rig/tp_isoShoot_pugRocket_rig.ma line 4974: You must either select the affected nodes or specify them on the command line. // 
// Warning: file: F:/maya/projects/tinyPhx_isoShooter/scenes/pugRocket/rig/tp_isoShoot_pugRocket_rig.ma line 4977: You must either select the affected nodes or specify them on the command line. // 
// Warning: file: F:/maya/projects/tinyPhx_isoShooter/scenes/pugRocket/rig/tp_isoShoot_pugRocket_rig.ma line 4980: You must either select the affected nodes or specify them on the command line. // 
// Warning: file: F:/maya/projects/tinyPhx_isoShooter/scenes/pugRocket/rig/tp_isoShoot_pugRocket_rig.ma line 4983: You must either select the affected nodes or specify them on the command line. // 
// Warning: line 2004: The default image may not be modified. Use the -i/image flag instead. // 
// Read 2 files in  0.27 seconds.
currentTime 1 ;
select -r tp_isoShoot_pugRocket_rig:rocket_COG_ctrl ;
currentTime 1 ;
selectKey -clear ;
selectKey -add -k -t "27:40" rocket_COG_ctrl_translateY ;
selectKey -clear ;
selectKey -clear ;
selectKey -add -k -t "27:40" rocket_COG_ctrl_translateY ;
cutKey -animation keys -clear;
// 0 // 
selectKey -clear ;
selectKey -add -k -t 24 rocket_COG_ctrl_translateY ;
keyTangent -itt flat -ott flat;
// 1 // 
selectKey -clear ;
currentTime 1 ;
// Press the ESC key to stop playback.
currentTime 51 ;
currentTime 40 ;
currentTime 40 ;
currentTime 60 ;
if( `getAttr -k "tp_isoShoot_pugRocket_rig:rocket_COG_ctrl.ry"`||`getAttr -channelBox "tp_isoShoot_pugRocket_rig:rocket_COG_ctrl.ry"` )setKeyframe "tp_isoShoot_pugRocket_rig:rocket_COG_ctrl.ry";
// 1 // 
selectKey -clear ;
selectKey -add -k -t 60 rocket_COG_ctrl_rotateY ;
keyframe -e -iub true -r -o over -vc 227.039203 -t 60 rocket_COG_ctrl_rotateY ;
keyframe -e -iub true -r -o over -vc 61.996838 -t 60 rocket_COG_ctrl_rotateY ;
selectKey -clear ;
selectKey -add -k -t 40 rocket_COG_ctrl_rotateY ;
cutKey -animation keys -clear;
// 0 // 
selectKey -clear ;
selectKey -add -k -t 35 rocket_COG_ctrl_rotateY ;
selectKey -clear ;
selectKey -add -k -t 60 rocket_COG_ctrl_rotateY ;
currentTime 1 ;
// Press the ESC key to stop playback.
currentTime 112 ;
currentTime 1 ;
file -save;
// F:/maya/projects/tinyPhx_isoShooter/scenes/pugRocket/anim/takeOff/tpx_pugRocket_takeOff_anim.ma // 
file -f  -ignoreVersion  -typ "Fbx" -o "F:/maya/projects/tinyPhx_isoShooter/assets/pugRocket/anims/allTogether/02/pugRocket@allTogether.fbx";addRecentFile("F:/maya/projects/tinyPhx_isoShooter/assets/pugRocket/anims/allTogether/02/pugRocket@allTogether.fbx", "Fbx");
closeAllNodeEditors;
closeHypershade;
optionVar -sv colorManagementColorPickerColorSpaceSelection "Rendering Space";
optionVar -iv colorManagementColorPickerColorMgtEnabled 1;
// File read in  0.2 seconds.
// Logfile: "C:\Users\Wesley\Documents\maya\FBX\Logs\2016.1.2\maya2016imp.log"
setAttr -type "string" rocket_rig_grp|rocket_geo_grp|rocket_hull_geo|rocket_hull_geoShape.currentUVSet "map1";
setAttr -type "string" rocket_rig_grp|rocket_geo_grp|rocket_hatch_geo_grp|rocket_hatch01_geo|rocket_hatch01_geoShape.currentUVSet "map1";
setAttr -type "string" rocket_rig_grp|rocket_geo_grp|rocket_hatch_geo_grp|rocket_hatch02_geo|rocket_hatch02_geoShape.currentUVSet "map1";
setAttr -type "string" rocket_rig_grp|rocket_geo_grp|rocket_hatch_geo_grp|rocket_hatch03_geo|rocket_hatch03_geoShape.currentUVSet "map1";
setAttr -type "string" rocket_rig_grp|rocket_geo_grp|rocket_hatch_geo_grp|rocket_hatch04_geo|rocket_hatch04_geoShape.currentUVSet "map1";
setAttr -type "string" rocket_rig_grp|rocket_geo_grp|rocket_hatch_geo_grp|rocket_hatch05_geo|rocket_hatch05_geoShape.currentUVSet "map1";
setAttr -type "string" rocket_rig_grp|rocket_geo_grp|rocket_hatch_geo_grp|rocket_hatch06_geo|rocket_hatch06_geoShape.currentUVSet "map1";
setAttr -type "string" rocket_rig_grp|rocket_geo_grp|rocket_jewel_geo_grp|rocket_jewel01_geo|rocket_jewel01_geoShape.currentUVSet "map1";
setAttr -type "string" rocket_rig_grp|rocket_geo_grp|rocket_jewel_geo_grp|rocket_jewel02_geo|rocket_jewel02_geoShape.currentUVSet "map1";
setAttr -type "string" rocket_rig_grp|rocket_geo_grp|rocket_jewel_geo_grp|rocket_jewel03_geo|rocket_jewel03_geoShape.currentUVSet "map1";
setAttr -type "string" rocket_rig_grp|rocket_geo_grp|rocket_jewel_geo_grp|rocket_jewel04_geo|rocket_jewel04_geoShape.currentUVSet "map1";
setAttr -type "string" rocket_rig_grp|rocket_geo_grp|rocket_jewel_geo_grp|rocket_jewel05_geo|rocket_jewel05_geoShape.currentUVSet "map1";
setAttr -type "string" rocket_rig_grp|rocket_geo_grp|rocket_jewel_geo_grp|rocket_jewel06_geo|rocket_jewel06_geoShape.currentUVSet "map1";
setAttr -type "string" rocket_rig_grp|rocket_geo_grp|rocket_fin_geo_grp|rocket_fin01_geo|rocket_fin01_geoShape.currentUVSet "map1";
setAttr -type "string" rocket_rig_grp|rocket_geo_grp|rocket_fin_geo_grp|rocket_fin02_geo|rocket_fin02_geoShape.currentUVSet "map1";
setAttr -type "string" rocket_rig_grp|rocket_geo_grp|rocket_fin_geo_grp|rocket_fin03_geo|rocket_fin03_geoShape.currentUVSet "map1";
setAttr -type "string" rocket_rig_grp|rocket_geo_grp|exhaust_geo_grp|exhaust_out_geo|exhaust_out_geoShape.currentUVSet "map1";
setAttr -type "string" rocket_rig_grp|rocket_geo_grp|exhaust_geo_grp|exhaust_in_geo|exhaust_in_geoShape.currentUVSet "map1";
setAttr -type "string" rocket_rig_grp|rocket_geo_grp|rocket_dome_geo|rocket_dome_geoShape.currentUVSet "map1";
currentTime 1 ;
currentTime 1 ;
playbackOptions -min 1 -max 198 ;
currentTime 1 ;
// Press the ESC key to stop playback.
currentTime 98 ;
file -f  -ignoreVersion  -typ "Fbx" -o "F:/maya/projects/tinyPhx_isoShooter/assets/pugRocket/anims/allTogether/02/pugRocket@allTogether.fbx";addRecentFile("F:/maya/projects/tinyPhx_isoShooter/assets/pugRocket/anims/allTogether/02/pugRocket@allTogether.fbx", "Fbx");
closeAllNodeEditors;
closeHypershade;
optionVar -sv colorManagementColorPickerColorSpaceSelection "Rendering Space";
optionVar -iv colorManagementColorPickerColorMgtEnabled 1;
// File read in  0.091 seconds.
// Logfile: "C:\Users\Wesley\Documents\maya\FBX\Logs\2016.1.2\maya2016imp.log"
setAttr -type "string" rocket_rig_grp|rocket_geo_grp|rocket_hull_geo|rocket_hull_geoShape.currentUVSet "map1";
setAttr -type "string" rocket_rig_grp|rocket_geo_grp|rocket_hatch_geo_grp|rocket_hatch01_geo|rocket_hatch01_geoShape.currentUVSet "map1";
setAttr -type "string" rocket_rig_grp|rocket_geo_grp|rocket_hatch_geo_grp|rocket_hatch02_geo|rocket_hatch02_geoShape.currentUVSet "map1";
setAttr -type "string" rocket_rig_grp|rocket_geo_grp|rocket_hatch_geo_grp|rocket_hatch03_geo|rocket_hatch03_geoShape.currentUVSet "map1";
setAttr -type "string" rocket_rig_grp|rocket_geo_grp|rocket_hatch_geo_grp|rocket_hatch04_geo|rocket_hatch04_geoShape.currentUVSet "map1";
setAttr -type "string" rocket_rig_grp|rocket_geo_grp|rocket_hatch_geo_grp|rocket_hatch05_geo|rocket_hatch05_geoShape.currentUVSet "map1";
setAttr -type "string" rocket_rig_grp|rocket_geo_grp|rocket_hatch_geo_grp|rocket_hatch06_geo|rocket_hatch06_geoShape.currentUVSet "map1";
setAttr -type "string" rocket_rig_grp|rocket_geo_grp|rocket_jewel_geo_grp|rocket_jewel01_geo|rocket_jewel01_geoShape.currentUVSet "map1";
setAttr -type "string" rocket_rig_grp|rocket_geo_grp|rocket_jewel_geo_grp|rocket_jewel02_geo|rocket_jewel02_geoShape.currentUVSet "map1";
setAttr -type "string" rocket_rig_grp|rocket_geo_grp|rocket_jewel_geo_grp|rocket_jewel03_geo|rocket_jewel03_geoShape.currentUVSet "map1";
setAttr -type "string" rocket_rig_grp|rocket_geo_grp|rocket_jewel_geo_grp|rocket_jewel04_geo|rocket_jewel04_geoShape.currentUVSet "map1";
setAttr -type "string" rocket_rig_grp|rocket_geo_grp|rocket_jewel_geo_grp|rocket_jewel05_geo|rocket_jewel05_geoShape.currentUVSet "map1";
setAttr -type "string" rocket_rig_grp|rocket_geo_grp|rocket_jewel_geo_grp|rocket_jewel06_geo|rocket_jewel06_geoShape.currentUVSet "map1";
setAttr -type "string" rocket_rig_grp|rocket_geo_grp|rocket_fin_geo_grp|rocket_fin01_geo|rocket_fin01_geoShape.currentUVSet "map1";
setAttr -type "string" rocket_rig_grp|rocket_geo_grp|rocket_fin_geo_grp|rocket_fin02_geo|rocket_fin02_geoShape.currentUVSet "map1";
setAttr -type "string" rocket_rig_grp|rocket_geo_grp|rocket_fin_geo_grp|rocket_fin03_geo|rocket_fin03_geoShape.currentUVSet "map1";
setAttr -type "string" rocket_rig_grp|rocket_geo_grp|exhaust_geo_grp|exhaust_out_geo|exhaust_out_geoShape.currentUVSet "map1";
setAttr -type "string" rocket_rig_grp|rocket_geo_grp|exhaust_geo_grp|exhaust_in_geo|exhaust_in_geoShape.currentUVSet "map1";
setAttr -type "string" rocket_rig_grp|rocket_geo_grp|rocket_dome_geo|rocket_dome_geoShape.currentUVSet "map1";
currentTime 1 ;
currentTime 38 ;
currentTime 1 ;
currentTime 39 ;
// Press the ESC key to stop playback.
currentTime 13 ;
currentTime 38 ;
// Press the ESC key to stop playback.
currentTime 4 ;
currentTime 1 ;
playbackOptions -min 1 -max 200 ;
currentTime 40 ;
currentTime 40 ;
currentTime 71 ;
currentTime 70 ;
currentTime 70 ;
currentTime 69 ;
currentTime 40 ;
// Press the ESC key to stop playback.
currentTime 63 ;
currentTime 40 ;
currentTime 89 ;
currentTime 71 ;
currentTime 71 ;
currentTime 119 ;
currentTime 107 ;
currentTime 120 ;
currentTime 117 ;
currentTime 71 ;
// Press the ESC key to stop playback.
currentTime 76 ;
playbackOptions -min 120 -max 169 ;
currentTime 121 ;
currentTime 120 ;
currentTime 121 ;
currentTime 159 ;
currentTime 163 ;
currentTime 160 ;
currentTime 160 ;
currentTime 121 ;
file -f -options "v=0;"  -ignoreVersion  -typ "mayaAscii" -o "F:/maya/projects/tinyPhx_isoShooter/scenes/pugRocket/anim/exit/tpx_pugRocket_exit_anim.ma";addRecentFile("F:/maya/projects/tinyPhx_isoShooter/scenes/pugRocket/anim/exit/tpx_pugRocket_exit_anim.ma", "mayaAscii");
closeAllNodeEditors;
closeHypershade;
optionVar -sv colorManagementColorPickerColorSpaceSelection "Rendering Space";
optionVar -iv colorManagementColorPickerColorMgtEnabled 1;
// Warning: file: F:/maya/projects/tinyPhx_isoShooter/scenes/pugRocket/rig/tp_isoShoot_pugRocket_rig.ma line 4974: You must either select the affected nodes or specify them on the command line. // 
// Warning: file: F:/maya/projects/tinyPhx_isoShooter/scenes/pugRocket/rig/tp_isoShoot_pugRocket_rig.ma line 4977: You must either select the affected nodes or specify them on the command line. // 
// Warning: file: F:/maya/projects/tinyPhx_isoShooter/scenes/pugRocket/rig/tp_isoShoot_pugRocket_rig.ma line 4980: You must either select the affected nodes or specify them on the command line. // 
// Warning: file: F:/maya/projects/tinyPhx_isoShooter/scenes/pugRocket/rig/tp_isoShoot_pugRocket_rig.ma line 4983: You must either select the affected nodes or specify them on the command line. // 
// Warning: line 1997: The default image may not be modified. Use the -i/image flag instead. // 
// Read 2 files in  0.27 seconds.
currentTime 1 ;
select -r tp_isoShoot_pugRocket_rig:rocket_main01_ctrl tp_isoShoot_pugRocket_rig:rocket_main02_ctrl tp_isoShoot_pugRocket_rig:rocket_main03_ctrl tp_isoShoot_pugRocket_rig:rocket_main04_ctrl tp_isoShoot_pugRocket_rig:rocket_ROOT_ctrl tp_isoShoot_pugRocket_rig:rocket_COG_ctrl ;
currentTime 1 ;
select -cl  ;
setObjectPickMask "Marker" false;
setObjectPickMask "Joint" false;
setObjectPickMask "Surface" false;
setObjectPickMask "Deformer" false;
setObjectPickMask "Dynamic" false;
setObjectPickMask "Rendering" false;
setObjectPickMask "Other" false;
select -r tp_isoShoot_pugRocket_rig:rocket_main01_ctrl tp_isoShoot_pugRocket_rig:rocket_main02_ctrl tp_isoShoot_pugRocket_rig:rocket_main03_ctrl tp_isoShoot_pugRocket_rig:rocket_main04_ctrl tp_isoShoot_pugRocket_rig:rocket_ROOT_ctrl tp_isoShoot_pugRocket_rig:rocket_COG_ctrl ;
currentTime 39 ;
currentTime 40 ;
currentTime 1 ;
currentTime 39 ;
currentTime 1 ;
// Press the ESC key to stop playback.
currentTime 11 ;
file -f -options "v=0;"  -ignoreVersion  -typ "mayaAscii" -o "F:/maya/projects/tinyPhx_isoShooter/scenes/pugRocket/anim/flyLoop/tpx_pugRocket_flyLoop_anim.ma";addRecentFile("F:/maya/projects/tinyPhx_isoShooter/scenes/pugRocket/anim/flyLoop/tpx_pugRocket_flyLoop_anim.ma", "mayaAscii");
closeAllNodeEditors;
closeHypershade;
optionVar -sv colorManagementColorPickerColorSpaceSelection "Rendering Space";
optionVar -iv colorManagementColorPickerColorMgtEnabled 1;
// Warning: file: F:/maya/projects/tinyPhx_isoShooter/scenes/pugRocket/rig/tp_isoShoot_pugRocket_rig.ma line 4974: You must either select the affected nodes or specify them on the command line. // 
// Warning: file: F:/maya/projects/tinyPhx_isoShooter/scenes/pugRocket/rig/tp_isoShoot_pugRocket_rig.ma line 4977: You must either select the affected nodes or specify them on the command line. // 
// Warning: file: F:/maya/projects/tinyPhx_isoShooter/scenes/pugRocket/rig/tp_isoShoot_pugRocket_rig.ma line 4980: You must either select the affected nodes or specify them on the command line. // 
// Warning: file: F:/maya/projects/tinyPhx_isoShooter/scenes/pugRocket/rig/tp_isoShoot_pugRocket_rig.ma line 4983: You must either select the affected nodes or specify them on the command line. // 
// Warning: line 2002: The default image may not be modified. Use the -i/image flag instead. // 
// Read 2 files in  0.26 seconds.
currentTime 30 ;
select -r tp_isoShoot_pugRocket_rig:rocket_main01_ctrl tp_isoShoot_pugRocket_rig:rocket_main02_ctrl tp_isoShoot_pugRocket_rig:rocket_main03_ctrl tp_isoShoot_pugRocket_rig:rocket_main04_ctrl tp_isoShoot_pugRocket_rig:rocket_ROOT_ctrl tp_isoShoot_pugRocket_rig:rocket_COG_ctrl ;
setObjectPickMask "Marker" false;
setObjectPickMask "Joint" false;
setObjectPickMask "Surface" false;
setObjectPickMask "Deformer" false;
setObjectPickMask "Dynamic" false;
setObjectPickMask "Rendering" false;
setObjectPickMask "Other" false;
select -cl  ;
select -r tp_isoShoot_pugRocket_rig:rocket_main01_ctrl tp_isoShoot_pugRocket_rig:rocket_main02_ctrl tp_isoShoot_pugRocket_rig:rocket_main03_ctrl tp_isoShoot_pugRocket_rig:rocket_main04_ctrl tp_isoShoot_pugRocket_rig:rocket_ROOT_ctrl tp_isoShoot_pugRocket_rig:rocket_COG_ctrl ;
currentTime 1 ;
// Press the ESC key to stop playback.
currentTime 4 ;
currentTime 31 ;
currentTime 30 ;
if( `getAttr -k "tp_isoShoot_pugRocket_rig:rocket_COG_ctrl.tx"`||`getAttr -channelBox "tp_isoShoot_pugRocket_rig:rocket_COG_ctrl.tx"` )setKeyframe "tp_isoShoot_pugRocket_rig:rocket_COG_ctrl.tx";
if( `getAttr -k "tp_isoShoot_pugRocket_rig:rocket_main01_ctrl.tx"`||`getAttr -channelBox "tp_isoShoot_pugRocket_rig:rocket_main01_ctrl.tx"` )setKeyframe "tp_isoShoot_pugRocket_rig:rocket_main01_ctrl.tx";
if( `getAttr -k "tp_isoShoot_pugRocket_rig:rocket_main02_ctrl.tx"`||`getAttr -channelBox "tp_isoShoot_pugRocket_rig:rocket_main02_ctrl.tx"` )setKeyframe "tp_isoShoot_pugRocket_rig:rocket_main02_ctrl.tx";
if( `getAttr -k "tp_isoShoot_pugRocket_rig:rocket_main03_ctrl.tx"`||`getAttr -channelBox "tp_isoShoot_pugRocket_rig:rocket_main03_ctrl.tx"` )setKeyframe "tp_isoShoot_pugRocket_rig:rocket_main03_ctrl.tx";
if( `getAttr -k "tp_isoShoot_pugRocket_rig:rocket_main04_ctrl.tx"`||`getAttr -channelBox "tp_isoShoot_pugRocket_rig:rocket_main04_ctrl.tx"` )setKeyframe "tp_isoShoot_pugRocket_rig:rocket_main04_ctrl.tx";
if( `getAttr -k "tp_isoShoot_pugRocket_rig:rocket_ROOT_ctrl.tx"`||`getAttr -channelBox "tp_isoShoot_pugRocket_rig:rocket_ROOT_ctrl.tx"` )setKeyframe "tp_isoShoot_pugRocket_rig:rocket_ROOT_ctrl.tx";
if( `getAttr -k "tp_isoShoot_pugRocket_rig:rocket_COG_ctrl.ty"`||`getAttr -channelBox "tp_isoShoot_pugRocket_rig:rocket_COG_ctrl.ty"` )setKeyframe "tp_isoShoot_pugRocket_rig:rocket_COG_ctrl.ty";
if( `getAttr -k "tp_isoShoot_pugRocket_rig:rocket_main01_ctrl.ty"`||`getAttr -channelBox "tp_isoShoot_pugRocket_rig:rocket_main01_ctrl.ty"` )setKeyframe "tp_isoShoot_pugRocket_rig:rocket_main01_ctrl.ty";
if( `getAttr -k "tp_isoShoot_pugRocket_rig:rocket_main02_ctrl.ty"`||`getAttr -channelBox "tp_isoShoot_pugRocket_rig:rocket_main02_ctrl.ty"` )setKeyframe "tp_isoShoot_pugRocket_rig:rocket_main02_ctrl.ty";
if( `getAttr -k "tp_isoShoot_pugRocket_rig:rocket_main03_ctrl.ty"`||`getAttr -channelBox "tp_isoShoot_pugRocket_rig:rocket_main03_ctrl.ty"` )setKeyframe "tp_isoShoot_pugRocket_rig:rocket_main03_ctrl.ty";
if( `getAttr -k "tp_isoShoot_pugRocket_rig:rocket_main04_ctrl.ty"`||`getAttr -channelBox "tp_isoShoot_pugRocket_rig:rocket_main04_ctrl.ty"` )setKeyframe "tp_isoShoot_pugRocket_rig:rocket_main04_ctrl.ty";
if( `getAttr -k "tp_isoShoot_pugRocket_rig:rocket_ROOT_ctrl.ty"`||`getAttr -channelBox "tp_isoShoot_pugRocket_rig:rocket_ROOT_ctrl.ty"` )setKeyframe "tp_isoShoot_pugRocket_rig:rocket_ROOT_ctrl.ty";
if( `getAttr -k "tp_isoShoot_pugRocket_rig:rocket_COG_ctrl.tz"`||`getAttr -channelBox "tp_isoShoot_pugRocket_rig:rocket_COG_ctrl.tz"` )setKeyframe "tp_isoShoot_pugRocket_rig:rocket_COG_ctrl.tz";
if( `getAttr -k "tp_isoShoot_pugRocket_rig:rocket_main01_ctrl.tz"`||`getAttr -channelBox "tp_isoShoot_pugRocket_rig:rocket_main01_ctrl.tz"` )setKeyframe "tp_isoShoot_pugRocket_rig:rocket_main01_ctrl.tz";
if( `getAttr -k "tp_isoShoot_pugRocket_rig:rocket_main02_ctrl.tz"`||`getAttr -channelBox "tp_isoShoot_pugRocket_rig:rocket_main02_ctrl.tz"` )setKeyframe "tp_isoShoot_pugRocket_rig:rocket_main02_ctrl.tz";
if( `getAttr -k "tp_isoShoot_pugRocket_rig:rocket_main03_ctrl.tz"`||`getAttr -channelBox "tp_isoShoot_pugRocket_rig:rocket_main03_ctrl.tz"` )setKeyframe "tp_isoShoot_pugRocket_rig:rocket_main03_ctrl.tz";
if( `getAttr -k "tp_isoShoot_pugRocket_rig:rocket_main04_ctrl.tz"`||`getAttr -channelBox "tp_isoShoot_pugRocket_rig:rocket_main04_ctrl.tz"` )setKeyframe "tp_isoShoot_pugRocket_rig:rocket_main04_ctrl.tz";
if( `getAttr -k "tp_isoShoot_pugRocket_rig:rocket_ROOT_ctrl.tz"`||`getAttr -channelBox "tp_isoShoot_pugRocket_rig:rocket_ROOT_ctrl.tz"` )setKeyframe "tp_isoShoot_pugRocket_rig:rocket_ROOT_ctrl.tz";
if( `getAttr -k "tp_isoShoot_pugRocket_rig:rocket_COG_ctrl.rx"`||`getAttr -channelBox "tp_isoShoot_pugRocket_rig:rocket_COG_ctrl.rx"` )setKeyframe "tp_isoShoot_pugRocket_rig:rocket_COG_ctrl.rx";
if( `getAttr -k "tp_isoShoot_pugRocket_rig:rocket_main01_ctrl.rx"`||`getAttr -channelBox "tp_isoShoot_pugRocket_rig:rocket_main01_ctrl.rx"` )setKeyframe "tp_isoShoot_pugRocket_rig:rocket_main01_ctrl.rx";
if( `getAttr -k "tp_isoShoot_pugRocket_rig:rocket_main02_ctrl.rx"`||`getAttr -channelBox "tp_isoShoot_pugRocket_rig:rocket_main02_ctrl.rx"` )setKeyframe "tp_isoShoot_pugRocket_rig:rocket_main02_ctrl.rx";
if( `getAttr -k "tp_isoShoot_pugRocket_rig:rocket_main03_ctrl.rx"`||`getAttr -channelBox "tp_isoShoot_pugRocket_rig:rocket_main03_ctrl.rx"` )setKeyframe "tp_isoShoot_pugRocket_rig:rocket_main03_ctrl.rx";
if( `getAttr -k "tp_isoShoot_pugRocket_rig:rocket_main04_ctrl.rx"`||`getAttr -channelBox "tp_isoShoot_pugRocket_rig:rocket_main04_ctrl.rx"` )setKeyframe "tp_isoShoot_pugRocket_rig:rocket_main04_ctrl.rx";
if( `getAttr -k "tp_isoShoot_pugRocket_rig:rocket_ROOT_ctrl.rx"`||`getAttr -channelBox "tp_isoShoot_pugRocket_rig:rocket_ROOT_ctrl.rx"` )setKeyframe "tp_isoShoot_pugRocket_rig:rocket_ROOT_ctrl.rx";
if( `getAttr -k "tp_isoShoot_pugRocket_rig:rocket_COG_ctrl.ry"`||`getAttr -channelBox "tp_isoShoot_pugRocket_rig:rocket_COG_ctrl.ry"` )setKeyframe "tp_isoShoot_pugRocket_rig:rocket_COG_ctrl.ry";
if( `getAttr -k "tp_isoShoot_pugRocket_rig:rocket_main01_ctrl.ry"`||`getAttr -channelBox "tp_isoShoot_pugRocket_rig:rocket_main01_ctrl.ry"` )setKeyframe "tp_isoShoot_pugRocket_rig:rocket_main01_ctrl.ry";
if( `getAttr -k "tp_isoShoot_pugRocket_rig:rocket_main02_ctrl.ry"`||`getAttr -channelBox "tp_isoShoot_pugRocket_rig:rocket_main02_ctrl.ry"` )setKeyframe "tp_isoShoot_pugRocket_rig:rocket_main02_ctrl.ry";
if( `getAttr -k "tp_isoShoot_pugRocket_rig:rocket_main03_ctrl.ry"`||`getAttr -channelBox "tp_isoShoot_pugRocket_rig:rocket_main03_ctrl.ry"` )setKeyframe "tp_isoShoot_pugRocket_rig:rocket_main03_ctrl.ry";
if( `getAttr -k "tp_isoShoot_pugRocket_rig:rocket_main04_ctrl.ry"`||`getAttr -channelBox "tp_isoShoot_pugRocket_rig:rocket_main04_ctrl.ry"` )setKeyframe "tp_isoShoot_pugRocket_rig:rocket_main04_ctrl.ry";
if( `getAttr -k "tp_isoShoot_pugRocket_rig:rocket_ROOT_ctrl.ry"`||`getAttr -channelBox "tp_isoShoot_pugRocket_rig:rocket_ROOT_ctrl.ry"` )setKeyframe "tp_isoShoot_pugRocket_rig:rocket_ROOT_ctrl.ry";
if( `getAttr -k "tp_isoShoot_pugRocket_rig:rocket_COG_ctrl.rz"`||`getAttr -channelBox "tp_isoShoot_pugRocket_rig:rocket_COG_ctrl.rz"` )setKeyframe "tp_isoShoot_pugRocket_rig:rocket_COG_ctrl.rz";
if( `getAttr -k "tp_isoShoot_pugRocket_rig:rocket_main01_ctrl.rz"`||`getAttr -channelBox "tp_isoShoot_pugRocket_rig:rocket_main01_ctrl.rz"` )setKeyframe "tp_isoShoot_pugRocket_rig:rocket_main01_ctrl.rz";
if( `getAttr -k "tp_isoShoot_pugRocket_rig:rocket_main02_ctrl.rz"`||`getAttr -channelBox "tp_isoShoot_pugRocket_rig:rocket_main02_ctrl.rz"` )setKeyframe "tp_isoShoot_pugRocket_rig:rocket_main02_ctrl.rz";
if( `getAttr -k "tp_isoShoot_pugRocket_rig:rocket_main03_ctrl.rz"`||`getAttr -channelBox "tp_isoShoot_pugRocket_rig:rocket_main03_ctrl.rz"` )setKeyframe "tp_isoShoot_pugRocket_rig:rocket_main03_ctrl.rz";
if( `getAttr -k "tp_isoShoot_pugRocket_rig:rocket_main04_ctrl.rz"`||`getAttr -channelBox "tp_isoShoot_pugRocket_rig:rocket_main04_ctrl.rz"` )setKeyframe "tp_isoShoot_pugRocket_rig:rocket_main04_ctrl.rz";
if( `getAttr -k "tp_isoShoot_pugRocket_rig:rocket_ROOT_ctrl.rz"`||`getAttr -channelBox "tp_isoShoot_pugRocket_rig:rocket_ROOT_ctrl.rz"` )setKeyframe "tp_isoShoot_pugRocket_rig:rocket_ROOT_ctrl.rz";
if( `getAttr -k "tp_isoShoot_pugRocket_rig:rocket_COG_ctrl.sx"`||`getAttr -channelBox "tp_isoShoot_pugRocket_rig:rocket_COG_ctrl.sx"` )setKeyframe "tp_isoShoot_pugRocket_rig:rocket_COG_ctrl.sx";
if( `getAttr -k "tp_isoShoot_pugRocket_rig:rocket_main01_ctrl.sx"`||`getAttr -channelBox "tp_isoShoot_pugRocket_rig:rocket_main01_ctrl.sx"` )setKeyframe "tp_isoShoot_pugRocket_rig:rocket_main01_ctrl.sx";
if( `getAttr -k "tp_isoShoot_pugRocket_rig:rocket_main02_ctrl.sx"`||`getAttr -channelBox "tp_isoShoot_pugRocket_rig:rocket_main02_ctrl.sx"` )setKeyframe "tp_isoShoot_pugRocket_rig:rocket_main02_ctrl.sx";
if( `getAttr -k "tp_isoShoot_pugRocket_rig:rocket_main03_ctrl.sx"`||`getAttr -channelBox "tp_isoShoot_pugRocket_rig:rocket_main03_ctrl.sx"` )setKeyframe "tp_isoShoot_pugRocket_rig:rocket_main03_ctrl.sx";
if( `getAttr -k "tp_isoShoot_pugRocket_rig:rocket_main04_ctrl.sx"`||`getAttr -channelBox "tp_isoShoot_pugRocket_rig:rocket_main04_ctrl.sx"` )setKeyframe "tp_isoShoot_pugRocket_rig:rocket_main04_ctrl.sx";
if( `getAttr -k "tp_isoShoot_pugRocket_rig:rocket_ROOT_ctrl.sx"`||`getAttr -channelBox "tp_isoShoot_pugRocket_rig:rocket_ROOT_ctrl.sx"` )setKeyframe "tp_isoShoot_pugRocket_rig:rocket_ROOT_ctrl.sx";
if( `getAttr -k "tp_isoShoot_pugRocket_rig:rocket_COG_ctrl.sy"`||`getAttr -channelBox "tp_isoShoot_pugRocket_rig:rocket_COG_ctrl.sy"` )setKeyframe "tp_isoShoot_pugRocket_rig:rocket_COG_ctrl.sy";
if( `getAttr -k "tp_isoShoot_pugRocket_rig:rocket_main01_ctrl.sy"`||`getAttr -channelBox "tp_isoShoot_pugRocket_rig:rocket_main01_ctrl.sy"` )setKeyframe "tp_isoShoot_pugRocket_rig:rocket_main01_ctrl.sy";
if( `getAttr -k "tp_isoShoot_pugRocket_rig:rocket_main02_ctrl.sy"`||`getAttr -channelBox "tp_isoShoot_pugRocket_rig:rocket_main02_ctrl.sy"` )setKeyframe "tp_isoShoot_pugRocket_rig:rocket_main02_ctrl.sy";
if( `getAttr -k "tp_isoShoot_pugRocket_rig:rocket_main03_ctrl.sy"`||`getAttr -channelBox "tp_isoShoot_pugRocket_rig:rocket_main03_ctrl.sy"` )setKeyframe "tp_isoShoot_pugRocket_rig:rocket_main03_ctrl.sy";
if( `getAttr -k "tp_isoShoot_pugRocket_rig:rocket_main04_ctrl.sy"`||`getAttr -channelBox "tp_isoShoot_pugRocket_rig:rocket_main04_ctrl.sy"` )setKeyframe "tp_isoShoot_pugRocket_rig:rocket_main04_ctrl.sy";
if( `getAttr -k "tp_isoShoot_pugRocket_rig:rocket_ROOT_ctrl.sy"`||`getAttr -channelBox "tp_isoShoot_pugRocket_rig:rocket_ROOT_ctrl.sy"` )setKeyframe "tp_isoShoot_pugRocket_rig:rocket_ROOT_ctrl.sy";
if( `getAttr -k "tp_isoShoot_pugRocket_rig:rocket_COG_ctrl.sz"`||`getAttr -channelBox "tp_isoShoot_pugRocket_rig:rocket_COG_ctrl.sz"` )setKeyframe "tp_isoShoot_pugRocket_rig:rocket_COG_ctrl.sz";
if( `getAttr -k "tp_isoShoot_pugRocket_rig:rocket_main01_ctrl.sz"`||`getAttr -channelBox "tp_isoShoot_pugRocket_rig:rocket_main01_ctrl.sz"` )setKeyframe "tp_isoShoot_pugRocket_rig:rocket_main01_ctrl.sz";
if( `getAttr -k "tp_isoShoot_pugRocket_rig:rocket_main02_ctrl.sz"`||`getAttr -channelBox "tp_isoShoot_pugRocket_rig:rocket_main02_ctrl.sz"` )setKeyframe "tp_isoShoot_pugRocket_rig:rocket_main02_ctrl.sz";
if( `getAttr -k "tp_isoShoot_pugRocket_rig:rocket_main03_ctrl.sz"`||`getAttr -channelBox "tp_isoShoot_pugRocket_rig:rocket_main03_ctrl.sz"` )setKeyframe "tp_isoShoot_pugRocket_rig:rocket_main03_ctrl.sz";
if( `getAttr -k "tp_isoShoot_pugRocket_rig:rocket_main04_ctrl.sz"`||`getAttr -channelBox "tp_isoShoot_pugRocket_rig:rocket_main04_ctrl.sz"` )setKeyframe "tp_isoShoot_pugRocket_rig:rocket_main04_ctrl.sz";
if( `getAttr -k "tp_isoShoot_pugRocket_rig:rocket_ROOT_ctrl.sz"`||`getAttr -channelBox "tp_isoShoot_pugRocket_rig:rocket_ROOT_ctrl.sz"` )setKeyframe "tp_isoShoot_pugRocket_rig:rocket_ROOT_ctrl.sz";
// 1 // 
currentTime 31 ;
selectKey -clear ;
selectKey -add -k -t 31 rocket_ROOT_ctrl_scaleX ;
selectKey -add -k -t 31 rocket_ROOT_ctrl_scaleY ;
selectKey -add -k -t 31 rocket_ROOT_ctrl_scaleZ ;
selectKey -add -k -t 31 rocket_ROOT_ctrl_translateX ;
selectKey -add -k -t 31 rocket_ROOT_ctrl_translateY ;
selectKey -add -k -t 31 rocket_ROOT_ctrl_translateZ ;
selectKey -add -k -t 31 rocket_ROOT_ctrl_rotateX ;
selectKey -add -k -t 31 rocket_ROOT_ctrl_rotateY ;
selectKey -add -k -t 31 rocket_ROOT_ctrl_rotateZ ;
cutKey -animation keys -clear;
// 0 // 
currentTime 1 ;
file -save;
// F:/maya/projects/tinyPhx_isoShooter/scenes/pugRocket/anim/flyLoop/tpx_pugRocket_flyLoop_anim.ma // 
currentTime 30 ;
currentTime 1 ;
file -save;
// F:/maya/projects/tinyPhx_isoShooter/scenes/pugRocket/anim/flyLoop/tpx_pugRocket_flyLoop_anim.ma // 
file -f -options "v=0;"  -ignoreVersion  -typ "mayaAscii" -o "F:/maya/projects/tinyPhx_isoShooter/scenes/pugRocket/anim/land/tpx_pugRocket_land_anim.ma";addRecentFile("F:/maya/projects/tinyPhx_isoShooter/scenes/pugRocket/anim/land/tpx_pugRocket_land_anim.ma", "mayaAscii");
closeAllNodeEditors;
closeHypershade;
optionVar -sv colorManagementColorPickerColorSpaceSelection "Rendering Space";
optionVar -iv colorManagementColorPickerColorMgtEnabled 1;
// Warning: file: F:/maya/projects/tinyPhx_isoShooter/scenes/pugRocket/rig/tp_isoShoot_pugRocket_rig.ma line 4974: You must either select the affected nodes or specify them on the command line. // 
// Warning: file: F:/maya/projects/tinyPhx_isoShooter/scenes/pugRocket/rig/tp_isoShoot_pugRocket_rig.ma line 4977: You must either select the affected nodes or specify them on the command line. // 
// Warning: file: F:/maya/projects/tinyPhx_isoShooter/scenes/pugRocket/rig/tp_isoShoot_pugRocket_rig.ma line 4980: You must either select the affected nodes or specify them on the command line. // 
// Warning: file: F:/maya/projects/tinyPhx_isoShooter/scenes/pugRocket/rig/tp_isoShoot_pugRocket_rig.ma line 4983: You must either select the affected nodes or specify them on the command line. // 
// Warning: line 2007: The default image may not be modified. Use the -i/image flag instead. // 
// Read 2 files in  0.24 seconds.
currentTime 1 ;
setObjectPickMask "Marker" false;
setObjectPickMask "Joint" false;
setObjectPickMask "Surface" false;
setObjectPickMask "Deformer" false;
setObjectPickMask "Dynamic" false;
setObjectPickMask "Rendering" false;
setObjectPickMask "Other" false;
select -r tp_isoShoot_pugRocket_rig:rocket_main01_ctrl tp_isoShoot_pugRocket_rig:rocket_main02_ctrl tp_isoShoot_pugRocket_rig:rocket_main03_ctrl tp_isoShoot_pugRocket_rig:rocket_main04_ctrl tp_isoShoot_pugRocket_rig:rocket_ROOT_ctrl tp_isoShoot_pugRocket_rig:rocket_COG_ctrl ;
currentTime 49 ;
currentTime 49 ;
currentTime 49 ;
file -save;
// F:/maya/projects/tinyPhx_isoShooter/scenes/pugRocket/anim/land/tpx_pugRocket_land_anim.ma // 
select -cl  ;
file -f -options "v=0;"  -ignoreVersion  -typ "mayaAscii" -o "F:/maya/projects/tinyPhx_isoShooter/scenes/pugRocket/anim/takeOff/tpx_pugRocket_takeOff_anim.ma";addRecentFile("F:/maya/projects/tinyPhx_isoShooter/scenes/pugRocket/anim/takeOff/tpx_pugRocket_takeOff_anim.ma", "mayaAscii");
closeAllNodeEditors;
closeHypershade;
optionVar -sv colorManagementColorPickerColorSpaceSelection "Rendering Space";
optionVar -iv colorManagementColorPickerColorMgtEnabled 1;
// Warning: file: F:/maya/projects/tinyPhx_isoShooter/scenes/pugRocket/rig/tp_isoShoot_pugRocket_rig.ma line 4974: You must either select the affected nodes or specify them on the command line. // 
// Warning: file: F:/maya/projects/tinyPhx_isoShooter/scenes/pugRocket/rig/tp_isoShoot_pugRocket_rig.ma line 4977: You must either select the affected nodes or specify them on the command line. // 
// Warning: file: F:/maya/projects/tinyPhx_isoShooter/scenes/pugRocket/rig/tp_isoShoot_pugRocket_rig.ma line 4980: You must either select the affected nodes or specify them on the command line. // 
// Warning: file: F:/maya/projects/tinyPhx_isoShooter/scenes/pugRocket/rig/tp_isoShoot_pugRocket_rig.ma line 4983: You must either select the affected nodes or specify them on the command line. // 
// Warning: line 2007: The default image may not be modified. Use the -i/image flag instead. // 
// Read 2 files in  0.26 seconds.
setObjectPickMask "Marker" false;
setObjectPickMask "Joint" false;
setObjectPickMask "Surface" false;
setObjectPickMask "Deformer" false;
setObjectPickMask "Dynamic" false;
setObjectPickMask "Rendering" false;
setObjectPickMask "Other" false;
select -r tp_isoShoot_pugRocket_rig:rocket_main01_ctrl tp_isoShoot_pugRocket_rig:rocket_main02_ctrl tp_isoShoot_pugRocket_rig:rocket_main03_ctrl tp_isoShoot_pugRocket_rig:rocket_main04_ctrl tp_isoShoot_pugRocket_rig:rocket_ROOT_ctrl tp_isoShoot_pugRocket_rig:rocket_COG_ctrl ;
currentTime 60 ;
currentTime 60 ;
import maya.cmds as cmds

fakeAnim_A_start = 1
fakeAnim_A_end = 30
fakeAnim_B_start = 1
fakeAnim_B_end = 15

for i in range(len(2)):
    print i
# Error: TypeError: file <maya console> line 8: object of type 'int' has no len() # 
import maya.cmds as cmds

fakeAnim_A_start = 1
fakeAnim_A_end = 30
fakeAnim_B_start = 1
fakeAnim_B_end = 15

for i in range(2):
    print i
0
1
import maya.cmds as cmds

fakeAnim_A_start = 1
fakeAnim_A_end = 30
fakeAnim_B_start = 1
fakeAnim_B_end = 15

timeOffset = 1
totalLen = 0

for i in range(2):
    if i == 0:
        print "animA start time = " + timeOffset
        print "@ animA totalLen = " + totalLen
        totalLen += fakeAnim_A_end
        timeOffset = totalLen
    elif i == 1:
        print "animB start time = " + timeOffset
        print "@ animB totalLen = " + totalLen 
        
# Error: TypeError: file <maya console> line 13: cannot concatenate 'str' and 'int' objects # 
import maya.cmds as cmds

fakeAnim_A_start = 1
fakeAnim_A_end = 30
fakeAnim_B_start = 1
fakeAnim_B_end = 15

timeOffset = 1
totalLen = 0

for i in range(2):
    if i == 0:
        print "animA start time = %i" %timeOffset
        print "@ animA totalLen = %i" %totalLen
        totalLen += fakeAnim_A_end
        timeOffset = totalLen
    elif i == 1:
        print "animB start time = %i" %timeOffset
        print "@ animB totalLen = %i" %totalLen 
        
animA start time = 1
@ animA totalLen = 0
animB start time = 30
@ animB totalLen = 30
import maya.cmds as cmds

fakeAnim_A_start = 1
fakeAnim_A_end = 30
fakeAnim_B_start = 1
fakeAnim_B_end = 15

timeOffset = 1
totalLen = 0

for i in range(2):
    if i == 0:
        print "animA start time = %i" %timeOffset
        print "@ animA totalLen = %i" %totalLen
        totalLen += fakeAnim_A_end
        timeOffset = totalLen
    elif i == 1:
        print "animB start time = %i" %timeOffset
        print "@ animB totalLen = %i" %totalLen
        totalLen += fakeAnim_B_end
        timeOffset = totalLen
        
print "allTogether_anim totalLen = %i" %totalLen
        
animA start time = 1
@ animA totalLen = 0
animB start time = 30
@ animB totalLen = 30
allTogether_anim totalLen = 45
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
    #if a charcter is in the scene, then run the next line.  if not - then move to the prop tool.  run it with the approriate name
    ww_fbx_export_funcLib.ReorganizeCharacterHierarchy()
    ww_fbx_export_funcLib.ReorganizePropHierarchy('gun01')
    #ww_fbx_export_funcLib.ReorganizePropHierarchy('rocket')
    
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
    
timeOffset = 0
totalLen = 0

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
    duration_start = timeOffset + 1
    totalLen += sourceEnd
    duration_end = totalLen
    timeOffset = totalLen
    
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
    #timeOffset += sourceEnd
    
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
closeAllNodeEditors;
closeHypershade;
optionVar -sv colorManagementColorPickerColorSpaceSelection "Rendering Space";
optionVar -iv colorManagementColorPickerColorMgtEnabled 1;
// Warning: file: F:/maya/projects/tinyPhx_isoShooter/scenes/pugRocket/rig/tp_isoShoot_pugRocket_rig.ma line 4974: You must either select the affected nodes or specify them on the command line. // 
// Warning: file: F:/maya/projects/tinyPhx_isoShooter/scenes/pugRocket/rig/tp_isoShoot_pugRocket_rig.ma line 4977: You must either select the affected nodes or specify them on the command line. // 
// Warning: file: F:/maya/projects/tinyPhx_isoShooter/scenes/pugRocket/rig/tp_isoShoot_pugRocket_rig.ma line 4980: You must either select the affected nodes or specify them on the command line. // 
// Warning: file: F:/maya/projects/tinyPhx_isoShooter/scenes/pugRocket/rig/tp_isoShoot_pugRocket_rig.ma line 4983: You must either select the affected nodes or specify them on the command line. // 
// Warning: line 1997: The default image may not be modified. Use the -i/image flag instead. // 
# Read 2 files in  0.25 seconds. # 
With this file as input: F:/maya/projects/tinyPhx_isoShooter/scenes/pugRocket/anim/exit/tpx_pugRocket_exit_anim.ma
This would be the new file: F:/maya/projects/tinyPhx_isoShooter/assets/pugRocket/anims/exit/03/tpx_pugRocket_exit_anim.fbx
# Warning: bakeSimulation is obsolete.  Please use "bakeResults -simulation" instead. # 
// Logfile: "C:\Users\Wesley\Documents\maya\FBX\Logs\2016.1.2\maya2016exp.log" // 
closeAllNodeEditors;
closeHypershade;
optionVar -sv colorManagementColorPickerColorSpaceSelection "Rendering Space";
optionVar -iv colorManagementColorPickerColorMgtEnabled 1;
// Warning: file: F:/maya/projects/tinyPhx_isoShooter/scenes/pugRocket/rig/tp_isoShoot_pugRocket_rig.ma line 4974: You must either select the affected nodes or specify them on the command line. // 
// Warning: file: F:/maya/projects/tinyPhx_isoShooter/scenes/pugRocket/rig/tp_isoShoot_pugRocket_rig.ma line 4977: You must either select the affected nodes or specify them on the command line. // 
// Warning: file: F:/maya/projects/tinyPhx_isoShooter/scenes/pugRocket/rig/tp_isoShoot_pugRocket_rig.ma line 4980: You must either select the affected nodes or specify them on the command line. // 
// Warning: file: F:/maya/projects/tinyPhx_isoShooter/scenes/pugRocket/rig/tp_isoShoot_pugRocket_rig.ma line 4983: You must either select the affected nodes or specify them on the command line. // 
// Warning: line 1999: The default image may not be modified. Use the -i/image flag instead. // 
# Read 2 files in  0.25 seconds. # 
With this file as input: F:/maya/projects/tinyPhx_isoShooter/scenes/pugRocket/anim/flyLoop/tpx_pugRocket_flyLoop_anim.ma
This would be the new file: F:/maya/projects/tinyPhx_isoShooter/assets/pugRocket/anims/flyLoop/03/tpx_pugRocket_flyLoop_anim.fbx
# Warning: bakeSimulation is obsolete.  Please use "bakeResults -simulation" instead. # 
// Logfile: "C:\Users\Wesley\Documents\maya\FBX\Logs\2016.1.2\maya2016exp.log" // 
closeAllNodeEditors;
closeHypershade;
optionVar -sv colorManagementColorPickerColorSpaceSelection "Rendering Space";
optionVar -iv colorManagementColorPickerColorMgtEnabled 1;
// Warning: file: F:/maya/projects/tinyPhx_isoShooter/scenes/pugRocket/rig/tp_isoShoot_pugRocket_rig.ma line 4974: You must either select the affected nodes or specify them on the command line. // 
// Warning: file: F:/maya/projects/tinyPhx_isoShooter/scenes/pugRocket/rig/tp_isoShoot_pugRocket_rig.ma line 4977: You must either select the affected nodes or specify them on the command line. // 
// Warning: file: F:/maya/projects/tinyPhx_isoShooter/scenes/pugRocket/rig/tp_isoShoot_pugRocket_rig.ma line 4980: You must either select the affected nodes or specify them on the command line. // 
// Warning: file: F:/maya/projects/tinyPhx_isoShooter/scenes/pugRocket/rig/tp_isoShoot_pugRocket_rig.ma line 4983: You must either select the affected nodes or specify them on the command line. // 
// Warning: line 2004: The default image may not be modified. Use the -i/image flag instead. // 
# Read 2 files in  0.24 seconds. # 
With this file as input: F:/maya/projects/tinyPhx_isoShooter/scenes/pugRocket/anim/land/tpx_pugRocket_land_anim.ma
This would be the new file: F:/maya/projects/tinyPhx_isoShooter/assets/pugRocket/anims/land/03/tpx_pugRocket_land_anim.fbx
# Warning: bakeSimulation is obsolete.  Please use "bakeResults -simulation" instead. # 
// Logfile: "C:\Users\Wesley\Documents\maya\FBX\Logs\2016.1.2\maya2016exp.log" // 
closeAllNodeEditors;
closeHypershade;
optionVar -sv colorManagementColorPickerColorSpaceSelection "Rendering Space";
optionVar -iv colorManagementColorPickerColorMgtEnabled 1;
// Warning: file: F:/maya/projects/tinyPhx_isoShooter/scenes/pugRocket/rig/tp_isoShoot_pugRocket_rig.ma line 4974: You must either select the affected nodes or specify them on the command line. // 
// Warning: file: F:/maya/projects/tinyPhx_isoShooter/scenes/pugRocket/rig/tp_isoShoot_pugRocket_rig.ma line 4977: You must either select the affected nodes or specify them on the command line. // 
// Warning: file: F:/maya/projects/tinyPhx_isoShooter/scenes/pugRocket/rig/tp_isoShoot_pugRocket_rig.ma line 4980: You must either select the affected nodes or specify them on the command line. // 
// Warning: file: F:/maya/projects/tinyPhx_isoShooter/scenes/pugRocket/rig/tp_isoShoot_pugRocket_rig.ma line 4983: You must either select the affected nodes or specify them on the command line. // 
// Warning: line 2007: The default image may not be modified. Use the -i/image flag instead. // 
# Read 2 files in  0.25 seconds. # 
With this file as input: F:/maya/projects/tinyPhx_isoShooter/scenes/pugRocket/anim/takeOff/tpx_pugRocket_takeOff_anim.ma
This would be the new file: F:/maya/projects/tinyPhx_isoShooter/assets/pugRocket/anims/takeOff/03/tpx_pugRocket_takeOff_anim.fbx
# Warning: bakeSimulation is obsolete.  Please use "bakeResults -simulation" instead. # 
// Logfile: "C:\Users\Wesley\Documents\maya\FBX\Logs\2016.1.2\maya2016exp.log" // 
optionVar -sv colorManagementColorPickerColorSpaceSelection "Rendering Space";
optionVar -iv colorManagementColorPickerColorMgtEnabled 1;
With this file as input: F:/maya/projects/tinyPhx_isoShooter/assets/pugRocket/anims/exit/03/tpx_pugRocket_exit_anim.fbx
This would be the new file: F:/maya/projects/tinyPhx_isoShooter/assets/pugRocket/anims/exit/03/pugRocket@exit.fbx
// Logfile: "C:\Users\Wesley\Documents\maya\FBX\Logs\2016.1.2\maya2016imp.log" // 
setAttr -type "string" rocket_rig_grp|rocket_geo_grp|rocket_hull_geo|rocket_hull_geoShape.currentUVSet "map1";
setAttr -type "string" rocket_rig_grp|rocket_geo_grp|rocket_hatch_geo_grp|rocket_hatch01_geo|rocket_hatch01_geoShape.currentUVSet "map1";
setAttr -type "string" rocket_rig_grp|rocket_geo_grp|rocket_hatch_geo_grp|rocket_hatch02_geo|rocket_hatch02_geoShape.currentUVSet "map1";
setAttr -type "string" rocket_rig_grp|rocket_geo_grp|rocket_hatch_geo_grp|rocket_hatch03_geo|rocket_hatch03_geoShape.currentUVSet "map1";
setAttr -type "string" rocket_rig_grp|rocket_geo_grp|rocket_hatch_geo_grp|rocket_hatch04_geo|rocket_hatch04_geoShape.currentUVSet "map1";
setAttr -type "string" rocket_rig_grp|rocket_geo_grp|rocket_hatch_geo_grp|rocket_hatch05_geo|rocket_hatch05_geoShape.currentUVSet "map1";
setAttr -type "string" rocket_rig_grp|rocket_geo_grp|rocket_hatch_geo_grp|rocket_hatch06_geo|rocket_hatch06_geoShape.currentUVSet "map1";
setAttr -type "string" rocket_rig_grp|rocket_geo_grp|rocket_jewel_geo_grp|rocket_jewel01_geo|rocket_jewel01_geoShape.currentUVSet "map1";
setAttr -type "string" rocket_rig_grp|rocket_geo_grp|rocket_jewel_geo_grp|rocket_jewel02_geo|rocket_jewel02_geoShape.currentUVSet "map1";
setAttr -type "string" rocket_rig_grp|rocket_geo_grp|rocket_jewel_geo_grp|rocket_jewel03_geo|rocket_jewel03_geoShape.currentUVSet "map1";
setAttr -type "string" rocket_rig_grp|rocket_geo_grp|rocket_jewel_geo_grp|rocket_jewel04_geo|rocket_jewel04_geoShape.currentUVSet "map1";
setAttr -type "string" rocket_rig_grp|rocket_geo_grp|rocket_jewel_geo_grp|rocket_jewel05_geo|rocket_jewel05_geoShape.currentUVSet "map1";
setAttr -type "string" rocket_rig_grp|rocket_geo_grp|rocket_jewel_geo_grp|rocket_jewel06_geo|rocket_jewel06_geoShape.currentUVSet "map1";
setAttr -type "string" rocket_rig_grp|rocket_geo_grp|rocket_fin_geo_grp|rocket_fin01_geo|rocket_fin01_geoShape.currentUVSet "map1";
setAttr -type "string" rocket_rig_grp|rocket_geo_grp|rocket_fin_geo_grp|rocket_fin02_geo|rocket_fin02_geoShape.currentUVSet "map1";
setAttr -type "string" rocket_rig_grp|rocket_geo_grp|rocket_fin_geo_grp|rocket_fin03_geo|rocket_fin03_geoShape.currentUVSet "map1";
setAttr -type "string" rocket_rig_grp|rocket_geo_grp|exhaust_geo_grp|exhaust_out_geo|exhaust_out_geoShape.currentUVSet "map1";
setAttr -type "string" rocket_rig_grp|rocket_geo_grp|exhaust_geo_grp|exhaust_in_geo|exhaust_in_geoShape.currentUVSet "map1";
setAttr -type "string" rocket_rig_grp|rocket_geo_grp|rocket_dome_geo|rocket_dome_geoShape.currentUVSet "map1";
# Error: ValueError: file C:/Users/Wesley/Documents/maya/scripts\ww_fbx_export\ww_fbx_export_funcLib.py line 97: No object matches name: joints_grp # 
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
    #if a charcter is in the scene, then run the next line.  if not - then move to the prop tool.  run it with the approriate name
    #ww_fbx_export_funcLib.ReorganizeCharacterHierarchy()
    #ww_fbx_export_funcLib.ReorganizePropHierarchy('gun01')
    ww_fbx_export_funcLib.ReorganizePropHierarchy('rocket')
    
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
    
timeOffset = 0
totalLen = 0

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
    duration_start = timeOffset + 1
    totalLen += sourceEnd
    duration_end = totalLen
    timeOffset = totalLen
    
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
    #timeOffset += sourceEnd
    
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
closeAllNodeEditors;
closeHypershade;
optionVar -sv colorManagementColorPickerColorSpaceSelection "Rendering Space";
optionVar -iv colorManagementColorPickerColorMgtEnabled 1;
// Warning: file: F:/maya/projects/tinyPhx_isoShooter/scenes/pugRocket/rig/tp_isoShoot_pugRocket_rig.ma line 4974: You must either select the affected nodes or specify them on the command line. // 
// Warning: file: F:/maya/projects/tinyPhx_isoShooter/scenes/pugRocket/rig/tp_isoShoot_pugRocket_rig.ma line 4977: You must either select the affected nodes or specify them on the command line. // 
// Warning: file: F:/maya/projects/tinyPhx_isoShooter/scenes/pugRocket/rig/tp_isoShoot_pugRocket_rig.ma line 4980: You must either select the affected nodes or specify them on the command line. // 
// Warning: file: F:/maya/projects/tinyPhx_isoShooter/scenes/pugRocket/rig/tp_isoShoot_pugRocket_rig.ma line 4983: You must either select the affected nodes or specify them on the command line. // 
// Warning: line 1997: The default image may not be modified. Use the -i/image flag instead. // 
# Read 2 files in  0.25 seconds. # 
With this file as input: F:/maya/projects/tinyPhx_isoShooter/scenes/pugRocket/anim/exit/tpx_pugRocket_exit_anim.ma
This would be the new file: F:/maya/projects/tinyPhx_isoShooter/assets/pugRocket/anims/exit/04/tpx_pugRocket_exit_anim.fbx
# Warning: bakeSimulation is obsolete.  Please use "bakeResults -simulation" instead. # 
// Logfile: "C:\Users\Wesley\Documents\maya\FBX\Logs\2016.1.2\maya2016exp.log" // 
closeAllNodeEditors;
closeHypershade;
optionVar -sv colorManagementColorPickerColorSpaceSelection "Rendering Space";
optionVar -iv colorManagementColorPickerColorMgtEnabled 1;
// Warning: file: F:/maya/projects/tinyPhx_isoShooter/scenes/pugRocket/rig/tp_isoShoot_pugRocket_rig.ma line 4974: You must either select the affected nodes or specify them on the command line. // 
// Warning: file: F:/maya/projects/tinyPhx_isoShooter/scenes/pugRocket/rig/tp_isoShoot_pugRocket_rig.ma line 4977: You must either select the affected nodes or specify them on the command line. // 
// Warning: file: F:/maya/projects/tinyPhx_isoShooter/scenes/pugRocket/rig/tp_isoShoot_pugRocket_rig.ma line 4980: You must either select the affected nodes or specify them on the command line. // 
// Warning: file: F:/maya/projects/tinyPhx_isoShooter/scenes/pugRocket/rig/tp_isoShoot_pugRocket_rig.ma line 4983: You must either select the affected nodes or specify them on the command line. // 
// Warning: line 1999: The default image may not be modified. Use the -i/image flag instead. // 
# Read 2 files in  0.25 seconds. # 
With this file as input: F:/maya/projects/tinyPhx_isoShooter/scenes/pugRocket/anim/flyLoop/tpx_pugRocket_flyLoop_anim.ma
This would be the new file: F:/maya/projects/tinyPhx_isoShooter/assets/pugRocket/anims/flyLoop/04/tpx_pugRocket_flyLoop_anim.fbx
# Warning: bakeSimulation is obsolete.  Please use "bakeResults -simulation" instead. # 
// Logfile: "C:\Users\Wesley\Documents\maya\FBX\Logs\2016.1.2\maya2016exp.log" // 
closeAllNodeEditors;
closeHypershade;
optionVar -sv colorManagementColorPickerColorSpaceSelection "Rendering Space";
optionVar -iv colorManagementColorPickerColorMgtEnabled 1;
// Warning: file: F:/maya/projects/tinyPhx_isoShooter/scenes/pugRocket/rig/tp_isoShoot_pugRocket_rig.ma line 4974: You must either select the affected nodes or specify them on the command line. // 
// Warning: file: F:/maya/projects/tinyPhx_isoShooter/scenes/pugRocket/rig/tp_isoShoot_pugRocket_rig.ma line 4977: You must either select the affected nodes or specify them on the command line. // 
// Warning: file: F:/maya/projects/tinyPhx_isoShooter/scenes/pugRocket/rig/tp_isoShoot_pugRocket_rig.ma line 4980: You must either select the affected nodes or specify them on the command line. // 
// Warning: file: F:/maya/projects/tinyPhx_isoShooter/scenes/pugRocket/rig/tp_isoShoot_pugRocket_rig.ma line 4983: You must either select the affected nodes or specify them on the command line. // 
// Warning: line 2004: The default image may not be modified. Use the -i/image flag instead. // 
# Read 2 files in  0.24 seconds. # 
With this file as input: F:/maya/projects/tinyPhx_isoShooter/scenes/pugRocket/anim/land/tpx_pugRocket_land_anim.ma
This would be the new file: F:/maya/projects/tinyPhx_isoShooter/assets/pugRocket/anims/land/04/tpx_pugRocket_land_anim.fbx
# Warning: bakeSimulation is obsolete.  Please use "bakeResults -simulation" instead. # 
// Logfile: "C:\Users\Wesley\Documents\maya\FBX\Logs\2016.1.2\maya2016exp.log" // 
closeAllNodeEditors;
closeHypershade;
optionVar -sv colorManagementColorPickerColorSpaceSelection "Rendering Space";
optionVar -iv colorManagementColorPickerColorMgtEnabled 1;
// Warning: file: F:/maya/projects/tinyPhx_isoShooter/scenes/pugRocket/rig/tp_isoShoot_pugRocket_rig.ma line 4974: You must either select the affected nodes or specify them on the command line. // 
// Warning: file: F:/maya/projects/tinyPhx_isoShooter/scenes/pugRocket/rig/tp_isoShoot_pugRocket_rig.ma line 4977: You must either select the affected nodes or specify them on the command line. // 
// Warning: file: F:/maya/projects/tinyPhx_isoShooter/scenes/pugRocket/rig/tp_isoShoot_pugRocket_rig.ma line 4980: You must either select the affected nodes or specify them on the command line. // 
// Warning: file: F:/maya/projects/tinyPhx_isoShooter/scenes/pugRocket/rig/tp_isoShoot_pugRocket_rig.ma line 4983: You must either select the affected nodes or specify them on the command line. // 
// Warning: line 2007: The default image may not be modified. Use the -i/image flag instead. // 
# Read 2 files in  0.25 seconds. # 
With this file as input: F:/maya/projects/tinyPhx_isoShooter/scenes/pugRocket/anim/takeOff/tpx_pugRocket_takeOff_anim.ma
This would be the new file: F:/maya/projects/tinyPhx_isoShooter/assets/pugRocket/anims/takeOff/04/tpx_pugRocket_takeOff_anim.fbx
# Warning: bakeSimulation is obsolete.  Please use "bakeResults -simulation" instead. # 
// Logfile: "C:\Users\Wesley\Documents\maya\FBX\Logs\2016.1.2\maya2016exp.log" // 
optionVar -sv colorManagementColorPickerColorSpaceSelection "Rendering Space";
optionVar -iv colorManagementColorPickerColorMgtEnabled 1;
With this file as input: F:/maya/projects/tinyPhx_isoShooter/assets/pugRocket/anims/exit/04/tpx_pugRocket_exit_anim.fbx
This would be the new file: F:/maya/projects/tinyPhx_isoShooter/assets/pugRocket/anims/exit/04/pugRocket@exit.fbx
// Logfile: "C:\Users\Wesley\Documents\maya\FBX\Logs\2016.1.2\maya2016imp.log" // 
setAttr -type "string" rocket_rig_grp|rocket_geo_grp|rocket_hull_geo|rocket_hull_geoShape.currentUVSet "map1";
setAttr -type "string" rocket_rig_grp|rocket_geo_grp|rocket_hatch_geo_grp|rocket_hatch01_geo|rocket_hatch01_geoShape.currentUVSet "map1";
setAttr -type "string" rocket_rig_grp|rocket_geo_grp|rocket_hatch_geo_grp|rocket_hatch02_geo|rocket_hatch02_geoShape.currentUVSet "map1";
setAttr -type "string" rocket_rig_grp|rocket_geo_grp|rocket_hatch_geo_grp|rocket_hatch03_geo|rocket_hatch03_geoShape.currentUVSet "map1";
setAttr -type "string" rocket_rig_grp|rocket_geo_grp|rocket_hatch_geo_grp|rocket_hatch04_geo|rocket_hatch04_geoShape.currentUVSet "map1";
setAttr -type "string" rocket_rig_grp|rocket_geo_grp|rocket_hatch_geo_grp|rocket_hatch05_geo|rocket_hatch05_geoShape.currentUVSet "map1";
setAttr -type "string" rocket_rig_grp|rocket_geo_grp|rocket_hatch_geo_grp|rocket_hatch06_geo|rocket_hatch06_geoShape.currentUVSet "map1";
setAttr -type "string" rocket_rig_grp|rocket_geo_grp|rocket_jewel_geo_grp|rocket_jewel01_geo|rocket_jewel01_geoShape.currentUVSet "map1";
setAttr -type "string" rocket_rig_grp|rocket_geo_grp|rocket_jewel_geo_grp|rocket_jewel02_geo|rocket_jewel02_geoShape.currentUVSet "map1";
setAttr -type "string" rocket_rig_grp|rocket_geo_grp|rocket_jewel_geo_grp|rocket_jewel03_geo|rocket_jewel03_geoShape.currentUVSet "map1";
setAttr -type "string" rocket_rig_grp|rocket_geo_grp|rocket_jewel_geo_grp|rocket_jewel04_geo|rocket_jewel04_geoShape.currentUVSet "map1";
setAttr -type "string" rocket_rig_grp|rocket_geo_grp|rocket_jewel_geo_grp|rocket_jewel05_geo|rocket_jewel05_geoShape.currentUVSet "map1";
setAttr -type "string" rocket_rig_grp|rocket_geo_grp|rocket_jewel_geo_grp|rocket_jewel06_geo|rocket_jewel06_geoShape.currentUVSet "map1";
setAttr -type "string" rocket_rig_grp|rocket_geo_grp|rocket_fin_geo_grp|rocket_fin01_geo|rocket_fin01_geoShape.currentUVSet "map1";
setAttr -type "string" rocket_rig_grp|rocket_geo_grp|rocket_fin_geo_grp|rocket_fin02_geo|rocket_fin02_geoShape.currentUVSet "map1";
setAttr -type "string" rocket_rig_grp|rocket_geo_grp|rocket_fin_geo_grp|rocket_fin03_geo|rocket_fin03_geoShape.currentUVSet "map1";
setAttr -type "string" rocket_rig_grp|rocket_geo_grp|exhaust_geo_grp|exhaust_out_geo|exhaust_out_geoShape.currentUVSet "map1";
setAttr -type "string" rocket_rig_grp|rocket_geo_grp|exhaust_geo_grp|exhaust_in_geo|exhaust_in_geoShape.currentUVSet "map1";
setAttr -type "string" rocket_rig_grp|rocket_geo_grp|rocket_dome_geo|rocket_dome_geoShape.currentUVSet "map1";
// Logfile: "C:\Users\Wesley\Documents\maya\FBX\Logs\2016.1.2\maya2016exp.log" // 
optionVar -sv colorManagementColorPickerColorSpaceSelection "Rendering Space";
optionVar -iv colorManagementColorPickerColorMgtEnabled 1;
With this file as input: F:/maya/projects/tinyPhx_isoShooter/assets/pugRocket/anims/flyLoop/04/tpx_pugRocket_flyLoop_anim.fbx
This would be the new file: F:/maya/projects/tinyPhx_isoShooter/assets/pugRocket/anims/flyLoop/04/pugRocket@flyLoop.fbx
// Logfile: "C:\Users\Wesley\Documents\maya\FBX\Logs\2016.1.2\maya2016imp.log" // 
setAttr -type "string" rocket_rig_grp|rocket_geo_grp|rocket_hull_geo|rocket_hull_geoShape.currentUVSet "map1";
setAttr -type "string" rocket_rig_grp|rocket_geo_grp|rocket_hatch_geo_grp|rocket_hatch01_geo|rocket_hatch01_geoShape.currentUVSet "map1";
setAttr -type "string" rocket_rig_grp|rocket_geo_grp|rocket_hatch_geo_grp|rocket_hatch02_geo|rocket_hatch02_geoShape.currentUVSet "map1";
setAttr -type "string" rocket_rig_grp|rocket_geo_grp|rocket_hatch_geo_grp|rocket_hatch03_geo|rocket_hatch03_geoShape.currentUVSet "map1";
setAttr -type "string" rocket_rig_grp|rocket_geo_grp|rocket_hatch_geo_grp|rocket_hatch04_geo|rocket_hatch04_geoShape.currentUVSet "map1";
setAttr -type "string" rocket_rig_grp|rocket_geo_grp|rocket_hatch_geo_grp|rocket_hatch05_geo|rocket_hatch05_geoShape.currentUVSet "map1";
setAttr -type "string" rocket_rig_grp|rocket_geo_grp|rocket_hatch_geo_grp|rocket_hatch06_geo|rocket_hatch06_geoShape.currentUVSet "map1";
setAttr -type "string" rocket_rig_grp|rocket_geo_grp|rocket_jewel_geo_grp|rocket_jewel01_geo|rocket_jewel01_geoShape.currentUVSet "map1";
setAttr -type "string" rocket_rig_grp|rocket_geo_grp|rocket_jewel_geo_grp|rocket_jewel02_geo|rocket_jewel02_geoShape.currentUVSet "map1";
setAttr -type "string" rocket_rig_grp|rocket_geo_grp|rocket_jewel_geo_grp|rocket_jewel03_geo|rocket_jewel03_geoShape.currentUVSet "map1";
setAttr -type "string" rocket_rig_grp|rocket_geo_grp|rocket_jewel_geo_grp|rocket_jewel04_geo|rocket_jewel04_geoShape.currentUVSet "map1";
setAttr -type "string" rocket_rig_grp|rocket_geo_grp|rocket_jewel_geo_grp|rocket_jewel05_geo|rocket_jewel05_geoShape.currentUVSet "map1";
setAttr -type "string" rocket_rig_grp|rocket_geo_grp|rocket_jewel_geo_grp|rocket_jewel06_geo|rocket_jewel06_geoShape.currentUVSet "map1";
setAttr -type "string" rocket_rig_grp|rocket_geo_grp|rocket_fin_geo_grp|rocket_fin01_geo|rocket_fin01_geoShape.currentUVSet "map1";
setAttr -type "string" rocket_rig_grp|rocket_geo_grp|rocket_fin_geo_grp|rocket_fin02_geo|rocket_fin02_geoShape.currentUVSet "map1";
setAttr -type "string" rocket_rig_grp|rocket_geo_grp|rocket_fin_geo_grp|rocket_fin03_geo|rocket_fin03_geoShape.currentUVSet "map1";
setAttr -type "string" rocket_rig_grp|rocket_geo_grp|exhaust_geo_grp|exhaust_out_geo|exhaust_out_geoShape.currentUVSet "map1";
setAttr -type "string" rocket_rig_grp|rocket_geo_grp|exhaust_geo_grp|exhaust_in_geo|exhaust_in_geoShape.currentUVSet "map1";
setAttr -type "string" rocket_rig_grp|rocket_geo_grp|rocket_dome_geo|rocket_dome_geoShape.currentUVSet "map1";
// Logfile: "C:\Users\Wesley\Documents\maya\FBX\Logs\2016.1.2\maya2016exp.log" // 
optionVar -sv colorManagementColorPickerColorSpaceSelection "Rendering Space";
optionVar -iv colorManagementColorPickerColorMgtEnabled 1;
With this file as input: F:/maya/projects/tinyPhx_isoShooter/assets/pugRocket/anims/land/04/tpx_pugRocket_land_anim.fbx
This would be the new file: F:/maya/projects/tinyPhx_isoShooter/assets/pugRocket/anims/land/04/pugRocket@land.fbx
// Logfile: "C:\Users\Wesley\Documents\maya\FBX\Logs\2016.1.2\maya2016imp.log" // 
setAttr -type "string" rocket_rig_grp|rocket_geo_grp|rocket_hull_geo|rocket_hull_geoShape.currentUVSet "map1";
setAttr -type "string" rocket_rig_grp|rocket_geo_grp|rocket_hatch_geo_grp|rocket_hatch01_geo|rocket_hatch01_geoShape.currentUVSet "map1";
setAttr -type "string" rocket_rig_grp|rocket_geo_grp|rocket_hatch_geo_grp|rocket_hatch02_geo|rocket_hatch02_geoShape.currentUVSet "map1";
setAttr -type "string" rocket_rig_grp|rocket_geo_grp|rocket_hatch_geo_grp|rocket_hatch03_geo|rocket_hatch03_geoShape.currentUVSet "map1";
setAttr -type "string" rocket_rig_grp|rocket_geo_grp|rocket_hatch_geo_grp|rocket_hatch04_geo|rocket_hatch04_geoShape.currentUVSet "map1";
setAttr -type "string" rocket_rig_grp|rocket_geo_grp|rocket_hatch_geo_grp|rocket_hatch05_geo|rocket_hatch05_geoShape.currentUVSet "map1";
setAttr -type "string" rocket_rig_grp|rocket_geo_grp|rocket_hatch_geo_grp|rocket_hatch06_geo|rocket_hatch06_geoShape.currentUVSet "map1";
setAttr -type "string" rocket_rig_grp|rocket_geo_grp|rocket_jewel_geo_grp|rocket_jewel01_geo|rocket_jewel01_geoShape.currentUVSet "map1";
setAttr -type "string" rocket_rig_grp|rocket_geo_grp|rocket_jewel_geo_grp|rocket_jewel02_geo|rocket_jewel02_geoShape.currentUVSet "map1";
setAttr -type "string" rocket_rig_grp|rocket_geo_grp|rocket_jewel_geo_grp|rocket_jewel03_geo|rocket_jewel03_geoShape.currentUVSet "map1";
setAttr -type "string" rocket_rig_grp|rocket_geo_grp|rocket_jewel_geo_grp|rocket_jewel04_geo|rocket_jewel04_geoShape.currentUVSet "map1";
setAttr -type "string" rocket_rig_grp|rocket_geo_grp|rocket_jewel_geo_grp|rocket_jewel05_geo|rocket_jewel05_geoShape.currentUVSet "map1";
setAttr -type "string" rocket_rig_grp|rocket_geo_grp|rocket_jewel_geo_grp|rocket_jewel06_geo|rocket_jewel06_geoShape.currentUVSet "map1";
setAttr -type "string" rocket_rig_grp|rocket_geo_grp|rocket_fin_geo_grp|rocket_fin01_geo|rocket_fin01_geoShape.currentUVSet "map1";
setAttr -type "string" rocket_rig_grp|rocket_geo_grp|rocket_fin_geo_grp|rocket_fin02_geo|rocket_fin02_geoShape.currentUVSet "map1";
setAttr -type "string" rocket_rig_grp|rocket_geo_grp|rocket_fin_geo_grp|rocket_fin03_geo|rocket_fin03_geoShape.currentUVSet "map1";
setAttr -type "string" rocket_rig_grp|rocket_geo_grp|exhaust_geo_grp|exhaust_out_geo|exhaust_out_geoShape.currentUVSet "map1";
setAttr -type "string" rocket_rig_grp|rocket_geo_grp|exhaust_geo_grp|exhaust_in_geo|exhaust_in_geoShape.currentUVSet "map1";
setAttr -type "string" rocket_rig_grp|rocket_geo_grp|rocket_dome_geo|rocket_dome_geoShape.currentUVSet "map1";
// Logfile: "C:\Users\Wesley\Documents\maya\FBX\Logs\2016.1.2\maya2016exp.log" // 
optionVar -sv colorManagementColorPickerColorSpaceSelection "Rendering Space";
optionVar -iv colorManagementColorPickerColorMgtEnabled 1;
With this file as input: F:/maya/projects/tinyPhx_isoShooter/assets/pugRocket/anims/takeOff/04/tpx_pugRocket_takeOff_anim.fbx
This would be the new file: F:/maya/projects/tinyPhx_isoShooter/assets/pugRocket/anims/takeOff/04/pugRocket@takeOff.fbx
// Logfile: "C:\Users\Wesley\Documents\maya\FBX\Logs\2016.1.2\maya2016imp.log" // 
setAttr -type "string" rocket_rig_grp|rocket_geo_grp|rocket_hull_geo|rocket_hull_geoShape.currentUVSet "map1";
setAttr -type "string" rocket_rig_grp|rocket_geo_grp|rocket_hatch_geo_grp|rocket_hatch01_geo|rocket_hatch01_geoShape.currentUVSet "map1";
setAttr -type "string" rocket_rig_grp|rocket_geo_grp|rocket_hatch_geo_grp|rocket_hatch02_geo|rocket_hatch02_geoShape.currentUVSet "map1";
setAttr -type "string" rocket_rig_grp|rocket_geo_grp|rocket_hatch_geo_grp|rocket_hatch03_geo|rocket_hatch03_geoShape.currentUVSet "map1";
setAttr -type "string" rocket_rig_grp|rocket_geo_grp|rocket_hatch_geo_grp|rocket_hatch04_geo|rocket_hatch04_geoShape.currentUVSet "map1";
setAttr -type "string" rocket_rig_grp|rocket_geo_grp|rocket_hatch_geo_grp|rocket_hatch05_geo|rocket_hatch05_geoShape.currentUVSet "map1";
setAttr -type "string" rocket_rig_grp|rocket_geo_grp|rocket_hatch_geo_grp|rocket_hatch06_geo|rocket_hatch06_geoShape.currentUVSet "map1";
setAttr -type "string" rocket_rig_grp|rocket_geo_grp|rocket_jewel_geo_grp|rocket_jewel01_geo|rocket_jewel01_geoShape.currentUVSet "map1";
setAttr -type "string" rocket_rig_grp|rocket_geo_grp|rocket_jewel_geo_grp|rocket_jewel02_geo|rocket_jewel02_geoShape.currentUVSet "map1";
setAttr -type "string" rocket_rig_grp|rocket_geo_grp|rocket_jewel_geo_grp|rocket_jewel03_geo|rocket_jewel03_geoShape.currentUVSet "map1";
setAttr -type "string" rocket_rig_grp|rocket_geo_grp|rocket_jewel_geo_grp|rocket_jewel04_geo|rocket_jewel04_geoShape.currentUVSet "map1";
setAttr -type "string" rocket_rig_grp|rocket_geo_grp|rocket_jewel_geo_grp|rocket_jewel05_geo|rocket_jewel05_geoShape.currentUVSet "map1";
setAttr -type "string" rocket_rig_grp|rocket_geo_grp|rocket_jewel_geo_grp|rocket_jewel06_geo|rocket_jewel06_geoShape.currentUVSet "map1";
setAttr -type "string" rocket_rig_grp|rocket_geo_grp|rocket_fin_geo_grp|rocket_fin01_geo|rocket_fin01_geoShape.currentUVSet "map1";
setAttr -type "string" rocket_rig_grp|rocket_geo_grp|rocket_fin_geo_grp|rocket_fin02_geo|rocket_fin02_geoShape.currentUVSet "map1";
setAttr -type "string" rocket_rig_grp|rocket_geo_grp|rocket_fin_geo_grp|rocket_fin03_geo|rocket_fin03_geoShape.currentUVSet "map1";
setAttr -type "string" rocket_rig_grp|rocket_geo_grp|exhaust_geo_grp|exhaust_out_geo|exhaust_out_geoShape.currentUVSet "map1";
setAttr -type "string" rocket_rig_grp|rocket_geo_grp|exhaust_geo_grp|exhaust_in_geo|exhaust_in_geoShape.currentUVSet "map1";
setAttr -type "string" rocket_rig_grp|rocket_geo_grp|rocket_dome_geo|rocket_dome_geoShape.currentUVSet "map1";
// Logfile: "C:\Users\Wesley\Documents\maya\FBX\Logs\2016.1.2\maya2016exp.log" // 
optionVar -sv colorManagementColorPickerColorSpaceSelection "Rendering Space";
optionVar -iv colorManagementColorPickerColorMgtEnabled 1;
// Logfile: "C:\Users\Wesley\Documents\maya\FBX\Logs\2016.1.2\maya2016imp.log" // 
setAttr -type "string" rocket_rig_grp|rocket_geo_grp|rocket_hull_geo|rocket_hull_geoShape.currentUVSet "map1";
setAttr -type "string" rocket_rig_grp|rocket_geo_grp|rocket_hatch_geo_grp|rocket_hatch01_geo|rocket_hatch01_geoShape.currentUVSet "map1";
setAttr -type "string" rocket_rig_grp|rocket_geo_grp|rocket_hatch_geo_grp|rocket_hatch02_geo|rocket_hatch02_geoShape.currentUVSet "map1";
setAttr -type "string" rocket_rig_grp|rocket_geo_grp|rocket_hatch_geo_grp|rocket_hatch03_geo|rocket_hatch03_geoShape.currentUVSet "map1";
setAttr -type "string" rocket_rig_grp|rocket_geo_grp|rocket_hatch_geo_grp|rocket_hatch04_geo|rocket_hatch04_geoShape.currentUVSet "map1";
setAttr -type "string" rocket_rig_grp|rocket_geo_grp|rocket_hatch_geo_grp|rocket_hatch05_geo|rocket_hatch05_geoShape.currentUVSet "map1";
setAttr -type "string" rocket_rig_grp|rocket_geo_grp|rocket_hatch_geo_grp|rocket_hatch06_geo|rocket_hatch06_geoShape.currentUVSet "map1";
setAttr -type "string" rocket_rig_grp|rocket_geo_grp|rocket_jewel_geo_grp|rocket_jewel01_geo|rocket_jewel01_geoShape.currentUVSet "map1";
setAttr -type "string" rocket_rig_grp|rocket_geo_grp|rocket_jewel_geo_grp|rocket_jewel02_geo|rocket_jewel02_geoShape.currentUVSet "map1";
setAttr -type "string" rocket_rig_grp|rocket_geo_grp|rocket_jewel_geo_grp|rocket_jewel03_geo|rocket_jewel03_geoShape.currentUVSet "map1";
setAttr -type "string" rocket_rig_grp|rocket_geo_grp|rocket_jewel_geo_grp|rocket_jewel04_geo|rocket_jewel04_geoShape.currentUVSet "map1";
setAttr -type "string" rocket_rig_grp|rocket_geo_grp|rocket_jewel_geo_grp|rocket_jewel05_geo|rocket_jewel05_geoShape.currentUVSet "map1";
setAttr -type "string" rocket_rig_grp|rocket_geo_grp|rocket_jewel_geo_grp|rocket_jewel06_geo|rocket_jewel06_geoShape.currentUVSet "map1";
setAttr -type "string" rocket_rig_grp|rocket_geo_grp|rocket_fin_geo_grp|rocket_fin01_geo|rocket_fin01_geoShape.currentUVSet "map1";
setAttr -type "string" rocket_rig_grp|rocket_geo_grp|rocket_fin_geo_grp|rocket_fin02_geo|rocket_fin02_geoShape.currentUVSet "map1";
setAttr -type "string" rocket_rig_grp|rocket_geo_grp|rocket_fin_geo_grp|rocket_fin03_geo|rocket_fin03_geoShape.currentUVSet "map1";
setAttr -type "string" rocket_rig_grp|rocket_geo_grp|exhaust_geo_grp|exhaust_out_geo|exhaust_out_geoShape.currentUVSet "map1";
setAttr -type "string" rocket_rig_grp|rocket_geo_grp|exhaust_geo_grp|exhaust_in_geo|exhaust_in_geoShape.currentUVSet "map1";
setAttr -type "string" rocket_rig_grp|rocket_geo_grp|rocket_dome_geo|rocket_dome_geoShape.currentUVSet "map1";

We are working with: F:/maya/projects/tinyPhx_isoShooter/assets/pugRocket/anims/exit/04/pugRocket@exit.fbx
Associated ATOM file: F:/maya/projects/tinyPhx_isoShooter/data/anim/pugRocket/exit/pugRocket_exit_003.atom
sourceStart = 1
sourceEnd = 39
duration_start = 1
duration_end = 39

# File read in  0.075 seconds. # 

We are working with: F:/maya/projects/tinyPhx_isoShooter/assets/pugRocket/anims/flyLoop/04/pugRocket@flyLoop.fbx
Associated ATOM file: F:/maya/projects/tinyPhx_isoShooter/data/anim/pugRocket/flyLoop/pugRocket_flyLoop_002.atom
sourceStart = 1
sourceEnd = 30
duration_start = 40
duration_end = 69

# File read in  0.053 seconds. # 

We are working with: F:/maya/projects/tinyPhx_isoShooter/assets/pugRocket/anims/land/04/pugRocket@land.fbx
Associated ATOM file: F:/maya/projects/tinyPhx_isoShooter/data/anim/pugRocket/land/pugRocket_land_002.atom
sourceStart = 1
sourceEnd = 49
duration_start = 70
duration_end = 118

# File read in  0.088 seconds. # 

We are working with: F:/maya/projects/tinyPhx_isoShooter/assets/pugRocket/anims/takeOff/04/pugRocket@takeOff.fbx
Associated ATOM file: F:/maya/projects/tinyPhx_isoShooter/data/anim/pugRocket/takeOff/pugRocket_takeOff_002.atom
sourceStart = 1
sourceEnd = 60
duration_start = 119
duration_end = 178

# File read in  0.087 seconds. # 
// Logfile: "C:\Users\Wesley\Documents\maya\FBX\Logs\2016.1.2\maya2016exp.log" // 
currentTime 1 ;
currentTime 39 ;
// Press the ESC key to stop playback. // 
currentTime 32 ;
currentTime 40 ;
// Press the ESC key to stop playback. // 
currentTime 64 ;
currentTime 70 ;
// Press the ESC key to stop playback. // 
currentTime 86 ;
// Press the ESC key to stop playback. // 
currentTime 140 ;
currentTime 119 ;
playbackOptions -min 40 -max 178 ;
