#Types of files..
#1: text files: txt , docx , .log etc
#2: binary file: png , image , mp3 ,jpeg, mp4 etc.
#now we will access data from our demo1.txt file.

#Methods in file I/O
#1: R : open for reading.
#2: W : open for writing, trucating the file first.\
#3: x : create a new file and open it for writing.
#4: A : open for writing, appendiing too the end of the file if it existe.
#5: B : binary mode.
#6: T : text mode.
#7: + : open a disc file for updating(reading and writing).

f = open("demo1.txt", "r")
data = f.read()
print(data)
print(type(data))
f.close()

#to read one line at a time.
f = open("demo1.txt", "r")
line1 = f.readline()
print(line1)

line2 = f.readline()
print(line2)
f.close()