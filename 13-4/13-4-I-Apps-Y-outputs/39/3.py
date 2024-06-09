
def get_sequences():
    k = int(input())
    sequences = []
    for i in range(k):
        n = int(input())
        sequence = list(map(int, input().split()))
        sequences.append(sequence)
    return sequences

def find_solution(sequences):
    for i in range(len(sequences)):
        for j in range(i+1, len(sequences)):
            if sequences[i] == sequences[j]:
                continue
            for x in range(len(sequences[i])):
                for y in range(len(sequences[j])):
                    if sequences[i][x] + sequences[j][y] == 0:
                        return i+1, x+1, j+1, y+1
    return -1, -1, -1, -1

def print_solution(solution):
    if solution[0] == -1:
        print("NO")
    else:
        print("YES")
        print(solution[0], solution[1])
        print(solution[2], solution[3])

if __name__ == '__main__':
    sequences = get_sequences()
    solution = find_solution(sequences)
    print_solution(solution)

