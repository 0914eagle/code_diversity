
import sys

def solve(n, desks):
    # Initialize the answer and the set of available desks
    answer = 1
    available_desks = set(range(1, 2 * n + 1))

    # Iterate over the desks and the desired desks
    for current_desk, desired_desk in desks:
        # If the current desk is not the desired desk, remove the current desk from the set of available desks
        if current_desk != desired_desk:
            available_desks.remove(current_desk)
        # Add the desired desk to the set of available desks
        available_desks.add(desired_desk)

    # Return the number of possible assignments, modulo 1000000007 = 10^9 + 7
    return answer % 1000000007

if __name__ == '__main__':
    n = int(input())
    desks = []
    for _ in range(n):
        desks.append(tuple(map(int, input().split())))
    print(solve(n, desks))

