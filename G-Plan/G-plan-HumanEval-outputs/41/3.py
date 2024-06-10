
def count_char_frequency(s: str) -> dict:
    char_freq = {}
    for char in s:
        char_freq[char] = char_freq.get(char, 0) + 1
    return char_freq

def same_chars(s0: str, s1: str) -> bool:
    freq_s0 = count_char_frequency(s0)
    freq_s1 = count_char_frequency(s1)

    return freq_s0 == freq_s1

s0 = input()
s1 = input()
print(same_chars(s0, s1))
