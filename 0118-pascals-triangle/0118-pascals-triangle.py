class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []
        for rn in range(numRows):
            row = [1] * (rn + 1)
            for j in range(1, rn):
                row[j] = triangle[rn - 1][j - 1] + triangle[rn - 1][j]
            triangle.append(row)
        return triangle