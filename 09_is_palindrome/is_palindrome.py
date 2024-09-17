def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """
    
    
    reverse_phrase = ''

    last_index = len(phrase) - 1   # we have to get the last index of reverse_string by using len(phrase) first #
    for i in range(last_index, -1, -1):  # then we start from last_index as start, -1 as stop, & -1 as step #
        reverse_phrase = reverse_phrase + phrase[i] # 
    return reverse_phrase.lower().replace(' ', '') == phrase.lower().replace(' ', '')

    

