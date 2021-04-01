# String: ordered, immutable, text representation

myString = "Hello world!"
print(myString)

print(myString[0])
print(myString[-1])
print(myString[3:-1:2])

# String is immutable, cant change a charatcer at a position

# concatenate
greeting = "Hello"
name = "Mani"
print(greeting + " " + name)

# iterate
for ch in greeting:
    print(ch)

# in statement
if 'ell' in greeting:
    print("yes")
else:
    print("no")

# trimming a string
myString = "     Hello    "
print(myString.strip())


myString = "Hello World"

# upper and lower case
print(myString.upper())
print(myString.lower())


# Functions
# startswith(str) -> return boolean
# endswith(str) -> return boolean
# find(str) -> return index
# count(str) -> return occurences
# replace(str, newStr) -> return new string
# split(delimiter) -> return list
# join(list) -> return new string of concatenated list items

# String formatting
var = "Mani"
myString = "The name is %s" % var
print(myString)
# Using format()
myString = "The name is {}".format(var)
print(myString)
# Using f
myString = f"The name is {var}"
print(myString)
