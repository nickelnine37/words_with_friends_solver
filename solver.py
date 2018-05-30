from itertools import permutations, combinations, chain, product, groupby
from operator import itemgetter
import numpy as np
from pprint import pprint


with open('dictionary.txt', 'r') as f:
    dictionary = f.read().splitlines()

dls = [(2, 4), (2, 6), (4, 2), (4, 8),
       (6, 2), (6, 8), (8, 4), (8, 6)]

tls = [(0, 0), (2, 2), (3, 3), (7, 7), (8, 8), (10, 10),
       (0, 10), (2, 8), (3, 7), (10, 0), (8, 2), (7, 3)]

dws = [(1, 1), (9, 9), (1, 5), (1, 9),
       (5, 9), (5, 1), (9, 1), (1, 5), (9, 5)]

tws = [(0, 2), (0, 8), (2, 10), (8, 10),
       (2, 0), (8, 0), (10, 2), (10, 8)]


points = {'a': 1,
          'b': 4,
          'c': 4,
          'd': 2,
          'e': 1,
          'f': 4,
          'g': 3,
          'h': 3,
          'i': 1,
          'j': 10,
          'k': 5,
          'l': 2,
          'm': 4,
          'n': 2,
          'o': 1,
          'p': 4,
          'q': 10,
          'r': 1,
          's': 1,
          't': 1,
          'u': 2,
          'v': 5,
          'w': 4,
          'x': 8,
          'y': 3,
          'z': 10,
          ' ': 0}

tiles = {'a': 5,
         'b': 1,
         'c': 1,
         'd': 2,
         'e': 7,
         'f': 1,
         'g': 1,
         'h': 1,
         'i': 4,
         'j': 1,
         'k': 1,
         'l': 2,
         'm': 1,
         'n': 2,
         'o': 4,
         'p': 1,
         'q': 1,
         'r': 2,
         's': 4,
         't': 2,
         'u': 1,
         'v': 1,
         'w': 1,
         'x': 1,
         'y': 1,
         'z': 1,
         ' ': 2, }


def sort_dict():
    sorted_dict = {}
    alphabet = 'abcdefghijklmnopqrstuvwxyz '
    for letter1 in alphabet:
        for letter2 in alphabet:
            for letter3 in alphabet:
                sorted_dict[letter1 + letter2 + letter3] = []
    for word in dictionary:
        letters = word[:3]
        l = len(letters)
        if l == 3:
            sorted_dict[letters].append(word)
        elif l == 2:
            sorted_dict[letters + ' '].append(word)
        elif l == 1:
            sorted_dict[letters + '  '].append(word)

    return sorted_dict


sorted_dict = sort_dict()


def exists(word):
    letters = word[:3]
    l = len(letters)
    if l == 3:
        return word in sorted_dict[letters]
    elif l == 2:
        return word in sorted_dict[letters + ' ']
    elif l == 1:
        return word in sorted_dict[letters + '  ']


def find_words_simple(letters):
    all_combs = []
    all_perms = []
    for n in range(1, 8):
        all_combs += [''.join(p) for p in combinations(letters, n)]
    for comb in all_combs:
        all_perms += [''.join(p) for p in permutations(comb)]
    all_perms = set(all_perms)
    all_words = []
    for perm in all_perms:
        if exists(perm):
            all_words.append(perm)
    return all_words


class Board:

    def __init__(self, letters=None):
        self.letters = np.chararray((11, 11), itemsize=1, unicode=True)
        self.powers = np.chararray((11, 11), itemsize=3, unicode=True)
        if type(letters) != type(None):
            self.letters = letters
        for x in range(11):
            for y in range(11):
                square = (x, y)
                power = ''
                letter = ''
                if square in dls:
                    power = 'dlr'
                if square in tls:
                    power = 'tlr'
                if square in dws:
                    power = 'dwr'
                if square in tws:
                    power = 'twr'
                if type(letters) == type(None):
                    self.letters[x, y] = letter
                self.powers[x, y] = power

    def print_powers(self):
        print("  A   B   C   D   E   F   G   H   I   J   K  ")
        print(" " + '-' * 11 * 4)
        for y in reversed(range(11)):
            for x in range(11):
                power = self.powers[x, y]
                if power == '':
                    power = '   '
                print("|" + power, end="", flush=True)
            print('| {}'.format(11 - y), '\n', '-' * 11 * 4)

    def print_letters(self):
        print("  A   B   C   D   E   F   G   H   I   J   K  ")
        print(" " + '-' * 11 * 4)
        for y in reversed(range(11)):
            for x in range(11):
                letter = str(self.letters[x, y])
                if letter == '':
                    letter = ' '
                print('| ' + letter, end=" ", flush=True)
            print('| {}'.format(11 - y), '\n', '-' * 11 * 4)

    def change_row(self, index, new_row, rtype='row'):
        if rtype == 'row':
            self.letters[:, index] = new_row
            for i in range(11):
                if self.letters[i, index] != '':
                    self.powers[i, index] = ''
        elif rtype == 'col':
            self.letters[index, :] = list(reversed(new_row))
            for i in range(11):
                if self.letters[index, i] != '':
                    self.powers[index, i] = ''
        else:
            print('rtype must be row or col')
        # self.print_letters()

    def add_letter(self, letter, coords='A5'):
        cols = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']
        col = cols.index(coords[0])
        row = int(coords[1]) - 1
        self.letters[col, 10 - row] = letter
        self.powers[col, 10 - row] = ''


MyBoard = Board()
MyBoard.add_letter('f', 'J9')
# MyBoard.change_row(1, ['', '', '', '', '', 'b', 'e', '', '', '', ''], rtype='row')
# MyBoard.change_row(5, ['', '', '', '', '', '', 'd', 'r', 'a', 'b', ''], rtype='col')
# MyBoard.change_row(4, ['', '', '', '', '', 'd', 'a', 'm', 'n', '', ''], rtype='row')
# MyBoard.change_row(3, ['', '', '', '', '', 'r', 'e', '', '', '', ''], rtype='row')
# MyBoard.change_row(6, ['', '', '', '', '', '', 'a', 'e', '', 'e', 'r'], rtype='col')
MyBoard.print_letters()
MyBoard.print_powers()


class Solver:

    def __init__(self, Board, letters):
        self.letters = letters
        self.Board = Board

    def identify_starters(self, row, adjacent1, adjacent2):
        '''
        given a row, in the form of a list, identify the indicies
        where you can 'start' the algorithm below (which amounts
        to finding the indicies where one can place a single
        letter) and also return the occupied indicies and the non-
        starters (everthing that is not a starter or occupied)
        '''
        if adjacent1 == None:
            adjacent1 = [''] * 11
        if adjacent2 == None:
            adjacent2 = [''] * 11
        non_starters = []
        occupied = [index for index in range(len(row)) if row[index] != '']
        for index, item in enumerate(row):
            if index == 0:
                if item == '' and row[1] == '':
                    non_starters.append(index)
            elif index == 10:
                if item == '' and row[9] == '':
                    non_starters.append(index)
            else:
                if item == '' and row[index - 1] == '' and row[index + 1] == '':
                    non_starters.append(index)

        starters = [index for index in range(
            len(row)) if index not in occupied and index not in non_starters]

        for index in non_starters:
            if adjacent1[index] != '' or adjacent2[index] != '':
                non_starters.remove(index)
                starters.append(index)

        return starters, non_starters, occupied

    def find_valid_placements(self, row, adjacent1, adjacent2):
        '''
        Find the set of sets of indices where letters can possibly
        be placed
        '''
        starters, non_starters, occupied = self.identify_starters(row,  adjacent1, adjacent2)
        master_poss = []
        for starter in starters:
            poss = []
            next_nums = list(range(starter + 1, 11))
            next_nums = [num for num in next_nums if num not in occupied]
            for i in range(len(next_nums) + 1):
                poss.append([starter] + next_nums[:i])
            for p in poss:
                master_poss.append(p)
            if starter - 1 in non_starters:
                c = 1
                if starter - 2 in non_starters:
                    c += 1
                    if starter - 3 in non_starters:
                        c += 1
                        if starter - 4 in non_starters:
                            c += 1
                            if starter - 5 in non_starters:
                                c += 1
                                if starter - 6 in non_starters:
                                    c += 1
                                    if starter - 7 in non_starters:
                                        c += 1
                                        if starter - 8 in non_starters:
                                            c += 1
                                            if starter - 9 in non_starters:
                                                c += 1
                                                if starter - 10 in non_starters:
                                                    c += 1

                news = []
                for i in range(c):
                    news.append(list(reversed(range(starter - 1, starter - 1 - (i + 1), -1))))
                for new in news:
                    for old_poss in poss:
                        master_poss.append(new + old_poss)
        grouped = {}
        for item in master_poss:
            try:
                grouped[len(item)].append(item)
            except KeyError:
                grouped[len(item)] = [item]
        return grouped

    def extract_words(self, row):
        row = [' ' if letter == '' else letter for letter in row]
        return [word for word in ''.join(row).split(' ') if len(word) > 1]

    def find_words(self, row, adjacent1, adjacent2):

        valid_placements = self.find_valid_placements(row, adjacent1, adjacent2)
        if valid_placements == {}:
            return []
        big = min([len(self.letters), max(valid_placements.keys())])
        small = min(valid_placements.keys())
        valid_placements = {key: item for key, item in valid_placements.items() if key <= big}
        all_combs = {}
        all_perms = {}
        new_rows = []
        for n in range(small, big + 1):
            all_combs[n] = [''.join(p) for p in combinations(self.letters, n)]
        for key, item in all_combs.items():
            all_perms[key] = list(set([''.join(p) for comb in item for p in permutations(comb)]))
        for n in range(small, big + 1):
            placements = valid_placements[n]
            letterss = all_perms[n]
            for placement in placements:
                for letters in letterss:
                    new_row = row[:]
                    for i, index in enumerate(placement):
                        new_row[index] = letters[i]
                    words = self.extract_words(new_row)
                    for word in words:
                        if not exists(word):
                            break
                        new_rows.append(new_row)
        return new_rows

    def validate(self, number, new_row, rtype='row'):

        test_board = self.Board.letters.copy()

        if rtype == 'row':
            test_board[:, number] = new_row
            for col_num in range(11):
                test_col = list(test_board[col_num, :][::-1])
                words = self.extract_words(test_col)
                for word in words:
                    if not exists(word):
                        return False, None
            return True, test_board

        elif rtype == 'col':
            test_board[number, :] = list(reversed(new_row))
            for row_num in range(11):
                test_row = list(test_board[:, row_num])
                words = self.extract_words(test_row)
                for word in words:
                    if not exists(word):
                        return False, None
            return True, test_board
        else:
            print('rtype must be row or col')

    def extract_word_positions(self, board):

        words = []

        for row_num in range(11):
            row = list(board[:, row_num])
            word = ''
            starting_square = (0, 0)
            first_letter = True
            for i, letter in enumerate(row):

                if letter == '' or i == 10:

                    if i == 10 and letter == '':
                        if len(word) > 1:
                            words.append((word, starting_square, 'row'))
                    elif i == 10 and word != '':
                        if len(word) > 0:
                            word += letter
                            words.append((word, starting_square, 'row'))
                    else:
                        if len(word) > 1:
                            words.append((word, starting_square, 'row'))
                    word = ''
                    first_letter = True

                else:
                    word += letter
                    if first_letter:
                        starting_square = (i, row_num)
                        first_letter = False

        for col_num in range(11):
            col = list(board[col_num, :][::-1])
            word = ''
            starting_square = (0, 0)
            first_letter = True
            for i, letter in enumerate(col):

                if letter == '' or i == 10:

                    if i == 10 and letter == '':
                        if len(word) > 1:
                            words.append((word, starting_square, 'col'))
                    elif i == 10 and word != '':
                        if len(word) > 0:
                            word += letter
                            words.append((word, starting_square, 'col'))
                    else:
                        if len(word) > 1:
                            words.append((word, starting_square, 'col'))
                    word = ''
                    first_letter = True

                else:
                    word += letter
                    if first_letter:
                        starting_square = (col_num, i)
                        first_letter = False

        return words

    def score(self, old_board, new_board):

        old_words = self.extract_word_positions(old_board)
        new_words = self.extract_word_positions(new_board)
        new_words = [word for word in new_words if word not in old_words]

        total_score = 0

        for word in new_words:
            letters, (x, y), rtype = word
            l = len(letters)
            if rtype == 'col':
                powers = list(reversed(list(MyBoard.powers[x, :])))[y:y + l]
            elif rtype == 'row':
                powers = list(MyBoard.powers[x:x + l, y])

            word_score = 0
            multiplier = 1
            for l, p in zip(letters, powers):
                s = points[l]
                if p != '':
                    if p[1] == 'l':
                        if p[0] == 't':
                            s *= 3
                        elif p[0] == 'd':
                            s *= 2
                    elif p[1] == 'w':
                        if p[0] == 't':
                            multiplier *= 3
                        if p[0] == 'd':
                            multiplier *= 2
                word_score += s
            word_score *= multiplier
            total_score += word_score

        return total_score

    def solve(self):

        board = self.Board.letters
        options = []
        counter = 0
        poss = []
        for col_num in range(11):
            col = list(board[col_num, :][::-1])
            if col_num == 0:
                adjacent1 = None
                adjacent2 = list(board[col_num + 1, :][::-1])
            elif col_num == 10:
                adjacent1 = list(board[col_num - 1, :][::-1])
                adjacent2 = None
            else:
                adjacent1 = list(board[col_num - 1, :][::-1])
                adjacent2 = list(board[col_num + 1, :][::-1])
            rows = self.find_words(col, adjacent1, adjacent2)
            for row in rows:
                valid, new_board = self.validate(col_num, row, rtype='col')
                if valid:
                    poss.append(('col', row, col_num, self.score(board, new_board)))

        for row_num in range(11):
            row = list(board[:, row_num])
            if row_num == 0:
                adjacent1 = None
                adjacent2 = list(board[:, row_num + 1])
            elif row_num == 10:
                adjacent1 = list(board[:, row_num - 1])
                adjacent2 = None
            else:
                adjacent1 = list(board[:, row_num - 1])
                adjacent2 = list(board[:, row_num + 1])
            rows = self.find_words(row, adjacent1, adjacent2)
            for row in rows:
                valid, new_board = self.validate(row_num, row, rtype='row')
                if valid:
                    poss.append(('row', row, row_num, self.score(board, new_board)))

        poss = sorted(poss, key=lambda x: -x[3])

        return poss[:10]

    def present_solution(self):

        solutions = self.solve()

        for i, solution in enumerate(reversed(solutions)):

            new_board = self.Board.letters.copy()
            rtype, new_row, index, score = solution
            if rtype == 'row':
                old_row = list(new_board[:, index])
                old_words = self.extract_words(old_row)
                new_words = self.extract_words(new_row)
                new_word = [word for word in new_words if word not in old_words][0]
                new_board[:, index] = new_row
            elif rtype == 'col':
                old_col = list(new_board[index, :][::-1])
                old_words = self.extract_words(old_col)
                new_words = self.extract_words(new_row)
                new_word = [word for word in new_words if word not in old_words][0]
                new_board[index, :] = list(reversed(new_row))
            print('solution {0}: play {1} for {2} points'.format(10 - i, new_word, score))
            Board(letters=new_board).print_letters()


# solver = Solver(MyBoard, 'aaspr')
#
# solver.present_solution()
