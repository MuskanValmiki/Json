import json
with open("Q2.json","r") as file:
    data=json.load(file)
    print(data)
    print(type(data))
user=int(input("enter any id number="))
i=0
while i<len(data):
    for key in data[i]:
        if user==data[i]["id"]:
            name=input("enter any name=")
            age=int(input("enter any age="))
            data[i]["name"]=name
            data[i]["age"]=age
            break
    i+=1
print(data)
