def two_list_dictionary(keys, values):
    """Given keys and values, make dictionary of those.
    
        >>> two_list_dictionary(['x', 'y', 'z'], [9, 8, 7])
        {'x': 9, 'y': 8, 'z': 7}
        
    If there are fewer values than keys, remaining keys should have value
    of None:
    
        >>> two_list_dictionary(['a', 'b', 'c', 'd'], [1, 2, 3])
        {'a': 1, 'b': 2, 'c': 3, 'd': None}
    
    If there are fewer keys, ignore remaining values:

        >>> two_list_dictionary(['a', 'b', 'c'], [1, 2, 3, 4])
        {'a': 1, 'b': 2, 'c': 3}
   """
def two_list_dictionary(keys, values):
    
    result = {}  # Initialize an empty dictionary to store the key-value pairs
    
    for i, key in enumerate(keys):  # Loop through the keys using enumerate to get index and key
        if i < len(values):  # Check if there's a corresponding value
            result[key] = values[i]  # Assign the corresponding value to the key
        else:
            result[key] = None  # If no value is available, assign None
    
    return result  # Return the resulting dictionary
