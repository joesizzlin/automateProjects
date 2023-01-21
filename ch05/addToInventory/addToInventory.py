# Add to Inventory Project

# write a addToInventory(inventory, addedItems) function below
def addToInventory(inventory, addedItems):                                  # define addToInventory function                                 
    print(inventory, addedItems)                                            # print to test assignment, will remove later




# include: 1). inv{} dictionary, 2). dragonLoot[] list, 3). run that dictionary and list through function above and assign as 'inv'
inv={'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}      # inv dictionary
dragonLoot=['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']        # dragonLoot list
inv=addToInventory(inv,dragonLoot)                                          # run inventory and loot to the addToInventory function
# use displayInventory() from other ch05 project with 'inv' to print user friendly output.
