my_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

# simple for loop (no indices)
for item in my_list: # for each item in the list
    print(item)

# for loop with indices (start, stop)
for i in range(0, 5): 
    print(i, my_list[i]) 

# for loop with length function (start, stop)
for i in range (0, len(my_list)): # returns how ever long my_list is 
    print(i, my_list[i])

#transorm list to a new list 
my_new_list = [1, 2, 3, 4, 5]

def double(numbers):
    """Double every number in numbers"""
    new_list = [] # create a new empty list
    for num in numbers: # loop over every number (for each num in numbers) 
        new_num = num * 2 # multiplies each number by 2 (transform the number)
        new_list.append(new_num) # add to new_list
    return new_list

#filter
another_new_list = [1, 2, 3, 4, 5, -1, -2, 6, 7, -3, -8]

def get_posis(numbers):
    """Returns a new list with negative numbers filtered out"""
    new_list = [] # create a new empty list
    for num in numbers: # loop over every element of the array
        if num > 0: # create an if statement to check conditions for new_list
            new_list.append(num) # adds a number to the new list
    return new_list

print(another_new_list)
print*(get_posis(another_new_list))

#finding information 
my_dict = [
    {
        'name': 'joe',
        'age': 55
    },
    {
        'name': 'anne',
        'age': 66
    }
]

current_max = None
for current_item in my_dict: 
    if current_max is None or current_item['age'] > current_max['age']:
        current_max = current_item

print(current_max)

# or 

current_max = my_list[0] # assume that the first variable matches our test - and create an if statement to test that
for current_item in my_dict: 
    if current_item['age'] > current_max['age']:
        current_max = current_item