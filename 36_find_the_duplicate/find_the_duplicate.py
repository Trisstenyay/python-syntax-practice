def find_the_duplicate(nums):
    """Find duplicate number in nums.

    Given a list of nums with, at most, one duplicate, return the duplicate.
    If there is no duplicate, return None

        >>> find_the_duplicate([1, 2, 1, 4, 3, 12])
        1

        >>> find_the_duplicate([6, 1, 9, 5, 3, 4, 9])
        9

        >>> find_the_duplicate([2, 1, 3, 4]) is None
        True
    """
def find_the_duplicate(nums):
    
    seen = set()  # Create an empty set to track numbers we have already seen
    
    for num in nums:  # Loop through each number in the list nums
        if num in seen:  # If the number is already in the set, it's a duplicate
            return num   # Return the duplicate number
        seen.add(num)  # If it's not a duplicate, add it to the set
    
    return None  # If no duplicates are found, return None
