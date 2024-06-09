
def get_max_contest_size(difficulties):
    # Sort the difficulties in increasing order
    difficulties.sort()
    # Initialize the maximum contest size and the current contest size
    max_contest_size = 1
    current_contest_size = 1
    # Iterate through the difficulties
    for i in range(1, len(difficulties)):
        # If the current difficulty is less than or equal to twice the previous difficulty, include it in the current contest
        if difficulties[i] <= difficulties[i-1] * 2:
            current_contest_size += 1
        # Otherwise, start a new contest
        else:
            if current_contest_size > max_contest_size:
                max_contest_size = current_contest_size
            current_contest_size = 1
    # Return the maximum contest size
    return max(max_contest_size, current_contest_size)

def main():
    n = int(input())
    difficulties = list(map(int, input().split()))
    print(get_max_contest_size(difficulties))

if __name__ == '__main__':
    main()

