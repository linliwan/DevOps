# 获取完整的配置

import ncclient.manager
import xml.dom.minidom


with ncclient.manager.connect(host='192.168.162.128',
                              username='cisco',
                              password='cisco',
                              port=830,
                              hostkey_verify=False) as c:
    reply_str = c.get_config(source='running').xml
    with open('01_all_config.xml', mode='w') as f:
        f.write(reply_str)
    pretty_xml = xml.dom.minidom.parseString(reply_str).toprettyxml()
    with open('01_all_config_pretty.xml', mode='w') as f:
        f.write(pretty_xml)




