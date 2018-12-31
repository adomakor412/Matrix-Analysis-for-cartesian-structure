class Matrix: #matrices are lists; scalers are floats
    def __init__(self):
        return

    def addMatrices(self, matrix1, matrix2): 
        return [
            [matrix1[m][n] + matrix2[m][n] for n in range(len(matrix1[m]))]
            for m in range(len(matrix1))
        ]

    def subtractMatrices(self, matrix1, matrix2):
        return self.addMatrices(matrix1, self.scaleMatrix(matrix2, int(-1)))       

    def multiplyMatrices(self, matrix1, matrix2):
        return [
            sum([matrix1[m][r]*matrix2[r][n] for r in range(len(matrix2))])
            for m in range(len(matrix1))
            for n in range(len(matrix2[0])) 
        ]

    def scaleMatrix(self, matrix, scaler):
        return [
            [matrix[m][n] * scaler for n in range(len(matrix[m]))]
            for m in range(len(matrix))
        ]

    def inverse(self, matrix):#calculate inverse of matrix using adjoint method
        det = self.determinant(matrix)
        cofactor = [
             float(-1)**((m+1)+(n+1)) * minor(matrix,m+1,n+1)
             for m in range(len(matrix))
             for n in range(len(matrix[0])) 
        ]
        adjugate = self.transpose(cofactor)

        def minor(matrix,m,n):
            myMatrix = list(matrix)
            if len(myMatrix)>1:
                del myMatrix[m-1] #expands along row m

            column = range(len(matrix[0]))
            if len(myMatrix[0])>1:
                del column[n-1] #expands along column n

            expand = [
                [myMatrix[i][j] for j in column]
                for i in range(len(myMatrix))
            ]
            return self.determinant(expand)
        
        return self.scaleMatrix(adjugate,float(1/det))

    def identity(self, size):
        return [
            [0 if m!=n else 1 for n in len(size)]
            for m in len(size)
        ]

    def determinant(self, matrix):
        '''
        find determinant by expansion of minors
        '''
        myMatrix = matrix
        if len(myMatrix)==1:
            return float(1/myMatrix[0][0])
        
        mySum = 0
        columms = range(len(myMatrix[0]))
        for exp in range(len(myMatrix[0])):#expand along first row
            minors_1n = [
                [ myMatrix[m][n] for n in columns[:m]+columns[m+1:] ]
                for m in range(len(myMatrix))
            ]
            mySum+= myMatrix[exp] * ((-1)**exp) * self.determinant(minors_1n)
        return mySum
    
    def transform(self, matrix):
        return [
            [matrix[n][m] for n in len(matrix)]
            for m in len(matrix)
        ]
