
def input_data():
    n = int(input())
    vertical_spec = [tuple(map(int, input().split())) for _ in range(n)]
    horizontal_spec = [tuple(map(int, input().split())) for _ in range(n)]
    return n, vertical_spec, horizontal_spec

def find_solution(n, vertical_spec, horizontal_spec):
    # Initialize the solution matrix with 0s
    solution = [[0] * (n+1) for _ in range(n)]

    # Fill in the vertical bars
    for i in range(n):
        for j in range(len(vertical_spec[i])):
            # Check if the current position is already marked or not
            if solution[i][j] == 0:
                # Mark the current position and update the solution matrix
                solution[i][j] = 1
                # Update the vertical specification for the current row
                vertical_spec[i] = vertical_spec[i][:j] + (vertical_spec[i][j] - 1,) + vertical_spec[i][j+1:]
                # Break the loop since we have found a solution
                break

    # Fill in the horizontal bars
    for j in range(n):
        for i in range(len(horizontal_spec[j])):
            # Check if the current position is already marked or not
            if solution[i][j] == 0:
                # Mark the current position and update the solution matrix
                solution[i][j] = 1
                # Update the horizontal specification for the current column
                horizontal_spec[j] = horizontal_spec[j][:i] + (horizontal_spec[j][i] - 1,) + horizontal_spec[j][i+1:]
                # Break the loop since we have found a solution
                break

    return solution

def output_solution(solution):
    # Output the vertical bars
    for i in range(len(solution)):
        print("".join(map(str, solution[i])))

    # Output the horizontal bars
    for j in range(len(solution[0])):
        print("".join(map(str, [solution[i][j] for i in range(len(solution))])))

if __name__ == '__main__':
    n, vertical_spec, horizontal_spec = input_data()
    solution = find_solution(n, vertical_spec, horizontal_spec)
    output_solution(solution)

