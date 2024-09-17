def find_factors(num):
    """Find factors of num, in increasing order.

    >>> find_factors(10)
    [1, 2, 5, 10]

    >>> find_factors(11)
    [1, 11]

    >>> find_factors(111)
    [1, 3, 37, 111]

    >>> find_factors(321421)
    [1, 293, 1097, 321421]
    """
    factors = []  # Initialize an empty list to store factors
    
    for i in range(1, num + 1):  # Loop through numbers from 1 to num (inclusive)
        if num % i == 0:  # Check if num is divisible by i with no remainder
            factors.append(i)  # If divisible, append i to the factors list
    
    return factors  # Return the list of factors after the loop