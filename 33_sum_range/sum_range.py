def sum_range(nums, start=0, end=None):
    """Return sum of numbers from start...end.

    - start: where to start (if not provided, start at list start)
    - end: where to stop (include this index) (if not provided, go through end)

        >>> nums = [1, 2, 3, 4]

        >>> sum_range(nums)
        10

        >>> sum_range(nums, 1)
        9

        >>> sum_range(nums, end=2)
        6

        >>> sum_range(nums, 1, 3)
        9

    If end is after end of list, just go to end of list:

        >>> sum_range(nums, 1, 99)
        9
    """
def sum_range(nums, start=0, end=None):
    
    if end is None:  # If no end is provided, set it to the last index
        end = len(nums) - 1
    
    end = min(end, len(nums) - 1)  # Make sure end is within the list bounds
    
    return sum(nums[start:end + 1])  # Sum the values from start to end (inclusive)
