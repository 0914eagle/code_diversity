
import sys
import math

def get_input():
    R, C = map(int, input().split())
    board = [input() for _ in range(R)]
    return R, C, board

def get_distance(r1, c1, r2, c2):
    return abs(r1 - r2) + abs(c1 - c2)

def get_spread(board, piece):
    spread = 0
    for r in range(len(board)):
        for c in range(len(board[0])):
            if board[r][c] == piece:
                for nr in range(len(board)):
                    for nc in range(len(board[0])):
                        if board[nr][nc] == piece:
                            spread += get_distance(r, c, nr, nc)
    return spread

def main():
    R, C, board = get_input()
    mirko_spread = get_spread(board, 'M')
    slavko_spread = get_spread(board, 'S')
    print(mirko_spread, slavko_spread)

if __name__ == '__main__':
    main()

