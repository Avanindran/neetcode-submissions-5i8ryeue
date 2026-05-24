
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        #reverse the order of the rows and then transpose the matrix. (i, j) -> (j, i)

        matrix.reverse()

        for i in range(len(matrix)):

            for j in range(i + 1, len(matrix[0])):

                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        

        
