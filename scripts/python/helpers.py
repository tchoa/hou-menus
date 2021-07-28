'''
import sys
path = hou.getenv('HOUDINI_USER_PREF_DIR')
sys.path.append(path + '/scripts/python')
'''

import hou

def clean_subnet(args):
	node = args['node']
	group = node.parmTemplateGroup()
	for i in range(1, 5):
		name = 'label' + str(i)
		parm = group.find(name)
		if not node.parm(name) is None:
			parm.hide(True)
			group.replace(name, parm)
	for name in ['Transform', 'Render', 'Misc', 'Subnet']:
		parm = group.findFolder(name)
		if not parm is None:
			parm.hide(True)
			group.replace(parm.name(), parm)
	node.setParmTemplateGroup(group)

def edit_parent_spare_parms(args):
	node = args['node']
	parent = node.parent()
	while parent.isInsideLockedHDA():
		parent = parent.parent()
	typename = parent.type().name()
	if typename == 'obj':
		return
	if typename in ('geo', 'subnet') or 'solver' in typename:
		hou.ui.openParameterInterfaceDialog(parent)
	else:
		hou.ui.openTypePropertiesDialog(parent)