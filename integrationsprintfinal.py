"""
Integration Final Project
"""
__author__ = "Neve Krajcir"


def integration_sprint_final():
    """
    This is defining my entire code.
    :return: The code.
    """


def valid_number_input():
    """
    The def function is defining the statements below, so they can be called later. The purpose is to make sure their
    input is a whole number.
    :return: It is returning the persons input; once it is valid.
    """
    user_input = None
    validation = True
    while validation:
        try:
            user_input = int(input("Please enter a whole number."))
            validation = False
        except ValueError:
            print("Please enter an integer.")
    return user_input


# The following code is a math quiz using variables and numbers to solve the questions.
print("Hello!, welcome to the quiz.")
print("Basic calculations and problems will have to be solved," + "\nBegin.")
# The string operator "+" is being used to connect the statements together.
# \n tells the computer to start the words after it on a second line.
print("Solve the following problems using the given variables.")

print("x = 4" + " " + "y = 10" + " " + "z = 2")
print("Question 1.", end="\nWhat does x + y = ?\n")
# The "end =" function is telling the line to end and restart on a new line.
x = 4
y = 10
z = 2
addition = input(x + y)
# I am using the plus sign "+" to tell the computer to add the variables x and y.

print("Question 2.\nWhat does z - y = ?")
subtraction = input(z - y)
# The minus sign "-" is to tell the computer to subtract the 2 variables.

print("Question 3.\nWhat does y % x = ?")
modulus = input(y % x)
# The percent sign "%" is telling the computer to find the remainder of the 2 numbers.
print("Solve the following problems using the given variables.")
print("a = 25" + " " + "b = 100" + " " + "c = 5")

print("Question 4.")
print("What does b / a = ?")
a = 25
b = 100
c = 3
division = input(b / a)
# The "/" sign is telling the computer to divide the 2 variables.

print("Question 5.", end="\nWhat does a // c = ?\n")
floorDivision = input(a // c)
# The "//" sign is telling the computer to divide the 2 variables, but exclude the remainder.
print("Solve the following problems using the given variables.")
print("n = 6" + " " + "k = 22" + " " + "m = 2")

print("Question 6.", end="\nWhat does n ** m = ?\n", sep="**")
# The "sep =" function is telling the computer to separate the words under quotes by a "**", the exponential
# operator.
n = 6
k = 22
m = 2
exponential = input(n ** m)
# The "**" sign is telling the computer to raise the variable n to the power of the variable m, exponential.

print("Question 7.", end="\nWhat does k * n = ?\n")
multiplication = input(k * n)
# The "*" sign is telling the computer to multiply the variables.
print("Solve the question using the variables.")
print("x = 37 " * 2)
# The string operator "*" tells the computer to repeat the string, and write x = 37 twice.

print("Question 8.")
print("What is x * x = ?")
x = 37
multiply = input(x * x)
print("You have now completed the quiz,", "Have a great day!", sep=" \n")
print("You will now begin Quiz 2.")

print("Question 1.")
print("Is 2 + 6 > 3?")
left_side = 8
right_side = 3
if left_side <= right_side:
    # If is used to create a condition, you're telling the program to print True, if the condition is met.
    # The <= sign is stating if the left_side if less than or equal to the right_side
    print("False.")
else:
    # The else function is used when the If function condition is not passed.
    print("True.")

print("Question 2.")
print("Is x >= 17? If x = 13.")
# The >= sign is saying x is greater than or equal to 17.
x = 13
while x >= 17:
    # A while loop is a continuous loop until the conditions are no longer met.
    print(x)
else:
    print("False.")

print("Question 3.")
print("What are the multiples of 5, from 0 to 20?")
for x in range(0, 25, 5):
    # A for loop is when you know the amount of inputs.
    # In is used to state the variable in the loop is in the range sequence.
    # Range is a function talking about numbers, the first number is your starting point, the second is the last
    # number, and the third number is the multiples.
    if x % 5 == 0:
        print(x)

print("Question 4.")
print("Is x + y = 18? If x = 10 and y = 10.")
x = 10
y = 10
if x + y == 18:
    # The == sign means the left is equal to the right
    print("True.")
elif x + 9 != 18:
    # The != means the left side is not equal to the right.
    # The elif function is used instead of else, and combines if and else aka elif.
    print("False.")

print("Question 5.")
print("Is this statement true? 2 < x < 20, if x = 12.")
x = 12
if x > 2 and x < 20:
    # And is used for conditions, and the variable must meet both conditions to be true.
    print("True.")
elif not x > 20:
    # The > sign is to say x is greater than 20.
    # Not is used to say the variable can not be a certain value, otherwise not all requirements are met.
    print("Not all requirements meant.")
elif x > 2 or x < 20:
    # Or is used to say that the variable has to be one or the other to be false.
    print("False.")

print("Question 6.")
print("Choose a number, and add it to x + y.\nx = 2 y = 5")
user_input_2 = valid_number_input()
# This is calling the defined function created at the top of the code.
print(7 + user_input_2)

print("Question 7.")
print("Find x - z.")
print("x = 34\n o = 2\n w = 5\n z = o + w")
o = 2
w = 5
x = 34
z = o + w
x -= z
# The -= subtracts z from the total and makes it the new total.
# This is a shortcut operator for total = total - z.
print(x)

print("Question 8.\npart a.")
print("Solve the questions using the variables.")
print("d = 4 e = 7 k = 23")
d = 4
e = 7
k = 23
print("What is d * e = ?")
input(d * e)
print("part b.")
print("What is k - e = ?")
input(k - e)

print("Question 9.")
print("Is p = q?")
print("p = 66 q = 66")
p = 66
q = 66
if p == q:
    # This if statement is setting the condition that if p == q do this.
    print("Yes, p = q.")
print("You have finished Quiz 2.")

if __name__ == "__integrationsprintfinal__":
    integration_sprint_final()
    # This is so the code does not run when imported.
