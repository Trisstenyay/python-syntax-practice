def three_odd_numbers(nums):
    """Is the sum of any 3 sequential numbers odd?"

        >>> three_odd_numbers([1, 2, 3, 4, 5])
        True

        >>> three_odd_numbers([0, -2, 4, 1, 9, 12, 4, 1, 0])
        True

        >>> three_odd_numbers([5, 2, 1])
        False

        >>> three_odd_numbers([1, 2, 3, 3, 2])
        False
    """
def three_odd_numbers(nums):
    
    for i in range(len(nums) - 2):  # Iterate through indices where a set of three can be formed
        sum_of_three = nums[i] + nums[i + 1] + nums[i + 2]  # Calculate the sum of three consecutive numbers
        
        if sum_of_three % 2 != 0:  # Check if the sum is odd
            return True  # If odd, return True
    
    return False  # If no odd sums are found, return False
