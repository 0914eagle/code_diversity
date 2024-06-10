
def digitSum(s: str) -> int:
    sum_ascii = 0
    for char in s:
        if char.isupper():
            sum_ascii += ord(char)
    return sum_ascii

input_str = input().strip()
print(digitSum(input_str))
