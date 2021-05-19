import json
a=["neelam","programer","24","2400"]
b=["komal","trainer","24","20000"]
c=["anuradha","HR","25","40000"]
d=["Abhishek","manager","29","63000"]
e=["name","designation","age","salary"] 
d1={}
d2={}
d3={}
d4={}
dict={}
i=0
while i<len(a):
    j=0
    while j<len(e):
        d1[e[j]]=a[j]
        d2[e[j]]=b[j]
        d3[e[j]]=c[j]
        d4[e[j]]=d[j]
        j+=1
    dict["emp1"]=d1
    dict["emp2"]=d2
    dict["emp3"]=d3
    dict["emp4"]=d4
    i+=1
data=json.dumps(dict,indent=4)
print(data)
print(type(data))