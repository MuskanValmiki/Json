import json
json_obj='{"Name":"Ram","Class":"IV","Age":9 }'
data=json.loads(json_obj)
print(data)
print(type(data))
# json to python convert