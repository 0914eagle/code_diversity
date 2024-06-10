
def digitSum(s: str) -> int:
    def is_upper(char):
        return 'A' <= char <= 'Z'

    def ascii_value(char):
        return ord(char)

    sum_upper_ascii = sum(ascii_value(char) for char in s if is_upper(char))
    return sum_upper_ascii

s = input()
print(digitSum(s))
