# from os import stat
# from os import stat
import numpy as np


class Matrix:

    """
    In this class I intend to implement all of linear algebra so that it can be applied to
    future projects.
    """

    def __init__(self,*args:list):
        self.matrix = []
        for row in args:
            self.matrix.append(row)
        self.rows = len(self.matrix)
        self.columns = len(self.matrix[0])

    def show_matrix(self):
        """
        Gives visual representation of a matrix.
        """
        print('[')
        for row in self.matrix:
            print(str(row))
        print(']')

    def add_rows(self,*rows):
        """
        Adds rows to a matrix object.
        """
        for row in rows:
            self.matrix.append(row)
        return f"{len(rows)} rows added!"
    
    def add_columns(self,*columns):
        """
        Adds columns to a matrix object
        """
        for column in columns:
            for index,value in enumerate(column):
                self.matrix[index].append(value)
        return f"{len(columns)} columns added!"


    @staticmethod
    def get_empty_row(length):
        """
        returns an row vector of zeros.
        """
        row = Vector()
        zeros = [0]*length
        row.add_entries(*zeros)
        return Vector.unpack_vector(row)

    def get_empty_matrix(self, rows, columns):
        """
        Returns a rows x columns matrix with zeros for every entry.
        """
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
    
    def unpack_vector(self,vector):
        """
        Will unpack a vector into its components.
        """
        unpacked_vector = []
        for i in vector:
            unpacked_vector.append(i[0])
        return unpacked_vector
    
    def get_cross_product(self,vector1,vector2):
        """
        Will calculate the cross product between two vectors. These vectors must be three dimensional.
        note vectors must be in the form of:
        v = [
            [v1],
            [v2],
            [v3]
        ]
        """
        v1,v2,v3 = self.unpack_vector(vector1)
        w1,w2,w3 = self.unpack_vector(vector2)

        cross_vector = [
            [v2*w3 - v3*w2],
            [v3*w1 - v1*w3],
            [v1*w2 - v2*w3]
        ]
        return cross_vector
    
    def matrix_from_vectors(self,*args):
        """
        Creating a matrix from vectors passed in as args. Note that we can only do this if all the inputted vectors
        have the right shape.
        """
        columns = len(args)
        rows = len(args[0])
        matrix = self.get_empty_matrix(rows,columns)
        for column,vector in enumerate(args):
            for row in range(rows):
                matrix[row][column] = vector[row]
        return matrix


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
        """
        Will get the eigenvalues of a matrix
        """
        return np.linalg.eigvals(matrix)[0]

    def get_eigenvectors(self, matrix):
        """
        Will get the eigenvectors of a matrix
        """
        return np.linalg.eig(matrix)[1]

    def diagonalise_matrix(self,matrix):
        """
        Will diagonalise a matrix if that is possible (i.e if all eigenvalues are non degenerate.)
        """


    def solve_system_of_equations(self, matrix, vector):
        """
        Solving Ax = b, where x is a vector of unkowns, so x = inv(A)b.
        Only works when x has the same length as A and A is non singular.
        """
        if len(matrix) != len(vector) or self.get_determinant(matrix) == 0:
            return "Error! Invalid vector or singular matrix entered."
        matrix_inverse = self.get_inverted_matrix(matrix)
        return self.matrix_multiply(matrix_inverse, vector)

class Vector:

    def __init__(self,*args:int):
        self.vector = [[arg] for arg in args]

    def __add__(self,other):
        """
        Will add vectors component wise, only if they're the same shape.
        """
        v1 = self.vector
        v2 = other.vector
        dimv1 = len(v1)
        dimv2 = len(v2)
        packed_args = []
        if dimv1 == dimv2:
            for i in range(dimv1):
                packed_args.append(v1[i][0] + v2[i][0])
            return Vector(*packed_args)
        else:
            raise TypeError('Dimensions not equal.')
                
    def change_entry(self,new_entry,index):
        self.vector[index] = [new_entry]
        return f"Entry changed to {new_entry}"

    def add_entries(self,*new_entries):
        for entry in new_entries:
            self.vector.append([entry])
        return f"entries added!"

    def show_vector(self):
        """
        Visually showing a vector.
        """
        print('[')
        for index,component in enumerate(self.vector):
            if index == len(self.vector)-1:
                print(str(component))
            else:
                print(str(component) + ',')
        print(']')

    @staticmethod
    def get_dot_product(vector1, vector2) -> float:
        """
        Calculates the dot product between two vectors of equal length.
        """
        v_1_dim = len(vector1.vector)
        v_2_dim = len(vector2.vector)
        v1 = vector1.vector
        v2 = vector2.vector
        if v_1_dim != v_2_dim:
            raise TypeError(f"""Vector 1 has length {v_1_dim}, and vector 2 has length {v_2_dim}. 
            These must be equal.""")
        sum = 0
        for i in range(v_2_dim):
            sum += v1[i][0] * v2[i][0]
        return sum

    @staticmethod
    def unpack_vector(vector):
        """
        Will unpack a vector into its components, and then into an array.

        a = [
            [1],
            [2],
            [3]
        ]
        Vector.unpack(a) = [1,2,3]. This effectively transposes a vector!
        """
        unpacked_vector = []
        for i in vector.vector:
            unpacked_vector.append(i[0])
        return unpacked_vector

    @staticmethod
    def get_cross_product(vector1,vector2):
        """
        Will calculate the cross product between two vectors. These vectors must be three dimensional.
        note vectors must be instances of Vector.
        """
        v1,v2,v3 = Vector.unpack_vector(vector1)
        w1,w2,w3 = Vector.unpack_vector(vector2)

        cross_vector = [
            [v2*w3 - v3*w2],
            [v3*w1 - v1*w3],
            [v1*w2 - v2*w3]
        ]
        return cross_vector

    
    

if __name__ == '__main__':
    a = Vector(1,1,1)
    b = Vector(1,3,1)
    c = Vector(1,1,1)
    d = a + b + c
    unpacked_d = Vector.unpack_vector(d)
    e = Vector.get_dot_product(a,b)
    f = Vector.get_cross_product(a,b)


    M = Matrix(
        [1,2,3],
        [4,5,6],
        [7,8,9]
    )
    M.add_rows([1,2,3])
    M.show_matrix()
    

    

    
