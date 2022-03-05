# --------------------------------------------
# --------- ## Introduction to list ## -------


# List is a data structure.
# it's mutable, ordered, allows duplicate variables.
# Repped by []


#---------Example 1 >>> Simple List
import enum


male_names = ["Alex","John","Brian"]
print(male_names)
ages = [25,23,23]
print(ages)

#---------Example 2 >>> List of lists
books_type =[["horror","dark"], ["romance","adult series"]]
print(books_type)

#---------Example 3 >>> List of lists of lists
mixed_likes = [["sex","money"], 11, 1998,["pizza","chicken"],["sneakers"]]
print(mixed_likes)


#---------Example 4 >>> List of lists merging or concatation 
likes = ["money", "food"]
siblings = ["Ella", "Fedora", "Precious"]
flowers = ["roses", "tulips"]
fav_nums =[11,23,16,8,18]
boolean = [True, False]

info_mixed =likes + siblings + flowers + fav_nums + boolean 
print(info_mixed)


#  ----------- ## The List Method ## --------
# this involves ways of creating a list asides using the []
number = list()
number = list(range(50))
print(number)

a_phone = list("redmi")
print(a_phone)


# --------- Accessing list Items 
information = [23, "Lyka", 11, 344, "Female","Loves Wafer"]
information[3] = "cup"
print(information)

print(information[:4])
print(information[::-1])  # it prints the reverse form of the items in the variable


#  ----------- ## List Unpaacking ## --------
# *******------ Example 1
data_info = [23,"Lyka","Female"]
num1, name, gender = data_info
print(num1)
print(name)
print(gender)

# *******------ Example 2
numbers = [23, 44,67, 5, 4, 3, 2, 1]

num1, num2, num3, *other_num = numbers
print(num1)
print(num2)
print(num3)
print(other_num)


# --------------*** ## LOOPING OVER LISTS ## ***--------
# *******------ Example 1

names = ["Lucy", "Andrea", "Lyka", "Juliana"]

for name in names:
    print(name)

# *******------ Example 2
letters = ["a", "b", "c"]

for letter in enumerate (letters):
    print(letter)

# *******------ Example 3
items =(9, "big")
num1, *word,= items    # list unpacking 
print(num1, *word)

for num1, items enumerate ():
    print(num1,items)


# --------------*** ## MODIFYING LIST ITEMS Part 1 ## ***--------

num_1 = [1, 3, 5, 7, 9, 13]
f_names = ["Sabrina", "Juliana", "Danni", "Andi"]
cars = ["Tesala", "BMW", "Ferari"]

# *******------ Example 1 >>>>>>>>> append()
f_names.append("Lyka")
print(f_names)

# *******------ Example 1 >>>>>>>>> pop()
num_1.pop()
print(num_1)

cars.pop(1)
print(cars)

# *******------ Example 1 >>>>>>>>> insert(index,item)
f_names.insert(3, "Ella")
print(f_names)

# *******------ Example 1 >>>>>>>>> remove()
num_1.remove(7)
print(num_1)

# *******------ Example 1 >>>>>>>>> del statement
del f_names[2:4]
print(f_names)


# --------------*** ## MODIFYING LIST ITEMS Part 2 ## ***--------
# *******------ Example 1 >>>>>>>>> clear()
print(cars.clear())

# *******------ Example 2 >>>>>>>>> join()
print(" ".join(f_names))

# *******------ Example 3 >>>>>>>>> count()
print(num_1.count(3))    # its used accurately when the item is in the list.
print(num_1.count(4))    # a 0 will show up when the item called is not the list.

# *******------ Example 4 >>>>>>>>> index()
fruits = ["mango", "pear", "pine", "peach"]
print(fruits.index("pear"))

if "peach" in fruits:
    print(fruits.index("peaches"))


#  ----------- ## Sorting Lists ## --------

# *******------ Example 1 >>>>>>>>> sort()
numbers = [ 23, 1, 900, 56, 277, 22.1, 762]

print(numbers.sort())  # ascending order
# OR
numbers.sort(reverse=True)    # descending order
print(numbers)


# *******------ Example 2 >>>>>>>>> sorted()
print(sorted(numbers))       # ascending order

print(sorted(numbers, reverse=True))

# *******------ Example 2 >>>>>>>>> complex data

products = [
    ("cup", 5),
    ("Jenny", 25),
    ("Blessed", 23),          # tuples in a list to be sorted 
    ("UV lamp",),
    ("Mug", 9)
]    

products.sort()                # ascending order
print(products)

products.sort(reverse=True)    # descending order
print(products)

#OR

def sort_product(products):
    return products

products.sort(key=sort_product)   





#  ----------- ## LIST COMPREHENSION EXPRESSION Part 1 ## --------
# used to create modified data structures duplicate with literally one line of code.
# it is also an expression for items in a list.

# *******------ Example 1 >>>>>>>>> 

numbers = [23, 5, 46, 11, 9, 100]
cars = ["Benz", "Venza", "Ferari", "Rover"]

numbers1 = [num for num in numbers]
print(numbers1)

numbers1 = [num*2 for num in numbers]
print(numbers1)

numbers1 = [(num/2)*2 for num in numbers]
print(numbers1)

cars2 = [car.lower() for car in cars]
print(cars2)

# *******------ Example 2 >>>>>>>>> tuple in a list
products = [
    ("cup", 5),
    ("Jenny", 25),
    ("Blessed", 23),          
    ("UV lamp", 33),
    ("Mug", 9)
]    

items = [item for item in products]
print(items)

# one can also access a particular item in the list
items = [item[0] for item in products]
print(items)

# in order to access product prices
items = [item[1] for item in products]
print(items)


#  ----------- ## LIST COMPREHENSION EXPRESSION Part 2 ## --------

products = [
    ("cup", 5),
    ("Jenny", 25),
    ("Blessed", 23),          
    ("UV lamp", 33),
    ("Mug", 9)
]    

numbers = [21, 24, 56, 77, 552, 79, 84, 222, 111, 100]

# *******------ Example 2 >>>>>>>>> single conditiions
items = [item[1] for item in products if item[1] > 24]
print(items)

# *******------ Example 2 >>>>>>>>> Two conditiions
org_numbers = [num if num < 200 else num/2 for num in numbers]
print(org_numbers)

org_numbers = [num if num > 100 else num/2 for num in numbers]
print(org_numbers)


#  ----------- ## Swapping List Items ## --------
# interchanging items positions in a lists

# *******------ Example 1 >>>>>>>>> 
safe_numbers = [8, 11, 0, 5]
safe_numbers[0], safe_numbers[1], safe_numbers[2], safe_numbers[3] = safe_numbers[2], safe_numbers[0], safe_numbers[3], safe_numbers[1]
print(safe_numbers)

# *******------ Example 2 >>>>>>>>>>
full_names = ["Glory-Lyka", "Edem", "Okposin"]
full_names[0], full_names[1], full_names[2] = full_names[1], full_names[0], full_names[2]
print(full_names)


