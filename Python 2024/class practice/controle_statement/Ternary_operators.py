#single line conditional statements or called ternary operators
#<var> = <val1> if <condition> else<val2> SYNTAXT....
diet = input("Enter your diet food : ")
Food = "You are eating healthy" if diet == "fruits" or  diet == "vegitables"  else "You are not eating healthy"
print(Food)  
#second method
#<stt1> if <condition> else <stt2>
food = input("Enter your dish : ")
print("sweets") if food =="cake" or food == "jalebi" else print("non-sweets")