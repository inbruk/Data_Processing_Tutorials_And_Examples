import numpy as np
import pandas as pd
import operator
import json
from pprint import pprint
import xml.etree.ElementTree as ET
import xmljson


tree = ET.parse('menu.xml')
root = tree.getroot()
print(root)

children = root.getchildren()
print(children)

print(root[0].attrib)

print(root[0][1])

print(root[0][0].text)

for elem in root:
    for subelem in elem:
        print(elem.attrib['name'], subelem.tag, subelem.text)
    print()

parker_json = xmljson.parker.data(root)
back_to_xml = xmljson.parker.etree(parker_json)
print(parker_json)
print(back_to_xml)


new_root = ET.Element('menu')
dish_1 = ET.SubElement(new_root, 'dish')
dish_1.set('name', 'Кура')
dish_1.text = 'Белок'
dish_2 = ET.SubElement(new_root, 'dish')
new_root.getchildren()
new_root_string = ET.tostring(new_root)
print(new_root_string)
ET.ElementTree(new_root).write('new_menu_good.xml', encoding="utf-8")







