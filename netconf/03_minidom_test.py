import xml.dom.minidom


xml_test_dom = xml.dom.minidom.parse('./01_all_config.xml')
# print(xml_test_dom)

result = xml_test_dom.getElementsByTagName('interfaces')
# print(result[0].toxml())
print(result[0].childNodes[0].toprettyxml())
print(result[0].childNodes[0].childNodes[0].tagName)
print(result[0].childNodes[0].childNodes[0].childNodes[0].nodeValue)

print('==================')

result_1 = xml_test_dom.getElementsByTagNameNS('urn:ietf:params:xml:ns:yang:ietf-interfaces', 'interfaces')
print(result_1[0].namespaceURI)


