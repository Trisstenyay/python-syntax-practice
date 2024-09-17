def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    num1_str = str(num1)
    num2_str = str(num2)

    if len(num1_str) != len(num2_str):
        return False
    
    freq1 = {} # create a dictionary to store frequency of digits in num1
    freq2 = {} # create a dictionary to store frequency of digits in num2

    for digit in num1_str: # loop through each digit in num1_str
        freq1[digit] = freq1.get(digit, 0) + 1 # count frequency of each digit

    for digit in num2_str:  # Loop through each digit in num2_str
        freq2[digit] = freq2.get(digit, 0) + 1  # Count frequency of each digit
        
    return freq1 == freq2  # Return True if the two dictionaries are equal



