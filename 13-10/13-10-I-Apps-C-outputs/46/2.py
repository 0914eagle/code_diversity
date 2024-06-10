
def get_starting_sequence(n):
    return list(range(1, n+1))

def get_resulting_sequence(n):
    return list(map(int, input().split()))

def get_proclamations(starting_sequence, resulting_sequence):
    proclamations = []
    for i in range(len(starting_sequence)):
        if starting_sequence[i] != resulting_sequence[i]:
            proclamations.append(resulting_sequence.index(starting_sequence[i]) - i)
    return proclamations

def main():
    n = int(input())
    starting_sequence = get_starting_sequence(n)
    resulting_sequence = get_resulting_sequence(n)
    proclamations = get_proclamations(starting_sequence, resulting_sequence)
    print(*proclamations)

if __name__ == '__main__':
    main()

