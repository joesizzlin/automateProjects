# Add to Inventory Project

# add displayInventory from other ch05 Project
def displayInventory(stuff):
    print('Inventory: ')
    items_total = 0                                         # declare items_total and assign int(0)
    for k,v in stuff.items():                           # in the for loop, the string of the inventory item and assign to k, assign number of items as v
        print(str(v) + ' ' + k)                             # prints the number of items, then the name of the item
        items_total += v                                    # add number of items to our tally of items_total
    print('Total number of Items: ' + str(items_total))

# write a addToInventory(inventory, addedItems) function below
def addToInventory(inventory, addedItems):                                  # define addToInventory function                                 
    print(inventory, addedItems)                                            # print to test assignment, will remove later




# include: 1). inv{} dictionary, 2). dragonLoot[] list, 3). run that dictionary and list through function above and assign as 'inv'
inv={'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}      # inv dictionary
dragonLoot=['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']        # dragonLoot list
inv=addToInventory(inv,dragonLoot)                                          # run inventory and loot to the addToInventory function
# use displayInventory() from other ch05 project with 'inv' to print user friendly output.
displayInventory(inv)