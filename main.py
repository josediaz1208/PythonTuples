# In Python, tuples are allocated large blocks of memory with lower overhead,
# since they are immutable; whereas for lists, small memory blocks are allocated.
# Between the two, tuples have smaller memory.
# This helps in making tuples faster than lists when there are a large number of elements.
# A tuple represents a sequence of any objects separated by commas and enclosed in parentheses.
# A tuple is an immutable object, which means it cannot be changed,
# and we use it to represent fixed collections of items.

# let's start with some basic examples of tuples
basic_tuple = (1, 2, 3, 4, 5)
print(basic_tuple)

# we can create a tuple with different types inside it
different_tuple = (1, "Jose", [1, 2, 3], (1, 2))
print(different_tuple)
# brings the type of the object
print(type(different_tuple))

# As mentioned earlier, because a tuple is a sequence of objects, we can access these objects through indexing.
# As with strings, the index of the first element is 0, the second element is 1, and so on.
print("This is the first argument", different_tuple[0])

# getting the last element
print("This is the last argument of the tuple", different_tuple[-1])


# get the data type of the second element of the tuple
print("This is the data type of the second element of the tuple", type(different_tuple[1]))

# how to get the first element from the tuple inside the tuple
print("The value of the tuple inside the tuple", different_tuple[2][0])









