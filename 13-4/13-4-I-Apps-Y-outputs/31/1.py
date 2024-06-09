
def is_valid_solution(queens):
    # Check if there are any two queens in the same row, column or diagonal
    for i in range(len(queens)):
        for j in range(i+1, len(queens)):
            if queens[i][0] == queens[j][0] or queens[i][1] == queens[j][1] or abs(queens[i][0] - queens[j][0]) == abs(queens[i][1] - queens[j][1]):
                return "INCORRECT"
    return "CORRECT"

