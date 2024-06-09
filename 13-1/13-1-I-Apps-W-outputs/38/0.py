
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
twice = []
for x in freq:
    if freq[x] == 2:
        twice.append(x)

# Find all x that occur exactly thrice in the sequence
thrice = []
for x in freq:
    if freq[x] == 3:
        thrice.append(x)

# Find all x that occur exactly four times in the sequence
four = []
for x in freq:
    if freq[x] == 4:
        four.append(x)

# Find all x that occur exactly five times in the sequence
five = []
for x in freq:
    if freq[x] == 5:
        five.append(x)

# Find all x that occur exactly six times in the sequence
six = []
for x in freq:
    if freq[x] == 6:
        six.append(x)

# Find all x that occur exactly seven times in the sequence
seven = []
for x in freq:
    if freq[x] == 7:
        seven.append(x)

# Find all x that occur exactly eight times in the sequence
eight = []
for x in freq:
    if freq[x] == 8:
        eight.append(x)

# Find all x that occur exactly nine times in the sequence
nine = []
for x in freq:
    if freq[x] == 9:
        nine.append(x)

# Find all x that occur exactly ten times in the sequence
ten = []
for x in freq:
    if freq[x] == 10:
        ten.append(x)

# Print the number of valid x
print(len(twice) + len(thrice) + len(four) + len(five) + len(six) + len(seven) + len(eight) + len(nine) + len(ten))

# Print the valid x and their common differences
for x in twice:
    print(x, 0)
for x in thrice:
    print(x, 0)
for x in four:
    print(x, 0)
for x in five:
    print(x, 0)
for x in six:
    print(x, 0)
for x in seven:
    print(x, 0)
for x in eight:
    print(x, 0)
for x in nine:
    print(x, 0)
for x in ten:
    print(x, 0)

