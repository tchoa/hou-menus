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
	hou.ui.openParameterInterfaceDialog(parent)
