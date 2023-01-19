# Comma Code Practice project

def comma(items):                                   # define the comma code function
    result = items[0]                               # initialize string with first item
    
    for item in items[1:-1]:                        # add the remaining items, separated by a comma and space
        result += ', ' + item                       # does not add "and" & the last item
    
    result += ' and ' + items[-1]                   # add "and" & last item

    return result                                   #returns a string with all the items separated by a comma


spam = ['apples', 'bananas', 'tofu', 'cats']        # starting list value
result = comma(spam)                                # sends list value of 'spam' as an argument, assigns returned result as 'result'            
print(result)                                       # prints final result