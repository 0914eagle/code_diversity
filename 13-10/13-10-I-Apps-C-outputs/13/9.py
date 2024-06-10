
import itertools

def get_sum_of_sizes(guest_sizes):
    return sum(guest_sizes)

def get_average_number_of_visitors(guest_sizes, table_length):
    number_of_visitors = 0
    for permutation in itertools.permutations(guest_sizes):
        current_sum = get_sum_of_sizes(permutation)
        if current_sum <= table_length:
            number_of_visitors += 1
    return number_of_visitors / len(guest_sizes)

def main():
    guest_sizes = list(map(int, input().split()))
    table_length = int(input())
    print(get_average_number_of_visitors(guest_sizes, table_length))

if __name__ == '__main__':
    main()

