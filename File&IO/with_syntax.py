#with syntax..
with open("demo1.txt","r") as f:                #syntax.
    data = f.read()
    print(data)

with open("demo2.txt", "w") as f:
 f.write("This is new data")
f = open("demo2.txt","r")
data = f.read()
print(data)