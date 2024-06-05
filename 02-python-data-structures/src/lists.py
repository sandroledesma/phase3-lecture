my_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

# TODO Test if an element exists in `my_list`
'a' in my_list

# TODO Add element to the end
my_list.append('h')

# TODO Insert element at an index
my_list.insert(0, 'x')

# TODO Merge two lists together
[ 1, 2 ] + [ 3, 4 ] 
[ 1, 2 ] + my_list

# TODO Duplicate a list
my_list.copy()

# TODO Index lookup
my_list[0]
my_list[-1]

# TODO Slice
my_list[0:3]

# TODO Get length
len(my_list)

# TODO Get min/max
min(my_list)
max(my_list)

# TODO Find index of an element
my_list.index('b') # only finds first instance

# TODO Count number of instances of an element
my_list.count('b')

# TODO Remove element from list
my_list.pop() # removes last element
my_list.pop(2) # removes element on index 2

# TODO Sorting (with an without a key)
my_number_list = [1, 5, 4, 2, 8]
my_number_list.sort() # [1, 2, 4, 5, 8]
my_number_list.sort(reverse=True) # [8, 5, 4, 2, 1]

# TODO sorted() vs .sort(), does not manipulate original list (versus sort())
sorted(my_list)
sorted(my_list, reverse=True)