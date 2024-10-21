#1: R+
f=open("sample1.txt","r+")      #r+ change the starting value of file which already exists.
f.write("hi")
print(f.read())
f.close()
