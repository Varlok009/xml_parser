import xml.etree.ElementTree as et

tree = et.parse('../VO_OTKRDAN_4_9965_9965_20231107_fffcc016_d1c1_4cc4_ac4c_229336443f44.xml')
root = tree.getroot()
print(root)
tags = set()
for elem in root.iter():
    # print(elem.tag, elem.attrib)
    tags.add(elem.tag)

print(tags)

for document in root.iter('Документ'):
    org = document.find('СведНП')
    org_name = org.get('НаимОрг')
    org_inn = org.get('ИННЮЛ')
    if org_inn == '8602141966':
        org_nalogs = document.findall('СвУплСумНал')
        for org_nalog in org_nalogs:
            print(org_nalog.get('НаимНалог'))
    # print(block, block.attrib)




# for elem in block.findall('НаимНалог'):
#     print(elem.attrib)