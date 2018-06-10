import xml.etree.ElementTree as xmlt
xmlelement=xmlt.parse('input.xml')
x=xmlelement.getroot()
print x.tag
print "".join(x.attrib.keys()),":","".join(x.attrib.values())
for i in x.getchildren(): 
    print "%s : -> %s : %s" %(i.tag,"".join(i.attrib.keys()),"".join(i.attrib.values()))
    for j in i.getchildren():
        print "--:> %s : %s" %(j.tag,j.text)