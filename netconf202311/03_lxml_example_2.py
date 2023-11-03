from lxml import etree

my_root = etree.Element("root")
etree.SubElement(my_root, "child1")
etree.SubElement(my_root, "child2")
etree.SubElement(my_root, "child1")
my_root[0].text = "ch1 text"

my_str = etree.tostring(my_root, encoding="unicode", pretty_print=True)
print(my_str)
print("============================")

print(my_root.findall('.//child1')[0].text)

