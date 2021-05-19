import json
dict={}
with open("saral7.txt") as file:
    for line in file:
        key,value=line.strip().split(None,1)
        dict[key]=value.strip()
out_file=open("q7.json","w")
json.dump(dict,out_file,indent=4)
out_file.close()
#convert text file data into json file data

