
def solve_puzzle(top_row, bottom_row):
    def is_valid_solution(solution):
        for i in range(5):
            for j in range(5):
                if i != j:
                    ratio = solution[i] / solution[j]
                    if top_row[i] != '_' and top_row[j] != '_':
                        if top_row[i] * ratio != top_row[j]:
                            return False
                    if bottom_row[i] != '_' and bottom_row[j] != '_':
                        if bottom_row[i] * ratio != bottom_row[j]:
                            return False
        return True

    def find_solutions():
        solutions = []
        for a in range(1, 201):
            for b in range(1, 201):
                for c in range(1, 201):
                    for d in range(1, 201):
                        for e in range(1, 201):
                            possible_solution = [a, b, c, d, e]
                            if is_valid_solution(possible_solution):
                                solutions.append(possible_solution)
        return solutions

    solutions = find_solutions()
    if not solutions:
        return "many"
    else:
        return len(solutions)

# Input parsing
top_row = list(map(lambda x: int(x) if x != '_' else '_', input().split()))
bottom_row = list(map(lambda x: int(x) if x != '_' else '_', input().split()))

print(solve_puzzle(top_row, bottom_row))
