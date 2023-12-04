# Функция для создания матрицы заданного размера и заполнения элементов
def create_matrix(size):
    matrix = []
    for i in range(size):
        row = []
        for j in range(size):
            row.append(i * j)  # Заполняем элементы матрицы произведением индексов
        matrix.append(row)
    return matrix

# Функция для замены элементов на диагоналях
def replace_diagonals(matrix):
    size = len(matrix)
    for i in range(size):
        for j in range(size):
            if i == j or i + j == size - 1:  # Проверяем элементы на главной и побочной диагоналях
                matrix[i][j] = 1  # Заменяем элементы на единицы
    return matrix

# Задаем размер матрицы
matrix_size = int(input("Введите размер матрицы: "))

# Создаем матрицу и выводим ее до замены элементов на диагоналях
matrix = create_matrix(matrix_size)
print("Исходная матрица:")
for row in matrix:
    print(row)

# Заменяем элементы на диагоналях
matrix = replace_diagonals(matrix)

# Выводим матрицу после замены элементов на диагоналях
print("\nМатрица после замены элементов на диагоналях:")
for row in matrix:
    print(row)
