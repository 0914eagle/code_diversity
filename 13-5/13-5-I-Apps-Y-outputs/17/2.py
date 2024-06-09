
def get_min_mp(N, A, B, C, lengths):
    # Initialize the minimum MP needed to achieve the objective
    min_mp = 0

    # Initialize the current length of the bamboos
    current_lengths = lengths.copy()

    # While there are still bamboos to be processed
    while current_lengths:
        # Find the longest bamboo that is less than or equal to A
        longest_less_than_a = -1
        for i in range(len(current_lengths)):
            if current_lengths[i] <= A and current_lengths[i] > longest_less_than_a:
                longest_less_than_a = current_lengths[i]

        # If there is no bamboo less than or equal to A, use extension magic
        if longest_less_than_a == -1:
            # Find the shortest bamboo
            shortest = min(current_lengths)

            # Use extension magic on the shortest bamboo
            current_lengths[current_lengths.index(shortest)] += 1
            min_mp += 1

        # If there is a bamboo less than or equal to A, use composition magic
        else:
            # Find the second longest bamboo that is less than or equal to B
            second_longest_less_than_b = -1
            for i in range(len(current_lengths)):
                if current_lengths[i] <= B and current_lengths[i] > second_longest_less_than_b:
                    second_longest_less_than_b = current_lengths[i]

            # If there is no bamboo less than or equal to B, use shortening magic
            if second_longest_less_than_b == -1:
                # Find the longest bamboo that is greater than or equal to C
                longest_greater_than_c = -1
                for i in range(len(current_lengths)):
                    if current_lengths[i] >= C and current_lengths[i] > longest_greater_than_c:
                        longest_greater_than_c = current_lengths[i]

                # If there is no bamboo greater than or equal to C, use extension magic
                if longest_greater_than_c == -1:
                    # Find the shortest bamboo
                    shortest = min(current_lengths)

                    # Use extension magic on the shortest bamboo
                    current_lengths[current_lengths.index(shortest)] += 1
                    min_mp += 1

                # If there is a bamboo greater than or equal to C, use composition magic
                else:
                    # Use composition magic on the longest bamboo and the second longest bamboo
                    current_lengths[current_lengths.index(longest_greater_than_c)] += current_lengths[current_lengths.index(second_longest_less_than_b)]
                    current_lengths.pop(current_lengths.index(second_longest_less_than_b))
                    min_mp += 10

            # If there is a bamboo less than or equal to B, use composition magic
            else:
                # Use composition magic on the longest bamboo and the second longest bamboo
                current_lengths[current_lengths.index(longest_less_than_a)] += current_lengths[current_lengths.index(second_longest_less_than_b)]
                current_lengths.pop(current_lengths.index(second_longest_less_than_b))
                min_mp += 10

    return min_mp

def main():
    N, A, B, C = map(int, input().split())
    lengths = list(map(int, input().split()))
    print(get_min_mp(N, A, B, C, lengths))

if __name__ == '__main__':
    main()

