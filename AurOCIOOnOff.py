#Turn OCIO Off
import maya.cmds as cmds
cmds.colorManagementPrefs( e=True, cfe=False );
#Turn OCIO On
import maya.cmds as cmds
cmds.colorManagementPrefs( e=True, cfe=True );