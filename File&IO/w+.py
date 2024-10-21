f=open("sample1.txt","w+")      #w+ to write after ceaning the old data of file.
# f.write("hi")
print(f.read())
f.write("This is new data")
f = open("sample1.txt","r")
data = f.read()
print(data)
f.close()