import numpy as np


def gaussian_eliminate(A, b):
    """
    A: a square (n, n) NumPy array that does not require row swaps
    b: a length-n NumPy array

    Returns:
        (U, c): U is A row-reduced to upper-triangular form, c is b
        transformed by the same row operations, such that Ux = c has
        the same solution as Ax = b.
    """
    # TODO: Implement elimination on copies of A and b in lockstep,
    # from Theory.
    row = len(A)
    A = A.astype(float)
    b = b.astype(float)
    for j in range(row):
        for i in range (j + 1, row):
            multiplier = A[i][j] / A[j][j]
            A[i] = A[i] - np.multiply(multiplier, A[j])
            b[i] = b[i] - np.multiply(multiplier, b[j])
    return (A, b)


def back_substitute(U, c):
    """
    U: an upper-triangular (n, n) NumPy array
    c: a length-n NumPy array

    Returns:
        x, the solution to Ux = c, solved from the last row up.
    """
    # TODO: Implement back substitution from Theory's formula.
    row = len(U)
    x = np.zeros(row)
    for i in range(row - 1, -1, -1):
        x[i] = (c[i] - np.dot(U[i][i+1:], x[i+1:])) / U[i][i]
    return x
