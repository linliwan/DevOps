# 通过路由器获取yang文件

import ncclient.manager
import xml.dom.minidom
from lxml import etree

with ncclient.manager.connect(host='192.168.162.128',
                              username='cisco',
                              password='cisco',
                              port=830,
                              hostkey_verify=False) as c:
    reply_str = c.get_schema('cisco-ia').xml

    my_root = etree.fromstring(bytes(reply_str, encoding="utf8"))
    yang_data = my_root[0].text
    with open('cisco-ia.yang', mode='w') as f:
         f.write(yang_data)

    # doc = xml.dom.minidom.parseString(reply_str)
    # schema_data = doc.getElementsByTagName('data')[0].childNodes[0].nodeValue
    # with open('cisco-ia.yang', mode='w') as f:
    #     f.write(schema_data)



