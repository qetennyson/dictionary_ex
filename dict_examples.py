# simple demonstration of a dictionary, including JSON format for easy readability
# Original Code and exercise credit to Erle Robotics via Gitbook
# Licensed under Attribution-ShareAlike 3.0 Unported (CC BY-SA 3.0)

import json

inventory = {
    'gold': 500,
    'pouch': ['flint', 'twine', 'gemstone'],
    'backpack': ['xylophone', 'dagger', 'bedroll', 'bread loaf']
}

inventory['pocket'] = ['seashell', 'strange berry', 'lint']
inventory['backpack'].sort()
inventory['backpack'].remove("dagger")
inventory['gold'] += 50

print inventory
print "\n"

print("A for loop can easily be used to pull out all keys or values: \n")
for key in inventory:
    print inventory[key]

print "\n"

print("You can also use 'for key, value in inventory.items(), this is a great formatting method:")
for key, value in inventory.items():
    print("\nKey: " + key)
    print("Value: " + str(value))

# using the .items() method returns a list of tuples with each tuple consisting of the key / value pair from the dict
print("**Using .items() to generate tuples of the dict: \n")
items = inventory.items()
print items
print type(items)

print "\n"


print("**Using .keys() to generate a list of the dict's keys: \n")
keys = inventory.keys()
print keys
print type(keys)

print "\n"

print("**Using .values() to generate a list of the dict's values: \n")
values = inventory.values()
print values
print type(keys)

print "\n"


print("**Using JSON module to generate another more readable dict: \n")
# if we import the json module, and utilize some of its methods, we can really clean up our dict output.
print json.dumps(inventory, sort_keys=True, indent=4)

print"-------------------------------"

print("When iterating over a dictionary, nothing is sorted, and pairs are returned in an unpredictable order.  "
      "However, we can compensate for this using sorted")

favorite_languages = {
    'quincy': 'python',
    'mark': 'powershell',
    'drew': 'javascript',
    'matthew': 'c',
}

for name in sorted(favorite_languages.keys()):
    print name

