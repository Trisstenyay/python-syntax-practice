def capitalize(phrase):
    """Capitalize first letter of first word of phrase.

        >>> capitalize('python')
        'Python'

        >>> capitalize('only first word')
        'Only first word'
    """
    
    return phrase[0].upper() + phrase[1:] # we are returning the character at index 0, and capatalizing first character of phrase,