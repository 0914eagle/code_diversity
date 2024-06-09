
def f1(n, pebbles):
    # f1(n, pebbles) returns the most distant pebble that can be reached by a sequence of jumps
    # from the first pebble to the last pebble, where each jump is only possible if the sum of
    # the number of spots on the current pebble and the next pebble is equal to the distance
    # between the two pebbles.
    # n: integer, the number of pebbles
    # pebbles: list of integers, the number of spots on each pebble

    # Initialize the maximum distance as 0
    max_distance = 0

    # Initialize the current pebble as the first pebble
    current_pebble = 0

    # Loop through each pebble
    for i in range(n):
        # If the sum of the number of spots on the current pebble and the next pebble is equal to the distance between the two pebbles
        if pebbles[current_pebble] + pebbles[i] == i - current_pebble:
            # Update the maximum distance
            max_distance = max(max_distance, i - current_pebble)
            # Update the current pebble
            current_pebble = i

    # Return the maximum distance
    return max_distance

def f2(n, pebbles):
    # f2(n, pebbles) returns the most distant pebble that can be reached by a sequence of jumps
    # from the first pebble to the last pebble, where each jump is only possible if the sum of
    # the number of spots on the current pebble and the next pebble is equal to the distance
    # between the two pebbles, and the number of spots on each pebble is at most 10^9.
    # n: integer, the number of pebbles
    # pebbles: list of integers, the number of spots on each pebble

    # Initialize the maximum distance as 0
    max_distance = 0

    # Initialize the current pebble as the first pebble
    current_pebble = 0

    # Loop through each pebble
    for i in range(n):
        # If the sum of the number of spots on the current pebble and the next pebble is equal to the distance between the two pebbles and the number of spots on the current pebble is at most 10^9
        if pebbles[current_pebble] + pebbles[i] == i - current_pebble and pebbles[current_pebble] <= 10**9:
            # Update the maximum distance
            max_distance = max(max_distance, i - current_pebble)
            # Update the current pebble
            current_pebble = i

    # Return the maximum distance
    return max_distance

if __name__ == '__main__':
    n = int(input())
    pebbles = list(map(int, input().split()))
    print(f2(n, pebbles))

