class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __add__(self, other):
        sum_matrix = list()
        row_sum_matrix = list()
        for i in range(len(self.matrix)):
            ls_1, ls_2 = self.matrix[i], other.matrix[i]
            for j in range(len(ls_1)):
                row_sum_matrix.append(ls_1[j] + ls_2[j])
            sum_matrix.append(row_sum_matrix)
            row_sum_matrix = list()
        self.matrix = sum_matrix
        return Matrix(self.matrix)

    def __str__(self):
        output_matrix = ''
        for rows in self.matrix:
            for el in rows:
                output_matrix += str(el) + '  '
            output_matrix += '\n'
        return output_matrix


mx_1 = Matrix([[1, 2, 3], [1, 2, 3], [1, 2, 3]])
mx_2 = Matrix([[1, 2, 3], [1, 2, 3], [1, 2, 3]])
print(mx_1 + mx_2)
