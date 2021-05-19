import json 
dict={"shopping_list":{"chaco":"15","Biscuits":"50","Diary_milk":"30","ice_cream":"20",}}
print("shoping_list=",dict["shopping_list"])
add=input("if you want to add=")
user=input("enter what you want=")
item=int(input("enter how much item you want"))
for key in dict:
    for i in dict[key]:
        if user==i:
            dict[key][i]=int(dict[key][i])-item
    if "y"==add:
            dict[key][user]=str(item)
print(json.dumps(dict,indent=4))

