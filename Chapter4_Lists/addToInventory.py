# Write your code here :-)
def addToInventory(inventory, addedItems):
    newInv = inventory
    for i in addedItems:
        newInv.setdefault(i,0)
        newInv[i] = newInv[i] + 1
    return newInv

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + " " + k)
        item_total = item_total + v
    print("Total number of items: " + str(item_total))
displayInventory(inv)
