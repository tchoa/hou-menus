import sys, hou

attrtype = sys.argv[1]
script = "\
def build_menu_from(items, menu):\n\
\tif len(items):\n\
\t\tmenu.extend((\"-\", \"\"))\n\
\tfor item in items:\n\
\t\tname = item.name()\n\
\t\tmenu.extend((name, name))\n\
\treturn menu\n\
sopnode = hou.pwd()\n\
menu = []\n\
if sopnode.inputs():\n\
\tmenu.extend((\"*\", \"*\"))\n\
\tgeo = sopnode.inputs()[0].geometry()\n\
\tmenu = build_menu_from(geo."
script += attrtype + "(), menu)\nreturn menu"

parm = kwargs["parms"][0]
name = parm.name()
node = parm.node()
group = node.parmTemplateGroup()
template = group.find(name)
template.setItemGeneratorScript(script)
template.setItemGeneratorScriptLanguage(hou.scriptLanguage.Python)
template.setMenuType(hou.menuType.StringToggle)
group.replace(name, template)
node.setParmTemplateGroup(group)