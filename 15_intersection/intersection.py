def intersection(l1, l2):
    """Return intersection of two lists as a new list::
    
        >>> intersection([1, 2, 3], [2, 3, 4])
        [2, 3]
        
        >>> intersection([1, 2, 3], [1, 2, 3, 4])
        [1, 2, 3]
        
        >>> intersection([1, 2, 3], [3, 4])
        [3]
        
        >>> intersection([1, 2, 3], [4, 5, 6])
        []
    """
    set1 = set(l1)  # Convert l1 to a set
    set2 = set(l2)  # Convert l2 to a set

    common_elements = set1 & set2  # Find the intersection of set1 and set2

    return list(common_elements)  # Convert the set of common elements back to a list and return it




    