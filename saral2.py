import json
dict={"Name":"muskan","Class":"12th","Age":18 }
# with open("saral2.json", "w") as outfile: 
#     json.dump(dict, outfile)
data=json.dumps(dict)
print(data)
print(type(data))
# python to json convert