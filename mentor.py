# import json
# d={"1":3,"2":4,"4":5,"6":7}
# with open("mentor.json","w") as jsonfile:
#      json.dump(d,jsonfile)

import json
data =json.load(open("mentor.json"))
print(data)
print(type(data))