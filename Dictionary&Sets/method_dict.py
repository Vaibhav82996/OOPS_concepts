student = {
    "names" : ["aman kumar", "shanu mishra", "akhilesh mishra"],
    "subjects" :{
        "phy" : 33,
        "bio" : 23,
        "maths" : 66
    }
    
}
print(student.keys()) #key()
print(list(student.keys()))
print(len(list(student.keys())))
#value().
print(list(student.values()))

#item().
print(list(student.items()))

#get().
print(student.get("subjects"))
print(student.get("bio")) # it gives none.