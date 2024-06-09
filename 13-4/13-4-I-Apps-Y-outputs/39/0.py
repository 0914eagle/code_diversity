
def read_input():
    k = int(input())
    sequences = []
    for i in range(k):
        n = int(input())
        sequence = list(map(int, input().split()))
        sequences.append(sequence)
    return k, sequences

def find_solution(sequences):
    for i in range(len(sequences)):
        for j in range(i+1, len(sequences)):
            if sequences[i][0] + sequences[j][0] == sequences[i][-1] + sequences[j][-1]:
                return i+1, 1, j+1, 1
    return -1, -1, -1, -1

def print_output(solution):
    if solution[0] == -1:
        print("NO")
    else:
        print("YES")
        print(solution[0], solution[1])
        print(solution[2], solution[3])

if __name__ == '__main__':
    k, sequences = read_input()
    solution = find_solution(sequences)
    print_output(solution)

