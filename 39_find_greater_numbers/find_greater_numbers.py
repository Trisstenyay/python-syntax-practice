def find_greater_numbers(nums):
    """Return # of times a number is followed by a greater number.

    For example, for [1, 2, 3], the answer is 3:
    - the 1 is followed by the 2 *and* the 3
    - the 2 is followed by the 3

    Examples:

        >>> find_greater_numbers([1, 2, 3])
        3

        >>> find_greater_numbers([6, 1, 2, 7])
        4

        >>> find_greater_numbers([5, 4, 3, 2, 1])
        0

        >>> find_greater_numbers([])
        0
    """
def find_greater_numbers(nums):
    
    count = 0  # Initialize a count variable to keep track of the number of times a number is followed by a greater number
    
    for i in range(len(nums)):  # Loop through each index in the list nums
        for j in range(i + 1, len(nums)):  # Loop through each index after index i
            if nums[j] > nums[i]:  # Check if the number at index j is greater than the number at index i
                count += 1  # Increment the count if the condition is met
    
    return count  # Return the final count after all comparisons
