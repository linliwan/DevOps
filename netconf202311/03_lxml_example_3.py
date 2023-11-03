from lxml import etree

# 从string创建etree element
my_str = '''
<root><child1>ch1 text</child1><child2/><child1/></root>
# '''
#
# my_root = etree.fromstring(my_str)
# print(my_root)
# my_root_str = etree.tostring(my_root, encoding="unicode", pretty_print=True)
# print(my_root_str)
# print("============================")

# 从文件创建etree
# xml_tree = etree.parse('./01_xml_test.xml')
# xml_tree_root = xml_tree.getroot()
# print(etree.tostring(xml_tree_root, encoding="unicode", pretty_print=True))
# print("========================")
#
# print(xml_tree_root[2][0].tag)
# print(xml_tree_root[1][0].tag)


# 从文件创建etree
xml_tree = etree.parse('./01_all_config.xml')
xml_tree_root = xml_tree.getroot()
# print(etree.tostring(xml_tree_root, encoding="unicode", pretty_print=True))
print("========================")

result = xml_tree_root.findall('.//{*}version')
print(result)




