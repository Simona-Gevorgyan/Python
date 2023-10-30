class Matrix:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.matrix = [[0] * m for _ in range(n)]

    def fill_matrix(self):
        for i in range(self.n):
            for j in range(self.m):
                self.matrix[i][j] = int(input(f"Enter value at position ({i}, {j}): "))

    def print_matrix(self):
        for row in self.matrix:
            print(row)

    def mean(self):
        total = 0
        count = self.n * self.m
        for i in range(self.n):
            for j in range(self.m):
                total += self.matrix[i][j]
        return total / count

    def sum_row(self, row_num):
        if 0 <= row_num < self.n:
            return sum(self.matrix[row_num])
        else:
            return None

    def average_column(self, col_num):
        if 0 <= col_num < self.m:
            total = 0
            for i in range(self.n):
                total += self.matrix[i][col_num]
            return total / self.n
        else:
            return None

    def submatrix(self, col1, col2, row1, row2):
        if 0 <= row1 <= row2 < self.n and 0 <= col1 <= col2 < self.m:
            for i in range(row1, row2 + 1):
                print(self.matrix[i][col1:col2 + 1])
        else:
            print("Invalid submatrix coordinates.")


# Example usage:
n = 3
m = 4
my_matrix = Matrix(n, m)
my_matrix.fill_matrix()

print("Matrix:")
my_matrix.print_matrix()

print(f"Mean of the matrix: {my_matrix.mean()}")

row_num = 1
print(f"Sum of row {row_num}: {my_matrix.sum_row(row_num)}")

col_num = 2
print(f"Average of column {col_num}: {my_matrix.average_column(col_num)}")

col1, col2, row1, row2 = 1, 3, 0, 2
print("Submatrix:")
my_matrix.submatrix(col1, col2, row1, row2)
