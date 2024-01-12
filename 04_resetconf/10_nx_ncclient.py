import ncclient.manager
from lxml import etree

my_filter = '''
<filter>
  <System xmlns="http://cisco.com/ns/yang/cisco-nx-os-device">
    <bd-items/>
  </System>
</filter>
'''

with ncclient.manager.connect(host='192.168.50.245',
                              username='admin',
                              password='Devnet123',
                              port=830,
                              hostkey_verify=False,
                              device_params={'name': 'nexus'}) as c:
    reply_str = c.get_config(source='running', filter=my_filter).xml
config_tree = etree.fromstring(bytes(reply_str, encoding="utf8"))
print(etree.tostring(config_tree, encoding="unicode", pretty_print=True))

