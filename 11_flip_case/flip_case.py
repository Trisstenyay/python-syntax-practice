def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    # I created a new variable result to store the result, this initializes to an empty string.
    result = ''

    for char in phrase: # I created a for loop and iterated through each character in the first parameter which is phrase
        if char.lower() == to_swap.lower(): # I am checking to see if both parameters are equal to lowercase
            if char.islower():
                result += char.upper() # if 'char' is lowercase, flip to uppercase
            else:
                result += char.lower() # if 'char' is uppercase, flip to lowercase
        else:
            result += char # if 'char' doesnt match 'to_swap', keep it unchanged
    return result # return the final modified string

result = flip_case('tristan', 't',)
print(result) 





