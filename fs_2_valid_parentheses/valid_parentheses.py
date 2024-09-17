def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """
def valid_parentheses(parens):
    
    balance = 0  # Initialize balance counter to 0
    
    for char in parens:  # Loop through each character in the string parens
        if char == '(':  # Check if the character is an opening parenthesis
            balance += 1  # Increment the balance counter
        elif char == ')':  # Check if the character is a closing parenthesis
            balance -= 1  # Decrement the balance counter
        
        if balance < 0:  # If balance goes negative, parentheses are not balanced
            return False
    
    return balance == 0  # Return True if balance is 0, otherwise False
