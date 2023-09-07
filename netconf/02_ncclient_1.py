import ncclient.manager

# c = ncclient.manager.connect(host='192.168.162.128',
#                              username='cisco',
#                              password='cisco',
#                              port=830,
#                              hostkey_verify=False)
# print(type(c.server_capabilities))
# for cap in c.server_capabilities:
#     print(cap)
#
# c.close_session()

with ncclient.manager.connect(host='192.168.162.128',
                              username='cisco',
                              password='cisco',
                              port=830,
                              hostkey_verify=False) as c:
    with open('01_cap.txt', mode='a') as f:
        for cap in c.server_capabilities:
            f.write(cap + '\n')

