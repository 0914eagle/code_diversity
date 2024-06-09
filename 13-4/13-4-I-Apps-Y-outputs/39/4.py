
def read_input():
    k = int(input())
    sequences = []
    for i in range(k):
        n = int(input())
        sequence = list(map(int, input().split()))
        sequences.append(sequence)
    return k, sequences

def solve(k, sequences):
    for i in range(k):
        for j in range(i+1, k):
            if sequences[i][0] + sequences[j][0] == 0:
                return "YES", i+1, 1, j+1, 1
            for x in range(1, len(sequences[i])):
                if sequences[i][x] + sequences[j][0] == 0:
                    return "YES", i+1, x+1, j+1, 1
                for y in range(1, len(sequences[j])):
                    if sequences[i][x] + sequences[j][y] == 0:
                        return "YES", i+1, x+1, j+1, y+1
    return "NO"

def main():
    k, sequences = read_input()
    result = solve(k, sequences)
    print(result)

if __name__ == '__main__':
    main()

