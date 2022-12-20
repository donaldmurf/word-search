# WORD BANK:
# This program uses a list of words and
# a board of letters to perform a word search.

import numpy as np

# Example of a list of words
word_bank = ['BEACH', 'LIGHTHOUSE', 'JUNGLE', 'FISH',
             'DOCK', 'SAND', 'PALMTREES', 'SHARK',
             'SAILOR', 'SHIP', 'WINDSURFER', 'WHALE']

# Example of a board
search_board = [
    ['H', 'R', 'J', 'M', 'L', 'P', 'F', 'D', 'Y', 'O'],
    ['G', 'O', 'U', 'P', 'I', 'R', 'A', 'T', 'E', 'N'],
    ['I', 'L', 'N', 'J', 'G', 'Z', 'O', 'U', 'J', 'A'],
    ['K', 'I', 'G', 'V', 'H', 'C', 'A', 'E', 'B', 'C'],
    ['P', 'A', 'L', 'M', 'T', 'R', 'E', 'E', 'S', 'L'],
    ['C', 'S', 'E', 'A', 'H', 'S', 'A', 'N', 'D', 'O'],
    ['E', 'Y', 'I', 'Q', 'O', 'H', 'S', 'I', 'F', 'V'],
    ['R', 'E', 'F', 'R', 'U', 'S', 'D', 'N', 'I', 'W'],
    ['D', 'O', 'C', 'K', 'S', 'H', 'A', 'R', 'K', 'I'],
    ['P', 'I', 'H', 'S', 'E', 'L', 'A', 'H', 'W', 'A']
]


# prints list of words with a space between them
def print_word_bank(list_of_words):
    print('Word bank:')

    for words in list_of_words:
        print(words, end=' ')
    print()


# prints the board being used
def print_search_board(board):
    print('\nBoard:')
    for row in board:
        for index_row in row:
            print(index_row, end=' ')
        print()
    print()


# prints info of a all words: first letter, last letter, and length of word
def print_word_list_details(list_of_words):
    for word in range(len(list_of_words)):
        first_letter = list_of_words[word][0]
        last_letter = word_bank[word][list_of_words[word].__len__() - 1]
        length_of_word = len(list_of_words[word])

        print(list_of_words[word])
        print('Length: ' + str(length_of_word))
        print('First letter: ' + first_letter)
        print("Last letter: " + last_letter)


# searches through the whole board for a letter and displays all locations
# of the letter along with how many occurrences produced
def find_letter_location(board, letter):
    matches = 0
    letter = letter.upper()
    print("Testing letter: " + letter + '. Matches:')
    for row in board:
        for index_row in row:
            if index_row == letter:
                matches += 1
                row_location = board.index(row)
                column_location = row.index(letter)
                print('Location: [{0}],[{1}]'.format(row_location, column_location))
    print(matches)


# searches for a word on the board via row and column
# prints row and column of where the first letter starts
# prints if word is left to right, right to left, up to down, or down to up
def solve_game(word, board):
    # transpose columns into rows
    board_transpose = np.transpose(board)
    # track row or column word where word was found
    row_count = 0
    column_count = 0
    # reverse the word to simulate right to left search
    reverse_word = word[::-1]
    # find words in row
    for row in board:
        row_count += 1
        # convert character list into single string
        temp = ""
        temp = temp.join(row)
        # check to see if word match from left to right in string
        if temp.__contains__(word):
            row_hit_LR = row_count
            column_hit = int(temp.find(word))
            print(word + "\nRow: " + str(row_hit_LR) + ' Column: ' + str(column_hit) + " | L to R")
            print()
        # check to see if word matches from right to left in string
        elif temp.__contains__(reverse_word):
            row_hit_RL = row_count
            column_hit_RL = temp.find(reverse_word) + len(reverse_word)
            print(word + "\nRow: " + str(row_hit_RL) + ' Column: ' + str(column_hit_RL) + " | R to L")
            print()
    # find words in column
    for column in board_transpose:
        column_count += 1
        # convert character list into single string
        temp = ""
        temp = temp.join(column)
        if temp.__contains__(word):
            row_hit_UD = temp.find(word) + 1
            column_hit_UD = column_count
            print(word + "\nRow: " + str(row_hit_UD) + ' Column: ' + str(column_hit_UD) + " | U to D")
            print()
        elif temp.__contains__(reverse_word):
            row_hit_DU = temp.find(reverse_word) + len(reverse_word) +1
            column_hit_DU = column_count
            print(word + "\nRow: " + str(row_hit_DU) + ' Column: ' + str(column_hit_DU) + " | D to U")
            print()


if __name__ == '__main__':
    print_word_bank(word_bank)
    print_search_board(search_board)
    for word in range(len(word_bank)):
        solve_game(word_bank[word], search_board)
