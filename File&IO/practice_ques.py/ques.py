#1: create a file"practice.txt" using python.add the following data in it:
with open("practice.txt","w")as f:
    f.write("Hi everyone\nWe are learning file I/O\n")
    f.write("Using Java.\nI like programming in Java.\nalso i love to code in c++")

#2: waf that replace all occurrences of "Java" with "Python" in above file.
def replace_words():
 with open("practice.txt","r")as f:
    data = f.read()
    new_data = data.replace("Java","Python")
    print(new_data)
 with open("practice.txt","w")as f:
    f.write(new_data)
replace_words()

#3: Search if the word "learning" exist in the file or not.
def check_word():
   with open("practice.txt","r")as f:
    data = f.read()
    word = "learning"
    if(word in data):
        print("found")
    else:
        print("not found")
check_word()

#4: waf to find in which line of the file does the word "learning" occur first. print -1 if word not found..
def find_line():
   word = "Python"
   data = True
   line_no = 1
   with open("practice.txt", "r") as f:
     while data:
        data = f.readline()
        if(word in data):
           print(line_no)
           return
        line_no += 1

     return -1
print(find_line())

#5:From a file containing numbers seperated by comma,print the even numbers.
count = 0
with open("sample1.txt","r") as f:
   data = f.read()
   
   nums = data.split(",")
   for val in nums:
      if(int(val) % 2 == 0):
         count += 1
print(count)
  