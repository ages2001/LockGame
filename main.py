def main():
    p1_char, p2_char = '', ''

    while p1_char.upper() == p2_char.upper():
        while len(p1_char) != 1:
            p1_char = input("\nEnter a character to represent the first player: ")

            if len(p1_char) != 1:
                print("Invalid character!")

        while len(p2_char) != 1:
            p2_char = input("\nEnter a character to represent the second player: ")

            if len(p2_char) != 1:
                print("Invalid character!")

        if p1_char.upper() == p2_char.upper():
            print("Both players can't have the same stones!")
            p1_char, p2_char = '', ''

    operation = 'y'

    while operation.upper() == 'Y':
        row, column = 0, 0

        while row < 4 or row > 8:
            try:
                row = int(input("\nEnter the row of table (4-8): "))

            except ValueError:
                print("Row of the game table must be integer!")

            else:
                if row < 4 or row > 8:
                    print("Row of the game table must between 4-8!")

        game_table = create_table(row, p1_char, p2_char)
        p1_stones, p2_stones = count_stones(game_table, p1_char, p2_char)

        print(f"\nPlayer 1's number of stone: {p1_stones}")
        print(f"Player 2's number of stone: {p2_stones}")

        print_table(game_table)

        while p1_stones >= 2 and p2_stones >= 2:
            while True:
                p1_move = input("\nPlayer 1, enter your move: ")

                if is_valid_move(game_table, p1_move, p1_char, p2_char):
                    break

            print_table(game_table)
            check_and_remove_stones(game_table, p1_char)

            p1_stones, p2_stones = count_stones(game_table, p1_char, p2_char)
            if p1_stones < 2 or p2_stones < 2:
                break

            while True:
                p2_move = input("\nPlayer 2, enter your move: ")

                if is_valid_move(game_table, p2_move, p2_char, p1_char):
                    break

            print_table(game_table)
            check_and_remove_stones(game_table, p2_char)

            p1_stones, p2_stones = count_stones(game_table, p1_char, p2_char)


        if p2_stones < 2:
            print("\nPLAYER 1 WON!\n")

        else:
            print("\nPLAYER 2 WON!\n")

        while True:
            operation = input("Do you want to play again (Y/N)?: ")

            if operation.upper() == 'Y' or operation.upper() == 'N':
                break

    print("Exiting...")


def create_table(row, p1_char, p2_char):
    column = row
    table, row_list = [], []

    for i in range(column):
        row_list.append(p2_char)

    table.append(row_list)

    for i in range(1, row - 1):
        row_list = []

        for j in range(column):
            row_list.append(' ')

        table.append(row_list)

    row_list = []

    for i in range(column):
        row_list.append(p1_char)

    table.append(row_list)

    return table


def print_table(table):
    row, column = len(table), len(table[0])

    print("\n\n ", end="")
    for i in range(column):
        print(f"   {chr(ord('A') + i)}", end="")

    print()
    for i in range(row):
        print("  ", end="")

        for k in range(4 * column + 1):
            print("-", end="")

        print(f"\n{i + 1} ", end="")

        for j in range(column):
            print(f"| {table[i][j]} ", end="")

        print(f"| {i + 1}")

    print("  ", end="")
    for i in range(4 * column + 1):
        print("-", end="")

    print("\n ", end="")
    for j in range(column):
        char = chr(ord('A') + j)
        print(f"   {char}", end="")

    print("\n")


def check_and_remove_stones(table, char):
    row, column = len(table), len(table[0])
    display_table_after_change = False

    for i in range(row):
        for j in range(column):
            pos_x, pos_y = -1, -1

            if table[i][j] != ' ' and table[i][j] != char:
                if i == 0 and j == 0:
                    if table[i][j + 1] == table[i + 1][j] and table[i][j + 1] != ' ' and table[i][j] != table[i][j + 1]:
                        table[i][j] = ' '
                        pos_x, pos_y = i, j
                        display_table_after_change = True

                elif i == row - 1 and j == 0:
                    if table[i][j + 1] == table[i - 1][j] and table[i][j + 1] != ' ' and table[i][j] != table[i][j + 1]:
                        table[i][j] = ' '
                        pos_x, pos_y = i, j
                        display_table_after_change = True

                elif i == row - 1 and j == column - 1:
                    if table[i][j - 1] == table[i - 1][j] and table[i][j - 1] != ' ' and table[i][j] != table[i][j - 1]:
                        table[i][j] = ' '
                        pos_x, pos_y = i, j
                        display_table_after_change = True

                elif i == 0 and j == column - 1:
                    if table[i][j - 1] == table[i + 1][j] and table[i][j - 1] != ' ' and table[i][j] != table[i][j - 1]:
                        table[i][j] = ' '
                        pos_x, pos_y = i, j
                        display_table_after_change = True

                elif i == 0 or i == row - 1:
                    if table[i][j - 1] == table[i][j + 1] and table[i][j - 1] != ' ' and table[i][j] != table[i][j - 1]:
                        table[i][j] = ' '
                        pos_x, pos_y = i, j
                        display_table_after_change = True

                elif j == 0 or j == column - 1:
                    if table[i - 1][j] == table[i + 1][j] and table[i - 1][j] != ' ' and table[i][j] != table[i - 1][j]:
                        table[i][j] = ' '
                        pos_x, pos_y = i, j
                        display_table_after_change = True

                else:
                    if (table[i - 1][j] == table[i + 1][j] and table[i - 1][j] != ' ' and table[i][j] != table[i - 1][j]) or (table[i][j - 1] == table[i][j + 1] and table[i][j - 1] != ' ' and table[i][j] != table[i][j - 1]):
                        table[i][j] = ' '
                        pos_x, pos_y = i, j
                        display_table_after_change = True


            if pos_x != -1 and pos_y != -1:
                print(f"The stone in position {pos_x + 1}{chr(pos_y + 65)} is locked and removed.")


    if display_table_after_change:
        print_table(table)


def count_stones(table, p1_char, p2_char):
    row, column = len(table), len(table[0])
    p1_stones, p2_stones = 0, 0

    for i in range(row):
        for j in range(column):
            if table[i][j] == p1_char:
                p1_stones += 1

            elif table[i][j] == p2_char:
                p2_stones += 1

    return p1_stones, p2_stones


def is_valid_move(table, move, char, other_char):
    if len(move) != 5:
        print("Invalid move entered!")
        return False

    if move[2] != ' ':
        print("Invalid move entered!")
        return False

    move = move[:1] + move[1].upper() + move[2:4] + move[4].upper()
    current_location, next_location = move[:2], move[-2:]

    try:
        cur_row, cur_col = int(current_location[0]) - 1, ord(current_location[1]) - 65
        next_row, next_col = int(next_location[0]) - 1, ord(next_location[1]) - 65

    except ValueError:
        print("Invalid move entered!")
        return False

    table_row, table_col = len(table), len(table[0])

    if cur_row >= table_row or next_row >= table_row or cur_col >= table_col or next_col >= table_col or cur_row < 0 or cur_col < 0 or next_row < 0 or next_col < 0:
        print("Invalid move entered!")
        return False

    if table[cur_row][cur_col] == ' ':
        print("Current location is empty!")
        return False

    if table[cur_row][cur_col] == other_char:
        print("You can't play other player's stone!")
        return False

    if table[next_row][next_col] != ' ':
        print("Next location is not empty!")
        return False

    if cur_row != next_row and cur_col != next_col:
        print("You can't play the stone diagonally!")
        return False

    if cur_row == next_row and cur_col == next_col:
        print("Current and next locations are same!")
        return False

    if is_jump_stone(table, current_location, next_location):
        print("You can't jump over stone(s)")
        return False

    table[cur_row][cur_col] = ' '
    table[next_row][next_col] = char

    return True


def is_jump_stone(table, current_location, next_location):
    cur_row, cur_col = int(current_location[0]) - 1, ord(current_location[1]) - 65
    next_row, next_col = int(next_location[0]) - 1, ord(next_location[1]) - 65

    if cur_col == next_col:
        if cur_row < next_row:
            for i in range(cur_row, next_row - 1):
                if table[i + 1][cur_col] != ' ':
                    return True

        else:
            for i in range(next_row, cur_row - 1):
                if table[i + 1][cur_col] != ' ':
                    return True

    else:
        if cur_col < next_col:
            for j in range(cur_col, next_col - 1):
                if table[cur_row][j + 1] != ' ':
                    return True

        else:
            for j in range(next_col, cur_col - 1):
                if table[cur_row][j + 1] != ' ':
                    return True

    return False


if __name__ == '__main__':
    main()
