def transpose(matrix):
    rows = len(matrix)
    columns = len(matrix[0])

    transposed_matrix = []

    for x in range(columns):
        new_rows = []
        for y in range(rows):
            new_rows.append(0)
        transposed_matrix.append(new_rows)

    for x in range(columns):
        for y in range(rows):
            transposed_matrix[x][y] = matrix[y][x]

    return transposed_matrix
    
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(transpose(matrix))

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6]
# ]
# print(transpose(matrix))
