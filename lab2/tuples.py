#ExampleGet your own Python Server
#Create a Tuple:

thistuple = ("apple", "banana", "cherry")
print(thistuple)
#Example
#Tuples allow duplicate values:

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)
#Example
#Print the number of items in the tuple:

thistuple = ("apple", "banana", "cherry")
print(len(thistuple))
#Example
#One item tuple, remember the comma:

thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))
#Example
#String, int and boolean data types:

tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
#Example
#A tuple with strings, integers and boolean values:

tuple1 = ("abc", 34, True, 40, "male")
#Example
#What is the data type of a tuple?

mytuple = ("apple", "banana", "cherry")
print(type(mytuple))
#Example
#Using the tuple() method to make a tuple:

thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)
#Print the second item in the tuple
thistuple = ("яблоко", "банан", "вишня")
print(thistuple[1])
#Print the last item of the tuple:
thistuple = ("яблоко", "банан", "вишня")
print(thistuple[-1])
#Возвращает третий, четвертый и пятый элемент:
thistuple = ("яблоко", "банан", "вишня", "апельсин", "киви", "дыня", "манго")
print(это число [2:5])
#Example
#This example returns the items from the beginning to, but NOT included, "kiwi":

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])
#Example
#This example returns the items from "cherry" and to the end:

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])
#Example
#This example returns the items from index -4 (included) to index -1 (excluded)

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])
#Example
#Check if "apple" is present in the tuple:

thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")


#ExampleGet your own Python Server
#Convert the tuple into a list to be able to change it:

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)
#Example
#Convert the tuple into a list, add "orange", and convert it back into a tuple:

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)


#Example
#Create a new tuple with the value "orange", and add that tuple:

thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)


#Example
#Convert the tuple into a list, remove "apple", and convert it back into a tuple:

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)


thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) #this will raise an error because the tuple no longer exists


#ExampleGet your own Python Server
#Packing a tuple:

fruits = ("apple", "banana", "cherry")


#Example
#Unpacking a tuple:

fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)


#Example
#Assign the rest of the values as a list called "red":

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)


#Example
#Add a list of values the "tropic" variable:

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)


#ExampleGet your own Python Server
#Iterate through the items and print the values:

thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

#Example
#Print all items by referring to their index number:

thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])


#Example
#Print all items, using a while loop to go through all the index numbers:

thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1 

#ExampleGet your own Python Server
#Join two tuples:

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

#Exercise:
T#he following code example would print the data type of x, what data type would that be?


x = 5
print(type(x))

int
#Exercise:
#Use the correct syntax to print the first item in the fruits tuple.


fruits = ("apple", "banana", "cherry")
print(fruits[0])

#Exercise:
#Use the correct syntax to print the first item in the fruits tuple.


fruits = ("apple", "banana", "cherry")
print(fruits[0])


#Exercise:
#Use the correct syntax to print the number of items in the fruits tuple.


fruits = ("apple", "banana", "cherry")
print(len(fruits))

#Exercise:
#Use the correct syntax to print the number of items in the fruits tuple.


fruits = ("apple", "banana", "cherry")
print(len(fruits))


#Exercise:
#Use a range of indexes to print the third, fourth, and fifth item in the tuple.


fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(fruits[2:5])


