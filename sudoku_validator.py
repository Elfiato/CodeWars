'''
https://www.codewars.com/kata/529bf0e9bdf7657179000008
'''


def valid_solution(board):
    column = [[] for i in range(1, 10)]
    block = [[] for i in range(1, 10)]

    if len(board) != 9:
        return False

    for i in range(len(board)):
        if len(board[i]) != 9:
            return False
        for j in range(len(board[i])):
            k = board[i].count(board[i][j])
            if board[i][j] not in range(1, 10) or board[i].count(board[i][j]) != 1:
                return False
            column[j].append(board[i][j])
        if i < 3:
            block[0] += board[i][:3]
            block[1] += board[i][3:6]
            block[2] += board[i][6:]
        if 3 <= i < 6:
            block[3] += board[i][:3]
            block[4] += board[i][3:6]
            block[5] += board[i][6:]
        if i >= 6:
            block[6] += board[i][:3]
            block[7] += board[i][3:6]
            block[8] += board[i][6:]

    for i in range(len(column)):
        for j in range(len(column[i])):
            if column[i][j] not in range(1, 10) or column[i].count(column[i][j]) != 1:
                return False
            if block[i][j] not in range(1, 10) or block[i].count(block[i][j]) != 1:
                return False

    return True


print(valid_solution([[5, 3, 4, 6, 7, 8, 9, 1, 2],
                      [6, 7, 2, 1, 9, 5, 3, 4, 8],
                      [1, 9, 8, 3, 4, 2, 5, 6, 7],
                      [8, 5, 9, 7, 6, 1, 4, 2, 3],
                      [4, 2, 6, 8, 5, 3, 7, 9, 1],
                      [7, 1, 3, 9, 2, 4, 8, 5, 6],
                      [9, 6, 1, 5, 3, 7, 2, 8, 4],
                      [2, 8, 7, 4, 1, 9, 6, 3, 5],
                      [3, 4, 5, 2, 8, 6, 1, 7, 9]]))

print(valid_solution([[5, 5, 4, 6, 7, 5, 9, 1, 2],
                      [6, 7, 2, 1, 9, 5, 3, 4, 8],
                      [1, 9, 8, 3, 4, 2, 5, 6, 7],
                      [8, 5, 9, 7, 6, 1, 4, 2, 3],
                      [4, 2, 6, 8, 5, 3, 7, 9, 1],
                      [7, 1, 3, 9, 2, 4, 8, 5, 6],
                      [9, 6, 1, 5, 3, 7, 2, 8, 4],
                      [2, 8, 7, 4, 1, 9, 6, 3, 5],
                      [3, 4, 5, 2, 8, 6, 1, 7, 9]]))
