
def digitSum(s: str) -> int:
    total_sum = 0
    for char in s:
        if char.isupper():
            total_sum += ord(char)
    return total_sum

# Test cases
print(digitSum(''))  # 0
print(digitSum('abAB'))  # 131
print(digitSum('abcCd'))  # 67
print(digitSum('helloE'))  # 69
print(digitSum('woArBld'))  # 131
print(digitSum('aAaaaXa'))  # 153
