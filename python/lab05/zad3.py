# print("************* zad3 *************")

matrix = [[1, 2, 3], [7, 5, 6], [4, 8, 9]]
print(matrix)


# największą wartość w każdym wierszu macierzy 
max_row = list(map(lambda x: max(x), matrix))
print(max_row)


# największą wartość w każdej kolumnie macierzy
max_column = list(map(lambda x: max(x), zip(matrix[0], matrix[1], matrix[2])))
print(max_column)