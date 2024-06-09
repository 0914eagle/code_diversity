
n = int(input())
s = input()

# Function to check if a string is a telephone number
def is_telephone_number(s):
    if len(s) != 11 or s[0] != '8':
        return False
    for digit in s:
        if not digit.isdigit():
            return False
    return True

# Count the occurrences of each digit in the input string
digit_count = {}
for digit in s:
    if digit in digit_count:
        digit_count[digit] += 1
    else:
        digit_count[digit] = 1

# Check if Vasya has a winning strategy
if digit_count.get('8', 0) >= (11 - n) // 2 + 1:
    print("YES")
else:
    print("NO")
