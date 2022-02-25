class Matrix:
    val = False
    def __init__(self,matrix):
        self.matrix = matrix
        k = len(matrix[0])
        if k == 0:
            self.val = True
            return 'Это не матрица'

        for i in matrix:
            if len(i) != k:
                self.val = True
                return 'Это не матрица'

    def transport(self):
        return [list(r) for r in zip(*self.matrix)]

a = Matrix([[1,2,3],[1,2,3],[1,2,3]])
print(a.transport())