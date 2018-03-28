# PRIMITIVE DATA TYPES

# str - string
# bool - boolean
True
False

# int - integer

1
2
3
4

# float
1.0
.9



# COMPLEX DATA TYPES
# list
# dict

# CASTING
# str + int = runtime exception

# SCOPE
# white space in Python defines scope
#     block of code associated with a control structure

# CONTROL STRUCTURES
# --for loops--
# for {variable_name} in <collection>:
#     <action>


name="Ricardo"
if name == "candace":
    print("sup you")

print(name)
if name =="Ricardo":
    print("howdy")


# --logical--
# if <bool>:
#   pass
# elif <bool>:
#   pass
# else <bool>:
#   pass

# -- exception handling --
# try <expression>:
#   <action>
# except [error_type]:
#   <handle error>

# --assignment--
# =

# --comparisons--
# == -> equals
# != -> not equals
# > -> greater than
# >= -> greater than equal
# < -> less than
# <= -> les than equal



"""
  PRACTICE: print each letter in a given string
"""

name='millie'

for rick in name:
    print(rick)


"""
  PRACTICE: create a function that takes an input,
  then prints each character of the input
"""
def print_char(text):
    print(text)
    for character in text:
        print(character)
print_char('millie')

"""
  PRACTICE: create a function that takes two inputs,
  then prints True/False whether or not the first input
  is contained within the second input
"""
text_value = "poop"

def search_string(search_value, text):
    return search_value in text

# print(search_string('a', text_value))  # False
print(search_string('s', text_value))  # True
# print(search_string('S', text_value))  # False


if search_string('r', 'poop'):
    print('found poop')
else:
    print('no poop')

"""
  PRACTICE: Create a diction that contains a list of 
  employee titles stored by the name, then print each record 
  such that each employee name and title is printed on a line
"""