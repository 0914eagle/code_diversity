
def digitSum(s: str) -> int:
    def is_uppercase(char: str) -> bool:
        return char.isupper()

    def ascii_value(char: str) -> int:
        return ord(char)

    def sum_uppercase_ascii(input_string: str) -> int:
        return sum(ascii_value(char) for char in input_string if is_uppercase(char))

    return sum_uppercase_ascii(s)

# Read input
input_string = input().strip()

# Print output
print(digitSum(input_string))
