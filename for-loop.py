##For Loop

#-In a for loop, we will know in advance how many times the loop will need to iterate because we will be working on a collection with predefined length.
#With for loops, on each iteration, we will be able to perform an action on each element of the action.
#In for loop we already know how many times we are going to loop.
#By default we already know how many times this loop is going to run.
#Example : "Count 1 to 20" or "Print 1 to 10"

#Print 
for i in range (10):
    print(i)  #"i" is a variable.

#Why dont we have "10" at terminal after print
# ---By counting, when we start counting indexing in programming  we start from "0"
#0 is the first index.
#The range should be 10 values. So you get the value ar the terminal to be (0 - 9)

#However you Can increment 1 to get all the values at the terminal which will be (1-9)
#i.e
for i in range (10):
    print(i+1)


