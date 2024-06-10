
def is_beautiful_sequence_possible(k, q):
    char_count = {}
    for char in q:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    if any(count > 1 for count in char_count.values()):
        return False
    return True

def generate_beautiful_sequence(k, q):
    if not is_beautiful_sequence_possible(k, q):
        print("NO")
        return

    char_count = {}
    sequence = []
    current_string = ""
    for char in q:
        if char not in char_count:
            char_count[char] = 1
            if current_string:
                sequence.append(current_string)
                current_string = ""
        else:
            char_count[char] += 1

        current_string += char

    sequence.append(current_string)
    print("YES")
    for s in sequence:
        print(s)

if __name__ == "__main__":
    k = int(input())
    q = input().strip()
    generate_beautiful_sequence(k, q)
