def sum_pairs(nums, goal):
    """Return tuple of first pair of nums that sum to goal.

    For example:

        >>> sum_pairs([1, 2, 2, 10], 4)
        (2, 2)

    (4, 2) sum to 6, and come before (5, 1):

        >>> sum_pairs([4, 2, 10, 5, 1], 6) # (4, 2)
        (4, 2)

    (4, 3) sum to 7, and finish before (5, 2):

        >>> sum_pairs([5, 1, 4, 8, 3, 2], 7)
        (4, 3)

    No pairs sum to 100, so return empty tuple:

        >>> sum_pairs([11, 20, 4, 2, 1, 5], 100)
        ()
    """
    def sum_pairs(nums, goal):
    
    
        seen = set()  # Create an empty set to store numbers we've already seen
    
        for num in nums:  # Loop through each number in the list nums
            complement = goal - num  # Calculate the complement needed to reach the goal
        
        if complement in seen:  # If the complement is in the set, return the pair
            return (complement, num)  # Return the first pair that sums to the goal
        
        seen.add(num)  # Add the current number to the set for future checks
    
    return ()  # If no pair is found, return an empty tuple
