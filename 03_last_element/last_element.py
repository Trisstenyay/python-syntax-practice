def last_element(lst):
    """Return last item in list (None if list is empty.
    
        >>> last_element([1, 2, 3])
        3
        
        >>> last_element([]) is None
        True
    """
    last_index = len(lst) - 1
    if last_index < 0:
        return None
    return lst[last_index]


   
# practice
def third_element(lst):
    if len(lst) < 3:
        return None
    return(lst[2]) # this return statement would result in returning the third element because I PASSED IN INDEX 2, which is element number 3

# practice 
def sixth_element(lst):
    if len(lst) < 6:
        return None
    return(lst[5]) # this return statement would result in returning the sixth element because I PASSED IN INDEX 5, which is element number 6
# practice
def eighth_element(lst):
    if len(lst) < 8:
        return None
    return(lst[7]) # this return statement would result in returning the sixth element because I PASSED IN INDEX 7, which is element number 8