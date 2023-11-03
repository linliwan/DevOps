# 保存配置

import ncclient.manager
import ncclient.xml_
from lxml import etree

save_rpc = '''
<cisco-ia:save-config xmlns:cisco-ia="http://cisco.com/yang/cisco-ia" />
'''


with ncclient.manager.connect(host='192.168.162.128',
                              username='cisco',
                              password='cisco',
                              port=830,
                              hostkey_verify=False) as c:
    dispatch_msg = ncclient.xml_.to_ele(save_rpc)
    dispatch_msg_1 = etree.fromstring(save_rpc)
    # reply_str = c.dispatch(dispatch_msg)
    # print(reply_str)
    print(dispatch_msg)
    print(dispatch_msg_1)




