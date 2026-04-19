# --------------------------------------------
# Name:
# Date:
# Program: Chapter 9 Practice
# Description:
# Complete each section by following the
# directions in the comments.
# --------------------------------------------

# ------------------------------------------------
# Practice 1: Creating and Using a Dictionary
# ------------------------------------------------
# TODO:
# 1. Create a dictionary named student with the
#    following key-value pairs:
#      'name'  : 'Alex Johnson'
#      'grade' : 92
#      'major' : 'Computer Science'
# 2. Print the entire dictionary
# 3. Print just the value associated with 'name'
# 4. Print just the value associated with 'grade'
# 5. Use the in operator to check if 'major' is
#    a key in the dictionary and print the result
student = {
'name': 'Alex Johnson',
'grade': 92,
'major': 'Computer Science'
}

print(student)
print(student['name'])
print(student['grade'])
result = 'major' in student
print(result)



print()  # blank line

# ------------------------------------------------
# Practice 2: Modifying a Dictionary
# ------------------------------------------------
# TODO:
# 1. Create a dictionary named inventory with the
#    following key-value pairs:
#      'apples'  : 50
#      'bananas' : 30
#      'oranges' : 20
# 2. Add a new key-value pair: 'grapes' : 15
# 3. Update the value for 'apples' to 65
# 4. Delete the key-value pair for 'bananas'
#    using the del statement
# 5. Print the final dictionary
# 6. Print the total number of items using len()
inventory = {
    'apples': 50,
    'bananas' : 30,
    'oranges' : 20
}

inventory['grapes'] = 15
inventory['apples'] = 65
del inventory ['bananas']

print(inventory)
print(len(inventory))

print()

# ------------------------------------------------
# Practice 3: Iterating Over a Dictionary
# ------------------------------------------------
# TODO:
# 1. Create a dictionary named scores with at least
#    4 student names as keys and their test scores
#    as values (integers)
# 2. Use a for loop with the keys() method to print
#    each student's name
# 3. Use a for loop with the values() method to print
#    each score
# 4. Use a for loop with the items() method to print
#    each name and score together on one line
#    (e.g. "Alice scored 88")

scores = {
    'Alice' : 88,
    'jake' : 92,
    'will' : 67,
    'scoma' : 44
}
print("Student Names ")
for name in scores.keys():
    print(name)

print("\nScore ")
for score in scores.values():
    print(score)

print("Score Summary ")
for name, score in scores.items():
    print(f"{name} scored {score}")




print()

# ------------------------------------------------
# Practice 4: Creating and Using a Set
# ------------------------------------------------
# TODO:
# 1. Create a set named colors using the set()
#    function with this list:
#    ['red', 'blue', 'green', 'red', 'blue']
# 2. Print the set (notice duplicates are removed)
# 3. Use add() to add 'yellow' to the set
# 4. Use discard() to remove 'green' from the set
# 5. Print the length of the set using len()
# 6. Create a second set named warm with the values:
#    {'red', 'orange', 'yellow'}
# 7. Print the union of colors and warm
# 8. Print the intersection of colors and warm

colors = set(['red', 'blue', 'green', 'red', 'blue'])
print(colors)

colors.add('yellow')
colors.discard('green')
print(len(colors))

warm = {'red', 'orange', 'yellow'}
print(colors.union(warm))
print(colors.intersection(warm))

print()

# ------------------------------------------------
# Practice 5: Debug the Dictionary Program
# ------------------------------------------------
# TODO:
# The program below is supposed to:
# - Create a dictionary of phone contacts
# - Add a new contact
# - Print each contact name and number
# - Safely look up a number using get()
#
# There are 3 errors in this code.
# Fix them so the program works correctly.


contacts = {'Alice': '555-1234', 'Bob': '555-5678'}

contacts['Charlie'] = '555-9999'

for name, number in contacts.items():
    print(name + ': ' + number)

result = contacts.get('Diana', 'Not found')
print(result)

print()
