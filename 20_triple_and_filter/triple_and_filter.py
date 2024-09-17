def triple_and_filter(nums):
    """Return new list of tripled nums for those nums divisible by 4.

    Return every number in list that is divisible by 4 in a new list,
    except multipled by 3.
    
        >>> triple_and_filter([1, 2, 3, 4])
        [12]
        
        >>> triple_and_filter([6, 8, 10, 12])
        [24, 36]
        
        >>> triple_and_filter([1, 2])
        []
    """
    result = []  # Create an empty list to store the filtered and tripled numbers
    
    for num in nums:  # Loop through each number in nums
        if num % 4 == 0:  # Check if the number is divisible by 4
            result.append(num * 3)  # Multiply the number by 3 and add it to the result list
    
    return result  # Return the final list of tripled numbers