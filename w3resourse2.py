# python to json convert
import json
python_obj = {"name": "David","class":"I","age": 6}
json_obj=json.dumps(python_obj)
print(json_obj)
print(type(json_obj))