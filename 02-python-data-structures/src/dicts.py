my_dict = {
    'name': 'joe',
    'age': 55
}

# Key Lookups 
my_dict['name']

# TODO Add a key/value pair
my_dict['phone'] = '555-555-5555'

# TODO Update a value
my_dict['phone'] = '555-555-4321'

# TODO Use an invalid key
my_dict['badkey'] # raises KeyError

# TODO Test if a key exists
'name' in my_dict

# TODO use .get()
my_dict['name'] # returns 'joe'
my_dict.get('name') # returns 'joe'
my_dict.get('badkey') # returns None
my_dict.get('badkey', 'missing value') # second arg is default value

# TODO Delete a key
my_dict.pop('age')

# TODO get the length of a dict
len(my_dict)

# TODO Merge two dicts
my_dict.update({'age': 6, 'phone': '555-555-5555'})

# TODO copy a dict
my_dict.copy()

# TODO loop over a dict
for x in my_dict: 
    print(x)

for key in my_dict: 
    print(key, my_dict[key])

for key, value in my_dict.items():
    print(key, value)