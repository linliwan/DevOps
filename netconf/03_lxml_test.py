from lxml import etree

xml_test_tree = etree.parse('01_all_config.xml')
# print(xml_test_tree)
root = xml_test_tree.getroot()
pretty_xml = etree.tostring(root, encoding='unicode', pretty_print=True)
# print(pretty_xml)
# print(root.tag)
# print(root[0].tag)
# print(root[0][1][0].tag)
# print(root[0][1][0].text)

result = root.find('.//{urn:ietf:params:xml:ns:yang:ietf-interfaces}interfaces')
print(etree.tostring(result, encoding='unicode', pretty_print=True))

# print(type(result))





