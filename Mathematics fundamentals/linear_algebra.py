class Linalg:
    def get_empty_row(self,length):
        row = []
        for i in range(length):
            row.append(0)
        return row

    def get_empty_matrix(self,rows,columns):
        matrix = []
        for i in range(rows):
            matrix.append(self.get_empty_row(columns))
        return matrix
        
    def get_transpose(self,mat1):
        rows = len(mat1)
        columns = len(mat1[0])
        transpose = self.get_empty_matrix(columns,rows)
        for i in range(rows):
            for j in range(columns):
                transpose[j][i] = mat1[i][j]
        return transpose

    def matrix_multiply(self,mat1,mat2):
        """
        Matrix multiplication works by multiplying rows by columns pairwise. Thus if mat1
        does not have the same number of rows as mat2 does columns, we cannot multiply them.

        Note: mat1 will be a list of lists to simulate a matrix:
            mat1 = [ [1,2,3] 
                     [4,5,6]
                     [7,8,9]   ] 3x3 matrix.
        For example.

        In essence we can only multiply matrices with dimensions k x n and m x k, the resulting matrix
        will have dimension n x m.
        """
        mat1_rows = len(mat1)
        mat2_columns = len(mat2[0])
        if mat1_rows != mat2_columns:
            return f"Error, matrix one has {mat1_rows}  rows and matrix two has {mat2_columns} columns."
        pass



