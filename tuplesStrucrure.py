# -------------*** ## INTRO TO TUPLES ## ***-------------
""" Tuples are immutable data structure, similare to "List". its rep by "( )"
Elements can't be chanaged in a tuple.
Can have any no. of items of differebt data types which includes , str,int,floats,dict,set, etc """

# ---------->>>>> EXAMPLE 1
missy = ()
# print(missy)

# ---------->>>>> EXAMPLE 2
numbers = (1.6, 4, 9)
print(numbers)

# ---------->>>>> EXAMPLE 3 >>>>. mixed tuples
info = ("Tibia", 23,("car","fish"), False)
# print(info)

# ---------->>>>> EXAMPLE 3 >>>>. nested tuples
bio_data = (["Winnie", 23, "Dancing"],{"Status": "Single"}, 3.5, (True))
#print(bio_data)


# -------------*** ## TUPLES PACKING AND UNPACKING ## ***-------------
# Tuples Unpacking 
bio_data1, bio_data2, bio_data3, bio_data4 = bio_data
print(bio_data1)
print(bio_data2)
print(bio_data3)
print(bio_data4)

# Tuples Packing and creation 
school_activities = "Gross Practical", "Steepl-chase", "Congress Meeting", "Lunch", "Library"
print(school_activities)
print(type(school_activities))


# Creating a tuples with just an element
name = ("Grace")      # this can't give a tuples
print(type(name))     # instead it resulted into a str

# in getting a tuples for a single element add a ","
name = ("Grace",)
print(name)
print(type(name))



# -------------*** ## ACCESSING TUPLES ITEMS ## ***-------------
# Tuples can be accessed using index()
# ---------->>>>> EXAMPLE 1
x = (False, "God Loves Me", 24, ["Redmi", "Iphone"], 19.98)
print(x[1])
print(x[4])
print(x[5])       #IndexError
print(x["g"])     #TypeError
print(x[-2])        # Negative Index is also allowed


# >>>>>> Tuples Slicing
# this is do to separate element in a tuples from a certain point
# ---------->>>>> EXAMPLE 2
print(x[:])      # this gives the whole element
print(x[1:3])       
print(x[:4])      


# -------------*** ## CHANGING TUPLES ## ***-------------
# since tuples are immutable data structures, it can only experience change if there is a list in the tuple element
# ---------->>>>> EXAMPLE 1
 
# x = (False, "God Loves Me", 24, ["Redmi", "Iphone"], 19.98)
# x[3][1] = "apple"
# print(x)

# ---------->>>>> EXAMPLE 2
# bio_data = (["Winnie", 23, "Dancing"],{"Status": "Single"}, 3.5, (True))
# print(bio_data)

# bio_data[0][0] = "Peter"
# print(bio_data)

# ---------->>>>> EXAMPLE 3 >>>>>> reassignment of Tuples
# it can only occur if the tuples element are numbers
numbers = (6, 8, 11)
print(numbers)
                   #reassignment occure having the same vairable names but differnt element
numbers = (222, 999, 1000)
print(numbers)

# ---------->>>>> EXAMPLE 4 >>>>>>> Tuples concatenation
vowels = ("a", "e", "i", "o", "u")
print(vowels + numbers)

# ---------->>>>> EXAMPLE 5>>>>>>> Repeating Tuples 
print(("movies",) * 4)



