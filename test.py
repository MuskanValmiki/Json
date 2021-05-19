d={"1":"one","2":"two","3":"three"}
# for key in d:
import json
with open("test.json","w") as file:
    json.dump(d,file)
# python to json