def list_manipulation(lst, command, location, value=None):
    """Mutate lst to add/remove from beginning or end.

    - lst: list of values
    - command: command, either "remove" or "add"
    - location: location to remove/add, either "beginning" or "end"
    - value: when adding, value to add

    remove: remove item at beginning or end, and return item removed

        >>> lst = [1, 2, 3]

        >>> list_manipulation(lst, 'remove', 'end')
        3

        >>> list_manipulation(lst, 'remove', 'beginning')
        1

        >>> lst
        [2]

    add: add item at beginning/end, and return list

        >>> lst = [1, 2, 3]

        >>> list_manipulation(lst, 'add', 'beginning', 20)
        [20, 1, 2, 3]

        >>> list_manipulation(lst, 'add', 'end', 30)
        [20, 1, 2, 3, 30]

        >>> lst
        [20, 1, 2, 3, 30]

    Invalid commands or locations should return None:

        >>> list_manipulation(lst, 'foo', 'end') is None
        True

        >>> list_manipulation(lst, 'add', 'dunno') is None
        True
    """


    if command not in ['remove', 'add']:
        
        return None
    
    if location not in ['beginning', 'end']:
        
        return None
    


    
    
    element = None

    if command == 'remove':
        # handle remove at the 'beginning'
        if location == 'beginning':
            element = lst.pop(0)
        # handle remove at the 'end'
        elif location == 'end':
            element = lst.pop()
        return element

    if command == 'add':
        #handle add at the 'beginning'
        if location == 'beginning':
            lst.insert(0, value)
            # lst = [value] + lst
        elif location == 'end':
            # lst.insert(len(lst), value)
            lst.append(value)
            # lst = lst + [value]
        return lst
    
        



    

    

def list_manipulation2(lst, command, location, value=None):

    element = None

    if command == 'remove':  # this means that we are choosing the parameter command to be 'remove' #
        if location == 'beginning': # this means that we are choosing the location to be 'beginning' #
            element = lst.pop(0) # .pop(0) method when 0 passed in means that the first element in the list will be popped off #
        elif location == 'end':  # this means that we are choosing the location to be 'end' in an elif conditional statement #
            element = lst.pop()  # .pop() method with nothing passed in means that the last element in the list will be popped off #
        return element



names = ['Michael Ogu', 'Tristan Tenyay', 'Springboard', 'Crazy']

print(f'Original list: {names}')
result = list_manipulation2(names, 'remove', 'beginning')
print(f'Mutated list: {names}')



# my_list = [1, 2, 3]
# print(f'Original list: {my_list}')
# result = list_manipulation(my_list, 'remove', 'beginning')
# print(f'Mutated list: {my_list}')




# new_list = [1, 20, 17, 44, 55, 67]
# print(f'original list: {new_list}')
# result = list_manipulation(new_list, 'remove', 'end')
# print(f'mutated list: {new_list}')

# print(result)








