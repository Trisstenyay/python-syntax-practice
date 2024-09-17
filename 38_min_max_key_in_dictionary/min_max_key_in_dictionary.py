def min_max_keys(d):
    """Return tuple (min-keys, max-keys) in d.

        >>> min_max_keys({2: 'a', 7: 'b', 1: 'c', 10: 'd', 4: 'e'})
        (1, 10)

    Works with any kind of key that can be compared, like strings:

        >>> min_max_keys({"apple": "red", "cherry": "red", "berry": "blue"})
        ('apple', 'cherry')
    """
def min_max_keys(d):
    
    if not d:  # Check if the dictionary is empty
        return (None, None)  # Return (None, None) if the dictionary is empty
    
    min_key = min(d)  # Find the minimum key using the min() function
    max_key = max(d)  # Find the maximum key using the max() function
    
    return (min_key, max_key)  # Return a tuple with the minimum and maximum keys
