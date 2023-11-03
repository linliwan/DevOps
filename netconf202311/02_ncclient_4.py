# 获取接口状态

import ncclient.manager
import xml.dom.minidom


with ncclient.manager.connect(host='192.168.162.128',
                              username='cisco',
                              password='cisco',
                              port=830,
                              hostkey_verify=False) as c:
    reply_str = c.get(filter=('xpath', '/interfaces')).xml
    pretty_xml = xml.dom.minidom.parseString(reply_str).toprettyxml()
    print(pretty_xml)




