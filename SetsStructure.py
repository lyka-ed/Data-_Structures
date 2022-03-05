# **** -------------  SETS --------------****

""" 
Sets are unordered, unindexed & mutable.
No Duplicate
Surrounded by { }, items separated by " , " 
There are mathematical set operations such as u & n
 """

#  ***-------------- Example 1 >>>>> unordered items
first_set = { 21, 22, 777, 101, 0, 54}
print(first_set)    # output is ordered

#  ***-------------- Example 2 >>>>> mixed items
stuff = {3,9, "Cut", ("London", "Paris")}
print(stuff)

#  ***-------------- Example 3 >>>>> no duplicate 
numbers = {1, 2, 3, 4, 5, 6, 4, 5, 6, 7, 8, 9, 10}
print(numbers)    # duplictaed numbers were printed only onces

#  ***-------------- Example 4 >>>>> creating a set from a tuples using set( )
colors = set(("Red","orange", "pink", "green"))
print(colors)         # output in a set format

#  ***-------------- Example 5 >>>>> creating a set from a list using set( )
fruits = set(["Pear", "Apple", "Grape"])
print(fruits)

#  ***-------------- Example 6 >>>>> creating a set from a list using set( )
student_info = set({
    "Jenny": 25,
    "Sandra": 18,
    "Blessed": 23,
})
print(student_info)

#  ***-------------- Example 5 >>>>> set 
