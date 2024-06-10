
def same_chars(s0: str, s1: str) -> bool:
    def count_chars(s: str) -> dict:
        char_count = {}
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1
        return char_count

    def compare_char_counts(count1: dict, count2: dict) -> bool:
        return count1 == count2

    char_count_s0 = count_chars(s0)
    char_count_s1 = count_chars(s1)

    return compare_char_counts(char_count_s0, char_count_s1)

s0, s1 = input().strip().split()
print(same_chars(s0, s1))
