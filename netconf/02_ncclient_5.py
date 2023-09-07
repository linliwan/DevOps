import ncclient.manager
import xml.dom.minidom


with ncclient.manager.connect(host='192.168.162.128',
                              username='cisco',
                              password='cisco',
                              port=830,
                              hostkey_verify=False) as c:
    reply_str = c.get_schema('cisco-ia').xml
    doc = xml.dom.minidom.parseString(reply_str)
    schema_data = doc.getElementsByTagName('data')[0].childNodes[0].nodeValue
    with open('cisco-ia.yang', mode='w') as f:
        f.write(schema_data)


