class Matrix: #matrices are lists; scalers are floats
    def __init__(self):
        return
    def addMatrices(self, matrix1, matrix2):
        myMatrix = [
            [matrix1[m][n] + matrix2[m][n] for n in range(len(matrix1[m]))]
            for m in range(len(matrix1))
        ]
        return myMatrix
    def subtractMatrices(self, matrix1, matrix2):
        return
    def multiplyMatrices(self, matrix1, matrix2):
        return
    def multiplyMatrix(self, matrix1, scaler):
        return
    def inverse(self, matrix1):
        return
    def identity(self, size):
        return
    def determinant(self, matrix1):
        return


