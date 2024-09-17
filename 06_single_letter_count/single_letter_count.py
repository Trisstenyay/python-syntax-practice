def single_letter_count(word, letter):
    """How many times does letter appear in word (case-insensitively)?
    
        >>> single_letter_count('Hello World', 'h')
        1
        
        >>> single_letter_count('Hello World', 'z')
        0
        
        >>> single_letter_count("Hello World", 'l')
        3
    """ 
    char_counter = 0
    word_lower = word.lower()
    letter_lower = letter.lower()
    for char in word_lower:
        if char == letter_lower:
            char_counter = char_counter + 1
            
    return char_counter
            



    
    