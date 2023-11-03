# 编辑配置

import ncclient.manager

netconf_data = '''
<config xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
<interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
<interface>
    <name>Loopback10</name>
    <type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">ianaift:softwareLoopback</type>
    <enabled>true</enabled>
    <ipv4 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip">
        <address>
            <ip>3.3.3.3</ip>
            <netmask>255.255.255.0</netmask>
        </address>
    </ipv4>
</interface>
</interfaces>
</config>
'''

netconf_data_1 = '''
<config xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
<interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
<interface operation='delete'>
    <name>Loopback10</name>
</interface>
</interfaces>
</config>
'''

with ncclient.manager.connect(host='192.168.162.128',
                              username='cisco',
                              password='cisco',
                              port=830,
                              hostkey_verify=False) as c:
    reply_str = c.edit_config(netconf_data_1, target='running')
    print(reply_str)
