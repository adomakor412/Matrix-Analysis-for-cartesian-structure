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

    def scaleMatrix(self, matrix1, scaler):
        return [
            [matrix1[m][n] * scaler for n in range(len(matrix1[m]))]
            for m in range(len(matrix1))
        ]

    def inverse(self, matrix1):
        return

    def identity(self, size):
        return

    def determinant(self, matrix1):
        return

myMatrix = Matrix()
print(myMatrix.subtractMatrices([[1],[2]],[[3],[4]]))
                           
