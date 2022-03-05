# ---------------** ## INTRODUCTION TO DICTIONARIES ## **--------
# Dictionaries are collection of key value pairs. It's mutable, no duplicate.
# Unordered and rep. with a {}

# ----------->>>>> EXAMPLE 1 >>> Basic Dic

class_info ={
    "Jennifer": 25,
    "Blessed": 23,
    "Lyka": 24,
    "Ashi": 30,
}

print(class_info)


# ----------->>>>> EXAMPLE 2 >>>

patientsInfo ={
    "Name": "Brian",
    "Age": 24,
    "Address": "Uyo, AKS",
    "Job": "Photographer"
}
print(patientsInfo)

# ----------->>>>> EXAMPLE 3 >>> creating a dic. using dict()
animals_name = dict(parrot="Mr.P", dog="Gatoso & Rexy")
print(animals_name)


# ---------------** ## Accessing Dictionary Key Value ## **--------
# ----------->>>>> EXAMPLE 4 >>> accessing an item in the dict.
print(patientsInfo["Age"])
print(patientsInfo["Job"])

# ----------->>>>> EXAMPLE 5 >>> adding key value to the dic
patientsInfo["Favourite Color"] = "White", "Brown"
patientsInfo["Favourite Food"] = "Cat-fish pepper soup"
print(patientsInfo)

# ************ ## Dictionary Methods Part 1 ## *************

employee_info = {
    "Name": "Glory-Lyka",
    "Surname": "Edem",
    "Age": 24,
    "Address": "Calabar, Cross-River State",
    "Job": {"Newbie Developer", "Forex Trader"},
    "Hobbies": {"Watching Series", "Music","Playing Chess","Surfing the Web"},
    1998: "Date of Birth",
    "Single": True,
    "Favorite Song": {"Rise Up", "Reflection", "Brave,loyal & Strong"},
    "Best Friend": {"hahaha, are really expecting a response."},
    "Special One": None
} 

# ----------->>>>> EXAMPLE 6 >>>>>> clear()
#This clears data
print(employee_info.clear())

# ----------->>>>> EXAMPLE 6 >>>>>> copy()
# create another copy of the dict. content without an alteration to the original.
alex_info = employee_info.copy()
print(alex_info)

# ---------->>>>> EXAMPLE 7 >>>>>> 
# changes can be made to any of the keyvalues.
alex_info["Name"]

# ---------->>>>> EXAMPLE 8 >>>>>> fromkeys()
# fromkeys() changes other data structure to a dictionary data structure
vowels = ["a", "i", "e", "o", "u"]
nums = [1, 2]

vowel1 = dict.fromkeys(vowels)
print(vowel1)

words_mixed = dict.fromkeys(vowels,nums)
print(words_mixed)

print({}.fromkeys(employee_info))

# ---------->>>>> EXAMPLE 8 >>>>>> items()
print(employee_info.items())
# OR

# ---------->>>>> EXAMPLE 9 >>>>>> del statement
del employee_info["Hobbies"]
print(employee_info.items())

# ---------->>>>> EXAMPLE 10 >>>>>> keys()
del employee_info["Age"]
print(employee_info.keys())

# ---------->>>>> EXAMPLE 11 >>>>>> values()
print(employee_info.values())

del employee_info["Favorite Song"]
print(employee_info.values())

#---------->>>>> EXAMPLE 12 >>>>>> popitem()
# its pops i.e removes the last item in a dictionary 
print(employee_info.popitem())
print(employee_info)

# ---------->>>>> EXAMPLE 13 >>>>>> setdefault()
""" N/B : when you pass in a key that doesnt exist in setdefault(), it create it and store in the dict
but when you pass in a key that exist in the dic, it returns the value.print """

print(employee_info.setdefault("Name"))

print(employee_info.setdefault("Color", "red"))
print(employee_info)

# ---------->>>>> EXAMPLE 13 >>>>>> pop()
# Case #1
# popping a key that exist
targetOne = employee_info.pop("Age")
print(targetOne)
print(employee_info)

# Case #2
# popping a key  with a value that doesnt exists.
target2 = employee_info.pop("Smoking", "Yes")
print(target2)
print(employee_info)

# Case #3
# popping a key that doesnt exist without a value
target3 = employee_info.pop("Allergies")
print(target3)
print(employee_info)

# Case #4
# popping a key that exist in the dict with a differnt value
target4 = employee_info.pop("Surname", "COCO")
print(target4)
print(employee_info)

#---------->>>>> EXAMPLE 13 >>>>>> update()
#Case #1 - adding a new dict to the previous one
fave = {"Favourite Movie": "I am Alive"}
employee_info.update(fave)
print(employee_info)

#Case #2 - giving a key a new value and it gets updated
new_key = {"Favourite Movie": "Ghost"}
employee_info.update(new_key)
print(employee_info)

#Case #3 - when a tuples is passed
employee_info.update(Nick_name="Ply")
print(employee_info)



# ************ ## DICTIONARY COMPREHENSION ## *************


# ---------->>>>> EXAMPLE 1 
# making use of for loop to iterates
angles_1 = {}
for y in range(5):
    angles_1[y] = (((y * 5) / 2) + 12) - (2.4 / 1.2) * 6

print(angles_1)    

# a one line code for that above

angles_1 = {y:(((y * 5) / 2) + 12) - (2.4 / 1.2) * 6 for y in range(5)}
print(angles_1)

# ---------->>>>> EXAMPLE 2
# Items prices in naira
naira_price = {"egg": 70, "bread": 120, "biscuit": 100}
naira_to_dollar = 496
new_price = {item:value * naira_to_dollar for(item, value) in naira_price.items()}

print(new_price)

# ---------->>>>> EXAMPLE 3 >>>>>>> using if conditional to control flow of logic

student_dict ={"Bianca": 22, "Pete": 28, "Love": 19, "Alex": 25, "Stan": 50}
even_dict = {x:y for (x,y) in student_dict.items() if y % 5 == 0}

print(even_dict) 






