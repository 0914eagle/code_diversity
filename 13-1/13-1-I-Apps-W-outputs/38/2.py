
n = int(input())
a = list(map(int, input().split()))

# Use a dictionary to count the frequency of each number in the sequence
freq = {}
for num in a:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

# Find all x that occur exactly twice in the sequence
x_list = []
for x in freq:
    if freq[x] == 2:
        x_list.append(x)

# Sort the list of x in increasing order
x_list.sort()

# Print the number of valid x
print(len(x_list))

# Print the pairs of x and p_x
for x in x_list:
    print(x, freq[x] - 1)

