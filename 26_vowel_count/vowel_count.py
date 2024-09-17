def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
def vowel_count(phrase):
    
    vowel_map = {}  # Initialize an empty dictionary to store vowel counts
    phrase = phrase.lower()  # Convert the string to lowercase to make counting case-insensitive
    
    for char in phrase:  # Loop through each character in the string
        if char in 'aeiou':  # Check if the character is a vowel
            vowel_map[char] = vowel_map.get(char, 0) + 1  # Update the vowel count
    
    return vowel_map  # Return the dictionary of vowel counts
