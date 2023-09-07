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
    # reply_str = c.dispatch(ncclient.xml_.to_ele(save_rpc))
    # print(type(ncclient.xml_.to_ele(save_rpc)))
    # print(reply_str)

    save_rpc_element = etree.fromstring(save_rpc)
    # print(save_rpc_element)
    reply_str = c.dispatch(save_rpc_element)
    print(reply_str)



