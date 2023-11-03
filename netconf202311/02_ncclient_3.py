# 过滤配置的四种方法

import ncclient.manager
import xml.dom.minidom
import pathlib

# 1. xpath
# 2. subtree
subtree_filter = '<native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native"><hostname></hostname></native>'
# 3. filter
my_filter = '''
<filter xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
<interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
</interfaces>
</filter>
'''
# 4. external xml file as filter
my_filter_1 = pathlib.Path('01_my_filter.xml').read_text()


with ncclient.manager.connect(host='192.168.162.128',
                              username='cisco',
                              password='cisco',
                              port=830,
                              hostkey_verify=False) as c:
    # reply_str = c.get_config(source='running', filter=('xpath', '/native/router/router-ospf')).xml
    # reply_str = c.get_config(source='running', filter=('subtree', subtree_filter)).xml
    # reply_str = c.get_config(source='running', filter=my_filter).xml
    reply_str = c.get_config(source='running', filter=my_filter_1).xml
    pretty_xml = xml.dom.minidom.parseString(reply_str).toprettyxml()
    print(pretty_xml)






