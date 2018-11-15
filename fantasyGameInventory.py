inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12 }
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(v, k)
        item_total += v
    print("Total number of items: " + str(item_total))

displayInventory(inventory)
print()

def addToInventory(inventory, addedItems):
    for item in addedItems:
        if item not in inventory:
            inventory.setdefault(item, 1)
        else:
            inventory[item] += 1


addToInventory(inventory, dragonLoot)
print()

displayInventory(inventory)
print()
