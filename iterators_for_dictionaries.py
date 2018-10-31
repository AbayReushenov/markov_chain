d = {
  "Name": "Guido",
  "Age": 56,
  "BDFL": True
}
print d.items()
# => [('BDFL', True), ('Age', 56), ('Name', 'Guido')]
print d.keys()
# ['BDFL', 'Age', 'Name']
print d.values()
# [True, 56, 'Guido']
print
print ". . . . . . . . . . . . . . . . . . . . "
for number in range(5):
  print number,

print
print ". . . . . . . . . . . . . . . . . . . . "
d = {
  "name": "Eric",
  "age": 26
}
for key in d:
  print key, d[key],

for letter in "Eric":
  print letter,  # note the comma!

print
print ". . . . . . . . . . . . . . . . . . . . "

my_dict = {
  'name': 'Nick',
  'age':  31,
  'occupation': 'Dentist',
}
for key in my_dict:
  print key , ' ' , my_dict[key]

print ". . . . . . . . . . . . . . . . . . . . "

evens_to_50 = [i for i in range(51) if i % 2 == 0]
print evens_to_50
# -------
doubles_by_3 = [x * 2 for x in range(1, 6) if (x * 2) % 3 == 0]
print doubles_by_3
# Complete the following line. Use the line above for help.
even_squares = [x ** 2 for x in range(1 , 12) if x % 2 == 0 ]

print even_squares

#----
cubes_by_four = [chislo ** 3 for chislo in range(1,11) if chislo ** 3 % 4 == 0]
print cubes_by_four
#----
my_list = range(1, 11) # List of numbers 1 - 10

# Add your code below!
print my_list[::2]
# ----
my_list = range(1, 11)

# Add your code below!
backwards = my_list[::-1]
print my_list
print backwards
# -----
to_one_hundred = range(101)
# Add your code below!
backwards_by_tens = to_one_hundred[::10]
print backwards_by_tens
# -----
to_21 = range(1,22)
odds = to_21[::2]
middle_third = to_21[7:14]
print to_21
print odds
print middle_third
#-----
my_list = range(16)
print filter(lambda x: x % 3 == 0, my_list)
#-----
languages = ["HTML", "JavaScript", "Python", "Ruby"]

# Add arguments to the filter()
print filter(lambda x: x == "Python" , languages)
# ----
squares = [z **2 for z in range(1,11)]
print filter(lambda y: y in range(30,71), squares)
#------

movies = {
  "Monty Python and the Holy Grail": "Great",
  "Monty Python's Life of Brian": "Good",
  "Monty Python's Meaning of Life": "Okay"
}
for key in movies.keys():
  print key + "  " + movies[key]
print movies.items()
# ----
threes_and_fives = filter(lambda x: (x % 3 == 0 or x % 5 == 0), range(1,16) )
print threes_and_fives
#--------
garbled = "!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI"
message = garbled[::-2]
print message
# -----
garbled = "IXXX aXXmX aXXXnXoXXXXXtXhXeXXXXrX sXXXXeXcXXXrXeXt mXXeXsXXXsXaXXXXXXgXeX!XX"
message = filter(lambda x: x != "X" , garbled)
print message

