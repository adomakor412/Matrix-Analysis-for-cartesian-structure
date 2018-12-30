class Matrix: #matrices are lists; scalers are floats
    def __init__(self):
        return
    def addMatrices(self, matrix1, matrix2):
        return [
            [matrix1[m][n] + matrix2[m][n] for n in range(len(matrix1[m]))]
            for m in range(len(matrix1))
        ]
    def subtractMatrices(self, matrix1, matrix2):
        myMatrix = addMatrices(matrix1, scaleMatrix(matrix2, float(-1))
        return myMatrix
    def multiplyMatrices(self, matrix1, matrix2):
        return
    def scaleMatrix(self, matrix1, scaler):
        return
    def inverse(self, matrix1):
        return
    def identity(self, size):
        return
    def determinant(self, matrix1):
        return


