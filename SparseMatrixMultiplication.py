"""
Write a function that takes in two integer matrices and multiplies them together.

Both matrices will be sparse, meaning that most of their elements will be zero. Take advantage of that to reduce the number of total computations that your function performs.

If the matrices can't be multiplied together, your function should return [[]].
"""

def sparse_matrix_multiplication(matrix_a, matrix_b):
    # Write your code here.
    if(len(matrix_a[0]) != len(matrix_b)):
        return [[]]

    nodes_A = get_nodes(matrix_a)
    nodes_B = get_nodes(matrix_b)

    matrix_c =[[0]*len(matrix_b[0]) for _ in range(len(matrix_a))]

    for i,k in nodes_A.keys():
        for j in range(len(matrix_b[0])):
            if (k,j) in nodes_B.keys():
                matrix_c[i][j] += nodes_A[(i,k)]*nodes_B[(k,j)]
    
    return matrix_c


def get_nodes(matrix):
    dict ={}
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if(matrix[i][j] != 0):
                dict[(i,j)] = matrix[i][j]
    return dict
