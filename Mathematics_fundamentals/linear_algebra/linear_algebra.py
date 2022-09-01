import numpy as np


class Linalg:

    """
    In this class I intend to implement all of linear algebra so that it can be applied to
    future projects.
    """

    def get_empty_row(self, length):
        row = []
        for i in range(length):
            row.append(0)
        return row

    def get_empty_matrix(self, rows, columns):
        matrix = []
        for i in range(rows):
            matrix.append(self.get_empty_row(columns))
        return matrix

    def get_transpose(self, mat1):
        """
        Will find the transpose of any matrix inputted. i.e will make the rows into columns and visa
        versa. The element at index [i,j] goes to [j,i] for all i in rows and j in columns.
        """
        rows = len(mat1)
        columns = len(mat1[0])
        transpose = self.get_empty_matrix(columns, rows)
        for i in range(rows):
            for j in range(columns):
                transpose[j][i] = mat1[i][j]
        return transpose

    def get_dot_product(self, vector1, vector2) -> float:
        """
        Calculates the dot product between two vectors of equal length.
        """
        v_1_length = len(vector1)
        v_2_length = len(vector2)
        if v_1_length != v_2_length:
            return f"""Error! Vector 1 has length {v_1_length}, and vector 2 has length {v_2_length}. 
            These must be equal."""
        sum = 0
        for i in range(v_2_length):
            sum += vector1[i] * vector2[i]
        return sum
    
    def get_cross_product(self,vector1,vector2):
        """
        Will calculate the cross product between two vectors. These vectors must be three dimensional.
        """


    def matrix_multiply(self, mat1, mat2):
        """
        Matrix multiplication works by multiplying rows by columns pairwise. Thus if mat1
        does not have the same number of rows as mat2 does columns, we cannot multiply them.

        Note: mat1 will be a list of lists to simulate a matrix:
            mat1 = [ [1,2,3]
                     [4,5,6]
                     [7,8,9]   ] 3x3 matrix.
        For example.

        In essence we can only multiply matrices with dimensions n x k and k x m, the resulting matrix
        will have dimension n x m. The plan is to transpose mat2 and then simply make the [i,j] element
        of the new matrix equal to the dot product of the i'th row of mat1 and the j'th column of mat2
        (which is the j'th row of mat2 transpose).
        """
        mat1_rows = len(mat1)
        mat1_columns = len(mat1[0])
        mat2_rows = len(mat2)
        mat2_columns = len(mat2[0])
        if mat1_columns != mat2_rows:
            return f"Error! Matrix one has {mat1_columns} columns and matrix two has {mat2_rows} rows."
        mat2_transpose = self.get_transpose(mat2)
        multiplied_matrix = self.get_empty_matrix(mat1_rows, mat2_columns)
        for row_index, row1 in enumerate(mat1):
            for column_index, row2 in enumerate(mat2_transpose):
                multiplied_matrix[row_index][column_index] = self.get_dot_product(
                    row1, row2
                )
        return multiplied_matrix

    def transform_function(self, x, function, matrix):
        """
        Will transform points of a function by using an inputted matrix transformation.
        """
        co_ordinate = [[x], [function(x)]]
        new_co_ordinate = self.matrix_multiply(matrix, co_ordinate)
        output = []
        for element in new_co_ordinate:
            output.append(element[0])
        return output

    def transform_conic_function(self, x, function, matrix):
        """
        One to many functions require special attention. This function will transform two points to new co ordinates
        as opposed to just one.
        """
        outputs = []
        for co_ordinates in function(x):
            co_ordinate = [[x], [co_ordinates]]
            new_co_ordinate = self.matrix_multiply(matrix, co_ordinate)
            outputs.append([new_co_ordinate[0], new_co_ordinate[1]])
        return outputs

    def get_2_d_determinant(self, matrix):
        """
        The n x n dimensional determinant can be found recursively from the root determinant,
        the 2 x 2 determinant.
        """
        determinant = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
        return determinant

    def get_determinant(self, matrix):
        """
        Gets determinant of an n x n matrix.
        """
        return np.linalg.det(matrix)

    def get_inverted_matrix(self, matrix):
        """
        Inverts n x n matrix that is non singular.
        """
        rows = len(matrix)
        empty_matrix = self.get_empty_matrix(rows, rows)
        inv = np.linalg.inv(matrix)
        for i in range(rows):
            for j in range(rows):
                empty_matrix[i][j] = inv[i][j]
        return empty_matrix

    def get_eigenvalues(self, matrix):
        return np.linalg.eigvals(matrix)[0]

    def get_eigenvectors(self, matrix):
        return np.linalg.eig(matrix)[1]

    def solve_system_of_equations(self, matrix, vector):
        """
        Solving Ax = b, where x is a vector of unkowns, so x = inv(A)b.
        Only works when x has the same length as A and A is non singular.
        """
        if len(matrix) != len(vector) or self.get_determinant(matrix) == 0:
            return "Error! Invalid vector or singular matrix entered."
        matrix_inverse = self.get_inverted_matrix(matrix)
        return self.matrix_multiply(matrix_inverse, vector)
