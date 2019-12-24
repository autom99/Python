from typing import Tuple

print("Test")

x = y = z = 50
print("idle")
print(y)
print(z)

a, b, c = 5, 10, 15
print("a + b + c : ", a + b + c)

A = 10
b = "Hi Python"
c = 10.5
print(type(a))
print(type(b))
print(type(c))

str1 = 'hello javatpoint'  # string str1
str2 = ' how are you'  # string str2
print(str1[0:2])  # printing first two character using slice operator
print(str1[4])  # printing 4th character of the string
print(str1 * 2)  # printing the string twice
print(str1 + str2)  # printing the concatenation of str1 and str2

# List
# Lists are similar to arrays in C. However; the list can contain data of different types. The items stored in the list are separated with a comma (,) and enclosed within square brackets [].
# We can use slice [:] operators to access the data of the list. The concatenation operator (+) and repetition operator (*) works with the list in the same way as they were working with the strings.

l = [1, "hi", "python", 2]
print(l[3:])
print(l[0:2])
print(l)
print(l + l)
print(l * 3)

# Tuple
# A tuple is similar to the list in many ways. Like lists, tuples also contain the collection of the items of different data types. The items of the tuple are separated with a comma (,) and enclosed in parentheses ().
# A tuple is a read-only data structure as we can't modify the size and value of the items of a tuple.

# Let's see a simple example of the tuple.

t: Tuple[str, str, int] = ["hi", "python", 2]
print(t[1:])
print(t[0:1])
print(t)
print(t + t)
print(t * 3)
print(type(t))
t[2] = "hi"


#Dictionary
#Dictionary is an ordered set of a key-value pair of items. It is like an associative array or a hash table where each key stores a specific value. Key can hold any primitive data type whereas value is an arbitrary Python object.
#The items in the dictionary are separated with the comma and enclosed in the curly braces {}.

#Consider the following example.

d = {1:'Jimmy', 2:'Alex', 3:'john', 4:'mike'}
print("1st name is "+d[1])
print("2nd name is "+ d[4])
print (d)
print (d.keys())
print (d.values())