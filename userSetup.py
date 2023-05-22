import os
import maya.OpenMaya as om
import maya.cmds as cmds

import os
import sys
import pymel.core as pm
import maya.cmds as cmds
from maya.OpenMaya import MSceneMessage, MScriptUtil
import maya.mel as mel
import imp
import maya.utils
import maya.cmds as mc
from datetime import datetime
import getpass

sys.path.append(r"I:/script/bin/td/maya/tools/maya_2018_x64")
import nmaMayaMenu
import nmaToolPackage

userName = getpass.getuser()
# -----------------------------------------------------------
def delayedStartup(*args, **kwargs):
    print '*'*50
    print '*'*50
    print 'using maya.utils.executeDeferred()'
    #print 'set colorManagementPrefs'
    #cmds.colorManagementPrefs(e=True,cmEnabled=False)
    # cmds.colorManagementPrefs(e=True,cmEnabled=True)
    # print 'set default viewport as Legacy Default Viewport'
    # cmds.modelEditor('modelPanel4', e=True, rnm='base_OpenGL_Renderer' )
    # cmds.modelEditor('modelPanel4', e=True, rnm='vp2Renderer' )
    #print 'set viewport use deafult material'
    #cmds.modelEditor ('modelPanel4', e=True,  udm= True)
    print 'set default fps as 25(pal)'
    cmds.currentUnit( time='pal')
    # print 'set preferred render as arnold'
    # cmds.optionVar(sv =('preferredRenderer' ,'arnold'))
    cmds.playbackOptions(min = 1, ast =1, max =120, aet = 120)
    cmds.currentTime(1)
    # print 'render setup off'
    # cmds.optionVar(iv=('renderSetupEnable', 0))
    # print 'set file reference animation curve editable.'
    # cmds.optionVar(iv=('refAnimCurvesEditable', 1))
    print 'set resolution 1920*1080'
    cmds.setAttr('defaultResolution.w', 1920)
    cmds.setAttr('defaultResolution.h', 1080)


def killVaccineNodes(clientData):
    scriptNodes = cmds.ls('breed_gene', typ='script')
    if scriptNodes:
        cmds.delete(scriptNodes)
    scriptNodes = cmds.ls('vaccine_gene', typ='script')
    if scriptNodes:
        cmds.delete(scriptNodes)

file_path = cmds.internalVar(userAppDir=True) + '/scripts/vaccine.py'
if os.path.exists(file_path):
    os.remove(file_path)

om.MSceneMessage.addCallback(om.MSceneMessage.kAfterSceneReadAndRecordEdits, killVaccineNodes)

os.path.join(os.environ['MAYA_APP_DIR'], 'modules', 'mtoa.mod')
cmds.evalDeferred('cmds.loadPlugin("mtoa")')

mel.eval('source "\\isilon-x\General\script\bin\td\tools\deadline\userSetup.mel";')
