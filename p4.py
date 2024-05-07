"""
    The code implements the N-Queens problem using backtracking to find a solution where N queens can be
    placed on an NxN chessboard without attacking each other.

    :param arr: The `arr` parameter in the `issafe` and `nQueen` functions represents the chessboard
    configuration where the value `1` indicates the presence of a queen at that position and `0`
    indicates an empty space. The `arr` is a 2D list representing the chessboard
    :param x: In the `issafe` function:
    :param y: The variable `y` in the `issafe` function represents the column index where we are
    checking if it is safe to place a queen at position `(x, y)` on the chessboard. It is used to check
    if there is any queen present in the same column as the current position `(
    :param n: The parameter `n` represents the number of Queens in the n-Queens problem. It is the size
    of the chessboard, which is `n x n` in this case. The goal is to place `n` Queens on an `n x n`
    chessboard in such a way
    :return: The code is implementing the N-Queens problem using backtracking. The `nQueen` function
    recursively tries to place queens on the chessboard represented by a 2D array `arr`. The `issafe`
    function checks if it is safe to place a queen at a given position.
    """


def issafe(arr, x, y, n):
    for row in range(x):
        if arr[row][y] == 1:
            return False

    row = x
    col = y
    while row >= 0 and col >= 0:
        if arr[row][col] == 1:
            return False
        row -= 1
        col -= 1

    row = x
    col = y
    while row >= 0 and col < n:
        if arr[row][col] == 1:
            return False
        row -= 1
        col += 1

    return True


def nQueen(arr, x, n):
    if x >= n:
        return True

    for col in range(n):
        if issafe(arr, x, col, n):
            arr[x][col] = 1
            if nQueen(arr, x + 1, n):
                return True
            arr[x][col] = 0

    return False


def main():
    n = int(input("Enter number of Queens : "))
    arr = [[0] * n for i in range(n)]
    if nQueen(arr, 0, n):
        for i in range(n):
            for j in range(n):
                print(arr[i][j], end=" ")
            print()


if __name__ == "__main__":
    main()
