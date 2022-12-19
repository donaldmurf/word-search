# WORD BANK:
# This program uses a list of words and
# a board of letters to perform a word search.

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


# prints info of a all words: first letter, last letter, and lengt of word
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


# searches for a word on the board
def search_word(word, board):
    first_letter = word[0]
    last_letter = word[len(word) - 1]
    length_of_word = len(word)

    # start at the first or last letter

    # check to see if first or last letter
    # exists.

    # check all letters in direction moved
    # compare and see if match

    find_letter_location(board, first_letter)
    find_letter_location(board, last_letter)


if __name__ == '__main__':
    # print_word_bank(word_bank)
    # print_search_board(search_board)
    # print_word_details(word_bank)
    # find_letter_location(search_board, 'a')
    for index in word_bank:
        search_word(index, search_board)
