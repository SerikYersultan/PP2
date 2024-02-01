#ExampleGet your own Python Server
print(10 + 5)
#Example
#Parentheses has the highest precedence, meaning that expressions inside parentheses must be evaluated first:

print((6 + 3) - (6 + 3))
#Example
Multiplication * has higher precedence than addition +, and therefor multiplications are evaluated before additions:

print(100 + 5 * 3)
#Example
Addition + and subtraction - has the same precedence, and therefor we evaluate the expression from left to right:

print(5 + 4 - 7 + 3)
#Exercise:
#Multiply 10 with 5, and print the result.
print(10 * 5)
#Exercise:
#Divide 10 by 2, and print the result.
print(10 / 2)
#Exercise:
#Use the correct membership operator to check if "apple" is present in the fruits object.
fruits = ["apple", "banana"] 
if "apple" in fruits:
print("Yes, apple is a fruit!")
#Exercise:
#Use the correct comparison operator to check if 5 is not equal to 10.
if 5 != 10:
  print("5 and 10 is not equal")
#Exercise:
#Use the correct logical operator to check if at least one of two statements is True.
if 5 == 10 or 4 == 4:
    print("At least one of the statements is true")