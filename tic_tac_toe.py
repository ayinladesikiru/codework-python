# print("""
#         *************************************************
#                         Lets Play Tic Tac Toe
#         *************************************************
#
#             position1       position2       position3
#
#             position1       position2       position3
#
#             position1       position2       position3
#         *************************************************
#
#         """)
#
# x = 0
#
# position1 = input("Enter X or O")


def print_board(boards):

    for board in boards:
        for cell in board:
            print(cell, end=" ")
        print()


def printing_board(boards):

    for board in boards:

        print(" ".join(board))




boards = [['*', '*', '*'],
          ['*', '*', '*'],
          ['*', '*', '*']]
printing_board(boards)
print(boards[0][0])

boardings = ['*'] * 9

print(boardings)

for i in range(len(boardings)):
    if i != 0 and i % 3 == 0:
        print()
    print(boardings[i], end=" ")

pos = 5
print(boardings[pos - 1])