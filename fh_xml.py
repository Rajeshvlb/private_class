pip instal  xmltodict

import xmltodict

handle = open("xml_input.xml", "r")
content = handle.read()
print(content)

d = xmltodict.parse(content) #returns dictionary

x = xmltodict.unparse(d) #returns xml
