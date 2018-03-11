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

print json.dumps(inventory, sort_keys=True, indent=4)


