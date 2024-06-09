
def get_input():
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
                return i+1, j+1, 1, 1
            for x in range(1, len(sequences[i])):
                for y in range(1, len(sequences[j])):
                    if sequences[i][x] + sequences[j][y] == 0:
                        return i+1, j+1, x+1, y+1
    return -1, -1, -1, -1

def main():
    k, sequences = get_input()
    i, j, x, y = solve(k, sequences)
    if i == -1:
        print("NO")
    else:
        print("YES")
        print(i, x)
        print(j, y)

if __name__ == '__main__':
    main()

