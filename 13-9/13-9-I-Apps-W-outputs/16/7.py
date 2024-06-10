
def check_plan(plan, n, m):
    # Initialize a 2D array to store the color of each pixel
    field = [[0] * m for _ in range(n)]

    # Iterate through each move in the plan
    for i, j in plan:
        # If the pixel is not already black, color it black
        if field[i - 1][j - 1] == 0:
            field[i - 1][j - 1] = 1

    # Check if a 2x2 square consisting of black pixels is formed
    for i in range(n - 1):
        for j in range(m - 1):
            if field[i][j] == 1 and field[i + 1][j] == 1 and field[i][j + 1] == 1 and field[i + 1][j + 1] == 1:
                return True
    return False

def find_losing_move(plan, n, m):
    # Initialize a 2D array to store the color of each pixel
    field = [[0] * m for _ in range(n)]

    # Iterate through each move in the plan
    for i, j in plan:
        # If the pixel is not already black, color it black
        if field[i - 1][j - 1] == 0:
            field[i - 1][j - 1] = 1

        # Check if a 2x2 square consisting of black pixels is formed
        for k in range(i, n):
            for l in range(j, m):
                if field[k][l] == 1 and field[k + 1][l] == 1 and field[k][l + 1] == 1 and field[k + 1][l + 1] == 1:
                    return i * m + j + 1
    return 0

if __name__ == '__main__':
    n, m, k = map(int, input().split())
    plan = []
    for _ in range(k):
        i, j = map(int, input().split())
        plan.append((i, j))
    if check_plan(plan, n, m):
        print(find_losing_move(plan, n, m))
    else:
        print(0)

