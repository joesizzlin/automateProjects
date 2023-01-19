#fantasyGameInventory, pg 120
# create a function that will take any possible inventory (using dictionary value) and display as user friendly output.
# starting inventory: 1 rope, 6 torch, 42 gold coin, 1 dagger, 12 arrow

inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(stuff):
    print('Inventory: ')
    items_total = 0
    for k,v in inventory.items():
        print(str(v) + ' ' + k)
        items_total += v
    print('Total number of Items: ' + str(items_total))

displayInventory(inventory)
