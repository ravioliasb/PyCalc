def cofactor(matrix, omit_row, omit_column):
    if len(matrix) != len(matrix[0]):
        raise ValueError("The matrix is not square")
    else:
        row = len(matrix)
        column = len(matrix[0])
        return [[matrix[row][column] for column in range(column) if column != omit_column]
                for row in range(row) if row != omit_row]


def cofactor_determinant(matrix, omit_row, omit_column):
    if len(matrix) != len(matrix[0]):
        raise ValueError("The matrix is not square")
    else:
        matrix = cofactor(matrix, omit_row, omit_column)
        return determinant(matrix)


def determinant(matrix):
    if len(matrix) != len(matrix[0]):
        raise ValueError("The matrix is not square")
    else:
        dimensions = len(matrix)
        if dimensions == 2:
            det = matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]
            return det
        else:
            det = 0
            for i in range(dimensions):
                constant = matrix[0][i]
                if i % 2 == 1:
                    constant = constant * -1
                det += constant * cofactor_determinant(matrix, 0, i)
        return det


def transpose(matrix):
    row = len(matrix)
    column = len(matrix[0])
    transpose_matrix = [[matrix[row][column] for row in range(row)] for column in range(column)]
    return transpose_matrix


def inverse(matrix):
    if len(matrix) != len(matrix[0]):
        raise ValueError('The matrix is not square')
    elif determinant(matrix) != 0:
        dimensions = len(matrix)
        det = determinant(matrix)
        cofactor_matrix = []
        if dimensions > 2:
            for i in range(dimensions):
                cofactor_row = []
                for j in range(dimensions):
                    constant = -1 if (i % 2) ^ (j % 2) else 1
                    cofactor_row.append(constant * cofactor_determinant(matrix, i, j))
                cofactor_matrix.append(cofactor_row)
            comatrix = transpose(cofactor_matrix)
            inverse_matrix = [[component / det for component in row] for row in comatrix]
            return inverse_matrix
        else:
            constant = 1 / det
            inv_matrix = []
            inv_matrix.append([matrix[1][1], -1*(matrix[0][1])])
            inv_matrix.append([-1*(matrix[1][0]), matrix[0][0]])
            final = scalar_multiply(inv_matrix, constant)
            return final

    else:
        raise ValueError("This matrix does not have an inverse")


def scalar_multiply(matrix, scalar):
    scaled_matrix = [[component * scalar for component in row] for row in matrix]
    return scaled_matrix


def trace(matrix):
    trace_value = 0
    for i in range(len(matrix[0])):
        trace_value += matrix[i][i]
    return trace_value


def add(matrix1, matrix2):
    sum_matrix = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] + matrix2[i][j])
        sum_matrix.append(row)
    return sum_matrix


def sub(matrix1, matrix2):
    diff_matrix = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] - matrix2[i][j])
        diff_matrix.append(row)
    return diff_matrix


def multiply(matrix1, matrix2):
    if len(matrix1[0]) != len(matrix2):
        raise ValueError("The number of columns in the first matrix should be equal to the number of rows in the second")
    else:
        product = [[0 for _ in range(len(matrix2[0]))] for _ in range(len(matrix1))]
        for i in range(len(matrix1)):
            for j in range(len(matrix2[0])):
                sum_num = 0

                for k in range(len(matrix1[0])):
                    sum_num += matrix1[i][k] * matrix2[k][j]
                product[i][j] = sum_num
        return product


def print_matrix(matrix):
    for i in matrix:
        print(*i)


def identity(matrix):
    if len(matrix) != len(matrix[0]):
        raise ValueError("The matrix is not square")
    else:
        identity_matrix = [[0 for _ in range(len(matrix))] for _ in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if i == j:
                    identity_matrix[i][j] = 1
        return identity_matrix


def matrix_pow(matrix, n):
    if len(matrix) != len(matrix[0]):
        raise ValueError('The matrix is not square')
    else:
        new = matrix
        return matrix_pow_help(matrix, n, new)


def matrix_pow_help(matrix, n, new):
    if n == 1:
        return new
    elif n == 0:
        return identity(matrix)
    elif n < 0:
        _ = []
        _ = inverse(matrix)
        return matrix_pow_help(_, -n, _)
    else:
        new = multiply(new, matrix)
        return matrix_pow_help(matrix, n - 1, new)
