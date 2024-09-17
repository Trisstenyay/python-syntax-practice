def is_odd_string(word):
    """Is the sum of the character-positions odd?

    Word is a simple word of uppercase/lowercase letters without punctuation.

    For each character, find it's "character position" ("a"=1, "b"=2, etc).
    Return True/False, depending on whether sum of those numbers is odd.

    For example, these sum to 1, which is odd:
    
        >>> is_odd_string('a')
        True

        >>> is_odd_string('A')
        True

    These sum to 4, which is not odd:
    
        >>> is_odd_string('aaaa')
        False

        >>> is_odd_string('AAaa')
        False

    Longer example:
    
        >>> is_odd_string('amazing')
        True
    """
    # Hint: you may find the ord() function useful here
def is_odd_string(word):
    
    total_sum = 0  # Initialize total_sum to 0, to store the sum of character positions
    
    for char in word:  # Loop through each character in the word
        position = ord(char.lower()) - ord('a') + 1  # Calculate the character position
        total_sum += position  # Add the position value to the total_sum
    
    return total_sum % 2 == 1  # Return True if the total_sum is odd, False otherwise

