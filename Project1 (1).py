#PROJECT 1
#AUTHOR: Aidan Hickey

#Covers material from weeks 1, 2, and 3

#For the Autograder:
# Make sure you are only printing out exactly what we say should be printed
# before submission 

#TODO 1: Complete this line so the words Hello World will be printed to the terminal
# Make sure it is written exactly the same, 
# capital H and W, one space between them, 
# no punctuation
#You should only replace/change the ??? line
print('Hello World')

#TODO 2: Fix all the bugs in this code, so the phrase:
#       Rock 'n' Roll
# is printed out. VSCode can help you find almost every issue
print('Rock \'n\' ''Roll')

#TODO 3: Complete the following line, z holds the value 4 at the end
# note: the phrase 'assert' will print "Failed" if z doesn't equal 4
#You should only replace/change the ??? line
x=10 
x = 0
x += 4
y = x/2
z = y*2
try:
    assert(z == 4) #stop working if z does not equal 4, keep working if it does
    print("TODO2 Completed")
except:
    print("TODO2 Failed")

#TODO 4: make the following statements that are FALSE comments
# this will stop them from being printed out
print('Before you submit code, you should always try to run it yourself first')
#print('Strings and Integers are the only data types in python')
#print('Strings can only represent alpha-numeric characters')
print('You can use * with a string and a integer, and + with two strings')
#print('Writing in the shell is equivalent to writing in a python file')
#print('Variables in Python are used to solve for unknown values, like in Algebra')

#TODO 5: Change only the parentheses to the following math 
#   so that the number 13 gets saved in the variable final
final = (2)*(5-3+10)//2+(1)
print("Final is ", final)

#TODO 6: In a single line, print the following statement using a single f-string:
#My name's Trent, I'm 19 and I never learned how to read: True
#   You must use all the provided variables. Make sure spelling, punctuation, and spacing match identically
# You should only replace/change the ??? line
a = "Trent"
b = 19
c = True 
print(f'My name\'s {a}, I\'m {b} and I never learned how to read: {c}')
#TODO 7: Remove the following items from the list lis using the most appropriate method
#       7 by index
#       'Akita' by value
#       the last item in the list without providing an index or a value
#     you should do this in three different lines, in the ??? spaces provided
lis = ['Akita',True,7]
lis.pop(2)
lis.remove('Akita')
lis.pop()
print(lis)

#TODO 8: Change the print statement, so only the 2nd item in the list (@ index 1) is printed
    #HINT: the shortest solution only adds three characters to the line
fruits = ['Apples', 'Grapes', 'Durians','Strawberries']
print('My favorite fruit is: ' + fruits[1])

#TODO 9:9: Create a list called animals. When creating the list, start it with one item. Then append a second item..
#  Start the list with "Turtles". Append "Frogs" in the next line      
#You should only replace/change the ??? lines
lis_TODO= ["Turtles"]
lis_TODO.append("Frogs")
print('Animals: ', lis_TODO)

#TODO 10: Sort the list fruits from TODO 8 alphabetically, you can do this:
# manually removing and adding items until the list is in the right order
# or you can use a built-in python function
#You should only replace/change the ??? line
fruits.sort()
print("Sorted fruits: ", fruits)


#------------------------------------
#--------EXTRA CREDIT----------------
#------------------------------------
#TODO 11: write a single line of code that allows us to use python's preinstalled math functions
import math

#TODO 12: Fill in the two ??? on the following two lines
#      remove the comment symbol on the print 4 lines below if you attempt
#   The first should calculate the value of 5! (5 factorial) using only default python methods
#   the second should use the math library's factorial() function to calculate 5!
#   information about factorials found here: https://www.mathsisfun.com/numbers/factorial.html
#   remove the comment on the print 4 lines below if you attempt
fac_by_hand = 2
math_fac = 1
print(str(fac_by_hand) + ' is equal to ' + str(math_fac))
print("TODO 12 Attempted")

#TODO 13: Pick a different function from the math library, properly use it, and print out the results 
#   remove the comment symbol on the print 3 lines below if you attempt
# This website provides a list as well as example usage: https://www.w3schools.com/python/module_math.asp
math.cos(0)
print(math.cos(0))
#print("TODO 13 Attempted")