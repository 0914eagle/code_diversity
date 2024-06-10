
def is_beautiful_sequence_possible(k, q):
    char_count = {}
    for char in q:
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1

    if len(char_count) < k:
        return False

    return True

def generate_beautiful_sequence(k, q):
    if not is_beautiful_sequence_possible(k, q):
        print("NO")
        return

    char_count = {}
    result = []
    current_string = ""
    for char in q:
        if char not in char_count:
            char_count[char] = 1
            if current_string:
                result.append(current_string)
                current_string = ""
        else:
            char_count[char] += 1

        current_string += char

    result.append(current_string)

    print("YES")
    for string in result:
        print(string)

if __name__ == "__main__":
    k = int(input())
    q = input().strip()
    generate_beautiful_sequence(k, q)
