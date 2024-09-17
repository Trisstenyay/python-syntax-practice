def number_compare(a, b):
    """Report on whether a>b, b>a, or b==a
    
        >>> number_compare(1, 1)
        'Numbers are equal'
        
        >>> number_compare(-1, 1)
        'Second is greater'
        
        >>> number_compare(1, -2)
        'First is greater'
    """
    report = ''
    
    if a == b:
        report = 'Numbers are equal'
    elif a > b:
        report = 'First is greater'
    else:
        report = 'Second is greater'
    
    return report


