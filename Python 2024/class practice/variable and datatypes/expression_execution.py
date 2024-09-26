#rule : 1 , strings & numeric values can operate together with *
a,b = 2,4
txt ="xxx"
print(2*txt*4)

#rule : 2 , strings & strings can operate with +
A,B ="3",4
Txt ="@"
print((A+Txt)*4)

#rule :3 , numeric values can operates with all arithmatic operators.
A,B,C = 2,3,4
print(A+B*C)

#rule : 4 , arithmatic expression with integer and float will result in float
A,B = 10,5.0
c=A*B
print(c)

#rule : 5 , result of devision operator with two integers will be float
A,B = 1,2
c= A/B
print(c)

#Rule : 6 , integer division{//} or floor division, with float and  int will give int display as float.
#( It wil convert into smaller value like the answer of 1.5//3 is 0.5 but it will give 0.0)
#(whether if the answer will 1.7 then it will give 1.0)
A,B = 1.5,3
c = A//B
print(c)