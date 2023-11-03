from lxml import etree

my_root = etree.Element("root")
# method1
child1 = etree.Element("child1")
my_root.append(child1)
# method2
etree.SubElement(my_root, "child2")

my_root[0].text = "ch1 text"

my_str = etree.tostring(my_root, encoding="unicode", pretty_print=True)
print(my_str)
print("============================")

print(my_root[0].text)