class Matrix:
    def __init__(self, *args):
        self.all_matrix = []
        for matrix in args:
            self.all_matrix.append(matrix)

    def __str__(self):
        txt = ''
        i = 1
        for matrix in self.all_matrix:
            txt += f'Matrix {i}: \n'
            for matrix_line in matrix:
                for matrix_element in matrix_line:
                    txt += f'{matrix_element} '
                txt += '\n'
            txt += '\n'
            i += 1
        return txt

    def __add__(self, other):
        added_matrix = []
        i = 0
        for matrix1, matrix2 in zip(self.all_matrix, other.all_matrix):
            for matrix1_line, matrix2_line in zip(matrix1, matrix2):
                added_matrix.append([])
                for matrix1_element, matrix2_element in zip(matrix1_line, matrix2_line):
                    added_matrix[i].append(matrix1_element + matrix2_element)
                i += 1
        return Matrix(added_matrix)


print_matrix = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[9, 8, 7], [6, 5, 4], [3, 2, 1]])
print(print_matrix)

matrix1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix2 = Matrix([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
print(matrix1 + matrix2)
