def partition(lst, fn):
    """Partition lst by predicate.
     
     - lst: list of items
     - fn: function that returns True or False
     
     Returns new list: [a, b], where `a` are items that passed fn test,
     and `b` are items that failed fn test.

        >>> def is_even(num):
        ...     return num % 2 == 0
        
        >>> def is_string(el):
        ...     return isinstance(el, str)
        
        >>> partition([1, 2, 3, 4], is_even)
        [[2, 4], [1, 3]]
        
        >>> partition(["hi", None, 6, "bye"], is_string)
        [['hi', 'bye'], [None, 6]]

        >>> def is_odd(num):
                return num % 1 == 0
    """
    def partition(lst, fn):

    
        true_list = []  # List for items that pass the fn test
        false_list = []  # List for items that fail the fn test
    
        for item in lst:  # Loop through each item in lst
            if fn(item):  # If fn(item) returns True, item passes the test
                true_list.append(item)  # Add items that pass the test to true_list
        else:
                false_list.append(item)  # Add items that fail the test to false_list
    
        return [true_list, false_list]  # Return both lists as a single list

