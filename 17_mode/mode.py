def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    counts = {} # Create an empty dictionary to store the frequency of each number

    for num in nums: # loop through each number in the list nums
        counts[num] = counts.get(num, 0) + 1  # Increment the count of the current number
    max_count = max(counts.values())  # Find the maximum frequency
    for num, count in counts.items():  # Loop through the dictionary to find the number with the highest count
        if count == max_count:  # Check if the current number's count matches the maximum frequency
            return num  # Return the number that has the maximum frequency





