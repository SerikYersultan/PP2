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


#