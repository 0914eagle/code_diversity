
n = int(input())
a = list(map(int, input().split()))

# Use a dictionary to count the frequency of each number in the sequence
freq = {}
for x in a:
    if x in freq:
        freq[x] += 1
    else:
        freq[x] = 1

# Find all x that occur exactly once in the sequence
t = 0
for x in freq:
    if freq[x] == 1:
        t += 1

# Print the result
print(t)
for x in freq:
    if freq[x] == 1:
        print(x, 0)

# Find all x that occur more than once in the sequence
for x in freq:
    if freq[x] > 1:
        # Find the common difference between the positions of x in the sequence
        diff = []
        for i in range(n):
            if a[i] == x:
                diff.append(i - i - 1)
        common_diff = diff[1] - diff[0]

        # Print the result
        print(x, common_diff)

