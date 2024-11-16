##What if we have multiple conditions we use if elif statement
#It means that it's else if.
#The shot form for else if is "elif" which is used in multiple conditions.
#Examples grading systems -someone can scpre A, B, C , D

a = 200
b = 33

if b > a:
    print("B is greater than A")
elif a == b:  #what if a = b meaning that a has the same value as b. We can print below statement.
    print("A & B are equal values")
    #what if b is not greater than a and they are not equal. That means that b can be less than a. Then we will write another condition using else block.
else:
    print("A is greater than B")