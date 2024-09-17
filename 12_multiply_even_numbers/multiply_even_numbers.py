def multiply_even_numbers(nums):
    """Multiply the even numbers.
    
        >>> multiply_even_numbers([2, 3, 4, 5, 6])
        48
        
        >>> multiply_even_numbers([3, 4, 5])
        4
        
    If there are no even numbers, return 1.
    
        >>> multiply_even_numbers([1, 3, 5])
        1
    """
    product = 1 # initializes a variable product with the value 1.

    for num in nums: # Loop through each number in the list nums
        if num % 2 == 0: # Check if the number is even (divisible by 2)
            product *= num # Multiply the product by the current even number
    return product  # After the loop, return the product (or 1 if no even numbers were found)
         
