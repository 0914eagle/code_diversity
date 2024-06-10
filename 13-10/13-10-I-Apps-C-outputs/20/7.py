
def get_number_of_appearances(board, query):
    appearances = 0
    for row in board:
        for num in row:
            if query[0] <= num <= query[1]:
                appearances += 1
    return appearances

def get_board(rows, cols):
    board = []
    for i in range(rows):
        row = [i]
        for j in range(1, cols):
            row.append(row[j-1] + int(str(row[j-1])[::-1]))
        board.append(row)
    return board

def main():
    rows, cols = map(int, input().split())
    board = get_board(rows, cols)
    queries = int(input())
    for i in range(queries):
        query = list(map(int, input().split()))
        print(get_number_of_appearances(board, query))

if __name__ == '__main__':
    main()

