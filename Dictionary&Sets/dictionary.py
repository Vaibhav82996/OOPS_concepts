#Dictionaries are used to store data values in key.value pairs they are unorderd,mutable(changeble)
#  & don't allow duplicate keys.
info = {
    "key" : "value",
    "name" : "data science",
    "age" : 35,
    "is adult" : True,
    "marks" : 33.22,
    "subjects" : ["python", "c", "java"],
    "topics" : ("dict","set")
}
print(type(info))
print(info["name"])
print(info["age"])
info["name"] = "Vaibhav"
info["surname"] = "pandey"      #we can create a new key also. 
print(info)

#we can add a null dictionary and then add keys into it.
null_dictionary = {}
null_dictionary["new name"] = "akshay"
null_dictionary["new surname"] = "pandit"
print(null_dictionary)