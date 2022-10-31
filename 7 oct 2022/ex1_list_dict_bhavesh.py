inventory = {
    'gold': 500,
    'pouch': ['flint', 'twine', 'gemstone'],
    'backpack': ['xylophone', 'dagger', 'bedroll', 'bread loaf']
}

inventory.update({'pocket': ['seashell', 'strange', 'berry', 'lint']})
print(sorted(inventory['backpack']))
inventory['backpack'].remove('dagger')
inventory.update({'gold': inventory.get('gold') + 50})
print(inventory)
