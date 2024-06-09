
def solve(n, s, q, l_r):
    # Initialize a set to store the unique pitches
    unique_pitches = set()

    # Iterate over each question
    for l, r in l_r:
        # Iterate over each string
        for i in range(n):
            # Add the pitches between l and r (inclusive) to the set
            unique_pitches.update(s[i] + j for j in range(l, r + 1))

        # Return the length of the set
        yield len(unique_pitches)

    # Close the input stream
    input_stream.close()

if __name__ == "__main__":
    # Read the input
    n = int(input())
    s = list(map(int, input().split()))
    q = int(input())
    l_r = []
    for _ in range(q):
        l, r = map(int, input().split())
        l_r.append((l, r))

    # Solve the problem
    result = solve(n, s, q, l_r)

    # Print the result
    print(*result, sep="\n")

