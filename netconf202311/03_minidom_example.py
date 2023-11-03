from xml.dom import minidom

# 从string创建dom

my_str = '''
<root><child1 xmlns="http://www.abc.com/schema1">ch1 text</child1><child2/><child1/></root>
'''

my_dom = minidom.parseString(my_str)
print(my_dom)

my_dom_str = my_dom.toprettyxml()
print(my_dom_str)
print("==============================")

# print(my_dom.childNodes[0].childNodes[0].childNodes[0].nodeValue)
print(my_dom.getElementsByTagName('child1'))
print(my_dom.getElementsByTagNameNS('http://www.abc.com/schema1', 'child1'))