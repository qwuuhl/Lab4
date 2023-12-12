'''
На шаховій дошці стоїть король.
Відзначте положення короля на дошці і всі клітинки, які б’є король.
Клітинку, де стоїть король, відзначте буквою K, клітинки, які б’є король,
відзначте символами *,решта клітинок заповніть крапками.
Програма отримує на вхід координати короля на шаховій дошці в шаховій нотації,
тобто, у вигляді e2, де спочатку записується номер стовпця (буква від a до h, зліва направо),
потім номер рядка (цифра від 1 до 8, знизу догори).
Виведіть на екран зображення шахової дошки як у вихідних даних.

Автор: Задворна Анастасія Богданівна
'''

king_position = input()

chessboard = []

for i in range(8):
    row = []
    for j in range(8):
        row.append('.')
    chessboard.append(row)

CHARACTER_TO_NUMBER = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6,
    'g': 7,
    'h': 8
}

king_column = CHARACTER_TO_NUMBER[king_position[0]] - 1
king_row = int(king_position[1]) - 1
chessboard[king_row][king_column] = 'K'

for i in range(max(0, king_row - 1), min(8, king_row + 2)):
    for j in range(max(0, king_column - 1), min(8, king_column + 2)):
        chessboard[i][j] = '*' if chessboard[i][j] != 'K' else 'K'

for i in range(8):
    for j in range(8):
        print(chessboard[i][j], end=' ')
    print()
