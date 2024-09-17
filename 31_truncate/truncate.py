def truncate(phrase, n):
    """Return truncated-at-n-chars version of  phrase.
    
    If the phrase is longer than, or the same size as, n make sure it ends with '...' and is no
    longer than n.
    
        >>> truncate("Hello World", 6)
        'Hel...'
        
        >>> truncate("Problem solving is the best!", 10)
        'Problem...'
        
        >>> truncate("Yo", 100)
        'Yo'
        
    The smallest legal value of n is 3; if less, return a message:
    
        >>> truncate('Cool', 1)
        'Truncation must be at least 3 characters.'

        >>> truncate("Woah", 4)
        'W...'

        >>> truncate("Woah", 3)
        '...'
    """
    def truncate(phrase, n):
    
        if n < 3:
            return "Truncation must be at least 3 characters."  # Check for invalid n value
    
        if len(phrase) <= n:
            return phrase  # If phrase fits within n characters, return the original phrase
    
        truncated_phrase = phrase[:n - 3] + "..."  # Truncate and add "..." at the end
        return truncated_phrase  # Return the truncated phrase
