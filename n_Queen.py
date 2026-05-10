n = int(input("Enter value of N: "))

board = [[0]*n for _ in range(n)]

def safe(r, c):

    for i in range(c):
        if board[r][i] == 1:
            return False

    i, j = r, c
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    i, j = r, c
    while i < n and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True

def solve(c):

    if c >= n:
        return True

    for i in range(n):

        if safe(i, c):

            board[i][c] = 1

            if solve(c + 1):
                return True

            board[i][c] = 0

    return False

if solve(0):

    print("Solution:")

    for i in board:
        print(*i)

else:
    print("No Solution")

#----------------------OUTPUT----------------------
Enter value of N: 4
Solution:
0 1 0 0
0 0 0 1
1 0 0 0
0 0 1 0

