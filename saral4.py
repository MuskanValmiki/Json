dict={'4': 5,'6': 7,'1': 3,'2': 4}
l1=[]
l2=[]
for key in dict:
    l1.append(key)
    l2.append(dict[key])
for j in range(0,len(l1)):
    for k in range(0,len(l1)):
        if l1[j]<l1[k]:
            l1[j],l1[k]=l1[k],l1[j]
        if l2[j]<l2[k]:
            l2[j],l2[k]=l2[k],l2[j]
d={}
for l in range(0,len(l1)):
    d[l1[l]]=l2[l]
import json
with open("saral4.json","w") as jsonfile:
    json.dump(d,jsonfile)

# print(json.dumps(dict,sort_keys=True,indent=4))
# python to json sort by key 