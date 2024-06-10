
def get_possible_strings(a00, a01, a10, a11):
    possible_strings = []
    for i in range(a00 + 1):
        for j in range(a01 + 1):
            for k in range(a10 + 1):
                for l in range(a11 + 1):
                    if i + j + k + l == a00 + a01 + a10 + a11:
                        possible_strings.append("0" * i + "1" * j + "0" * k + "1" * l)
    return possible_strings

def find_matching_string(a00, a01, a10, a11):
    possible_strings = get_possible_strings(a00, a01, a10, a11)
    for string in possible_strings:
        substring_count = {}
        for i in range(len(string) - 1):
            substring = string[i:i+2]
            if substring not in substring_count:
                substring_count[substring] = 0
            substring_count[substring] += 1
        if substring_count.get("00", 0) == a00 and substring_count.get("01", 0) == a01 and substring_count.get("10", 0) == a10 and substring_count.get("11", 0) == a11:
            return string
    return "Impossible"

if __name__ == '__main__':
    a00, a01, a10, a11 = map(int, input().split())
    print(find_matching_string(a00, a01, a10, a11))

