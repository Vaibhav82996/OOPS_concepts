#string functions.
str = "my name is vaibhav apandey" #check or give boolean value whether the string ends with that alphabets or not
print(str.endswith("dey"))

str1 = "my name is vaibhav apandey" #capital the first striing of sentences
print(str.capitalize())

str2 = "my name is vaibhav apandey" #it replace the perticular word or letter from another string.
print(str.replace("vaibhav" , "vr"))

str3 = "my name is vaibhav apandey" #it find the word or letter from the string.
print(str.find("name"))

str4 = "my name is vaibhav pandey" #it count the word or letter from string ,how many times it was repeated.
print(str.count("a"))  

#question
str9 = input("Enter your name : ")
print(len(str9))

str8 = "hi my name is vaibhav"
print(str8.count("i"))