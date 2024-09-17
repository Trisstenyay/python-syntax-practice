def includes(collection, sought, start=None):
    """Is sought in collection, starting at index start?

    Return True/False if sought is in the given collection:
    - lists/strings/sets/tuples: returns True/False if sought present
    - dictionaries: return True/False if *value* of sought in dictionary

    If string/list/tuple and `start` is provided, starts searching only at that
    index. This `start` is ignored for sets/dictionaries, since they aren't
    ordered.

        >>> includes([1, 2, 3], 1)
        True

        >>> includes([1, 2, 3], 1, 2)
        False

        >>> includes("hello", "o")
        True

        >>> includes(('Elmo', 5, 'red'), 'red', 1)
        True

        >>> includes({1, 2, 3}, 1)
        True

        >>> includes({1, 2, 3}, 1, 3)  # "start" ignored for sets!
        True

        >>> includes({"apple": "red", "berry": "blue"}, "blue")
        True
    """
    # Handle lists, strings, and tuples with the start index
    if isinstance(collection, (list, str, tuple)):
        if start is not None:
            # Use slicing to search from the start index onwards
            return sought in collection[start:]  
        else:
            # Search the entire collection if no start index is provided
            return sought in collection
    
    # Handle sets (start is ignored since sets are unordered)
    if isinstance(collection, set):
        return sought in collection
    
    # Handle dictionaries (we're checking if the sought value is present)
    if isinstance(collection, dict):
        return sought in collection.values()