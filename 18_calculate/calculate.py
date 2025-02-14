def calculate(operation, a, b, make_int=False, message='The result is'):
    """Perform operation on a + b, ()possibly truncating) & returning w/msg.

    - operation: 'add', 'subtract', 'multiply', or 'divide'
    - a and b: values to operate on
    - make_int: (optional, defaults to False) if True, truncates to integer
    - message: (optional) message to use (if not provided, use 'The result is')

    Performs math operation (truncating if make_int), then returns as
    "[message] [result]"

        >>> calculate('add', 2.5, 4)
        'The result is 6.5'

        >>> calculate('subtract', 4, 1.5, make_int=True)
        'The result is 2'

        >>> calculate('multiply', 1.5, 2)
        'The result is 3.0'

        >>> calculate('divide', 10, 4, message='I got')
        'I got 2.5'

    If a valid operation isn't provided, return None.

        >>> calculate('foo', 2, 3)
    """
    if operation == 'add':
        result = a + b # perform addition if operation is 'add'
    elif operation == 'subtract':
        result = a - b # perform subtraction if operation is 'subtract'
    elif operation == 'multiply':
        result = a * b # perform multiplication if operation is 'multiply'
    elif operation == 'divide':
        result = a / b # perform division if operation is 'divide'
    else:
        return None # Return none if the operation is invalid
    

    # If make_int is True, truncate the result to an integer
    if make_int:
        result = int(result)


    # Return the result with the message (custom or default)
    return f"{message} {result}"