import numpy as np
import random as rd
from matplotlib import pyplot as plt


def index_shuffle():
    shuffle_index = []
    for i in range(3):
        index_1 = list(range(i * 3, i * 3 + 3))
        rd.shuffle(index_1)
        shuffle_index += index_1
    return shuffle_index

def shuffle_row(s):
    s_row = {}
    index = list(range(9))
    shuffle_index = index_shuffle()
    for i in index:
        s_row[shuffle_index[i]] = s[i*9:i*9+9]
    row_shuffled = []
    for i in range(9):
        row_shuffled += s_row[i]
    return row_shuffled

def shuffle_col(s):
    s_col = {}
    index = list(range(9))
    shuffle_index = index_shuffle()
    for i in index:
        s_col[shuffle_index[i]] = [s[i], s[i+9], s[i+18], s[i+27], s[i+36],
                                   s[i+45], s[i+54], s[i+63], s[i+72]]
    col_shuffled = []
    for i in range(9):
        col_shuffled += s_col[i]
    return col_shuffled

def shuffle(s):
    s = shuffle_row(s)
    s = shuffle_col(s)
    return s

def gen():
    row = list(range(1, 10))
    rd.shuffle(row)
    order = [1, 2, 3, 4, 5, 6, 7, 8, 9,
             4, 5, 6, 7, 8, 9, 1, 2, 3,
             7, 8, 9, 1, 2, 3, 4, 5, 6,
             2, 3, 1, 5, 6, 4, 8, 9, 7,
             5, 6, 4, 8, 9, 7, 2, 3, 1,
             8, 9, 7, 2, 3, 1, 5, 6, 4,
             3, 1, 2, 6, 4, 5, 9, 7, 8,
             6, 4, 5, 9, 7, 8, 3, 1, 2,
             9, 7, 8, 3, 1, 2, 6, 4, 5,
             ]
    s = []
    for i in range(81):
        s.append(row[order[i]-1])
    return s

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
    s = gen()
    s = shuffle(s)
    display(s)





