
n = int(input())
s = input()

# Count the number of occurrences of each digit in the string
digit_count = [0] * 10
for digit in s:
    digit_count[int(digit)] += 1

# Check if Vasya can win by ensuring there are enough digits to form a telephone number
if digit_count[8] >= 1 and n - 1 >= 11:
    print("YES")
else:
    print("NO")
