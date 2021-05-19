import json
dict={"a":"muskan","b":78,"c":[1,2,3,4,5],"d":True}
data=json.dumps(dict)
print(data)
print(type(data))
print(type(dict["a"]))
print(type(dict["b"]))
print(type(dict["c"]))
print(type(dict["d"]))
# json string check complex 