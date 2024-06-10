
def digitSum(s: str) -> int:
    def is_uppercase(char):
        return 'A' <= char <= 'Z'

    def calculate_ascii(char):
        return ord(char)

    def filter_and_sum(s):
        total_sum = 0
        for char in s:
            if is_uppercase(char):
                total_sum += calculate_ascii(char)
        return total_sum

    print(filter_and_sum(s))

digitSum(input())
