import json

python_dict = {
    "name": "localhost",
    "number": 10,
    "status": True,
    "event": None
}

json_style_string = '''
{
    "name": "localhost",
    "number": 10,
    "status": true,
    "event": null
}
'''

# json.dump()
# with open("00_test_json_string.json", "w") as f:
#     json.dump(python_dict, f, indent=4)

# json.dumps()
# print(type(json.dumps(python_dict)))

# json.load()
# with open("00_test_json_string.json") as f:
#     test_dict = json.load(f)
# print(test_dict)


# json.loads()
new_dict = json.loads(json_style_string)
print(type(new_dict))