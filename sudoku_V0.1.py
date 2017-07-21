import random as rd
import copy


class Sudoku:
    """It generates a random sudoku puzzle and is able to show the puzzle and
    the solution."""
    def __init__(self):
        def determine_loc(loc):
            for i in range(9):
                if loc >= i * 9:
                    n_row = i
            n_col = loc % 9

            block_head = [0, 3, 6, 27, 30, 33, 54, 57, 60]
            for i, head_num in enumerate(block_head):
                block_full = [head_num, head_num + 1, head_num + 2,
                              head_num + 9, head_num + 10,
                              head_num + 11, head_num + 18, head_num + 19,
                              head_num + 20]
                if loc in block_full:
                    n_block = i

            return n_row, n_col, n_block

        def record(loc, a, row_s, col_s, block_s):
            n_row, n_col, n_block = determine_loc(loc)
            row_s[n_row].append(a)
            col_s[n_col].append(a)
            block_s[n_block].append(a)
            return row_s, col_s, block_s

        row, col, block = {}, {}, {}
        for i in range(9):
            row[i], col[i], block[i] = [], [], []
        choice_full = list(range(1, 10))

        for mult in range(9):
            row_temp = copy.deepcopy(row)
            col_temp = copy.deepcopy(col)
            block_temp = copy.deepcopy(block)

            i = 0
            while True:
                loc = mult * 9 + i
                n_row, n_col, n_block = determine_loc(loc)
                choice_used = row_temp[n_row] + col_temp[n_col] + block_temp[
                    n_block]
                choice = [item for item in choice_full if
                          item not in choice_used]
                if choice:
                    a = rd.choice(choice)
                else:
                    i = 0
                    row_temp = copy.deepcopy(row)
                    col_temp = copy.deepcopy(col)
                    block_temp = copy.deepcopy(block)
                    continue
                row_temp, col_temp, block_temp = record(loc, a, row_temp,
                                                        col_temp, block_temp)
                i += 1
                if i > 8:
                    break
            row = copy.deepcopy(row_temp)
            col = copy.deepcopy(col_temp)
            block = copy.deepcopy(block_temp)

        s = []
        for values in row.values():
            s += values
        self.solution = s

    def show_puzzle(self, n=20):
        s = copy.deepcopy(self.solution)
        empty_choice = list(range(80))
        rd.shuffle(empty_choice)
        for i in range(n):
            i_1 = empty_choice[i]
            s[i_1] = ' '
        display(s)

    def show_solution(self):
        display(self.solution)

def display(s):
    for i in range(9):
        row_str = []
        for a_1 in s[9 * i:9 * i + 9]:
            row_str.append(str(a_1))
        print(' '.join(row_str[0:3]), '|', ' '.join(row_str[3:6]), '|',
              ' '.join(
                  row_str[6:9]))
        if i == 2 or i == 5:
            print('- - - - - - - - - - -')

if __name__ == '__main__':
    print('Welcome to the Sudoku Game! -- JoJoX')
    while True:
        n = input('Type a number for difficulty...')
        trial = Sudoku()
        try:
            trial.show_puzzle(int(n))
        except ValueError:
            print('You entered a invalid number. I assume you mean 20.')
            trial.show_puzzle()
        k = input("\nPress Any Key to See the Answer...\n")
        trial.show_solution()
        k = input("\nPress any key to go to the next puzzle...\n"
                  "Type 'q' to quit...\n")
        if k == 'q':
            break
