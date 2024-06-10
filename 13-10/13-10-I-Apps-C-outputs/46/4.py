
def get_proclamations(starting_sequence, resulting_sequence):
    proclamations = []
    current_sequence = starting_sequence
    while current_sequence != resulting_sequence:
        for i in range(len(current_sequence)):
            if current_sequence[i] != resulting_sequence[i]:
                break
        proclamation = resulting_sequence[i]
        proclamations.append(proclamation)
        current_sequence = list(map(lambda x: x+1 if x < proclamation else x-1 if x > proclamation else x, current_sequence))
    return proclamations

def main():
    num_frogs = int(input())
    starting_sequence = list(map(int, input().split()))
    resulting_sequence = list(map(int, input().split()))
    proclamations = get_proclamations(starting_sequence, resulting_sequence)
    print(*proclamations, sep='\n')

if __name__ == '__main__':
    main()

