def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """
    truthy_elements = []  # Create an empty list to store truthy elements

    for item in lst:  # Loop through each element in original lst
        if item:  # Check if the element is truthy (evaluates to True)
            truthy_elements.append(item)  # Add truthy elements to the new list
    return truthy_elements  # Return the new list with only truthy elements