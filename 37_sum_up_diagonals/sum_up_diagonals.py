def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30
    """
def sum_up_diagonals(matrix):

    
    tl_br_sum = 0  # Initialize sum for TL-to-BR diagonal
    bl_tr_sum = 0  # Initialize sum for BL-to-TR diagonal
    
    size = len(matrix)  # Determine the size of the matrix (number of rows/columns)
    
    for i in range(size):  # Loop through each index from 0 to size-1
        tl_br_sum += matrix[i][i]  # Add the element from TL-to-BR diagonal
        bl_tr_sum += matrix[i][size - 1 - i]  # Add the element from BL-to-TR diagonal
    
    return tl_br_sum + bl_tr_sum  # Return the sum of both diagonals
