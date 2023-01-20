#fantasyGameInventory, pg 120
# create a function that will take any possible inventory (using dictionary value) and display as user friendly output.
# starting inventory: 1 rope, 6 torch, 42 gold coin, 1 dagger, 12 arrow

inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}              # dictionary for inventory     

def displayInventory(inventory):
    print('Inventory: ')
    items_total = 0                                         # declare items_total and assign int(0)
    for k,v in inventory.items():                           # in the for loop, the string of the inventory item and assign to k, assign number of items as v
        print(str(v) + ' ' + k)                             # prints the number of items, then the name of the item
        items_total += v                                    # add number of items to our tally of items_total
    print('Total number of Items: ' + str(items_total))

displayInventory(inventory)                                 # takes the inventory dictionary and runs the displayInventory function
