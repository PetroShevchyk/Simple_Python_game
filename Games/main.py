# Хрестики-нолики

# Створюємо поле 3x3
board = [[' ' for _ in range(3)] for _ in range(3)]

# Функція для виведення поля на екран
def print_board():
    for row in range(3):
        print('|'.join(board[row]))
        if row < 2:
            print('-' * 5)


def check_winner():
    for row in board:
        if row[0] == row[1] == row[2] != ' ':
            return True

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != ' ':
            return True

    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return True
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return True

    return False

# Основний цикл гри
current_player = 'X'
while True:
    print_board()
    print("Гравець", current_player, "ходить.")

    # Запитуємо користувача про хід
    row = int(input("Введіть номер рядка (1-3): ")) - 1
    col = int(input("Введіть номер стовпця (1-3): ")) - 1

    # Перевірка дозволеності ходу
    if board[row][col] != ' ':
        print("Ця клітинка вже зайнята. Спробуйте ще раз.")
        continue

    # Записуємо хід гравця на поле
    board[row][col] = current_player

    # Перевірка на перемогу
    if check_winner():
        print_board()
        print("Гравець", current_player, "переміг!")
        break

    # Перевірка на нічию
    if all(board[i][j] != ' ' for i in range(3) for j in range(3)):
        print_board()
        print("Гра закінчилась в нічию!")
        break

    # Зміна гравця
    current_player = 'O' if current_player == 'X' else 'X'
