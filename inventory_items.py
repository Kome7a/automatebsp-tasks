def display_inventory(inventory):
    print("Inventory:")
    total_num_items = 0
    for k, v in inventory.items():
        total_num_items = total_num_items + v
        print(k, v)
    print("Total items: " + str(total_num_items))


def add_to_inventory(inventory, added_items):
    for item in added_items:
        inventory.setdefault(item, 0)
        inventory[item] += 1
    return inventory


inv = {'rope': 1, 'gold coin': 42}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby', 'diamond', 'diamond', 'diamond']
inv = add_to_inventory(inv, dragonLoot)
display_inventory(inv)


