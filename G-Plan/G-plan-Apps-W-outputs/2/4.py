
def is_beautiful_sequence_possible(k, q):
    char_count = {}
    for char in q:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    if len(char_count) < k:
        return False
    
    return True

def generate_beautiful_sequence(k, q):
    if not is_beautiful_sequence_possible(k, q):
        print("NO")
        return
    
    print("YES")
    char_count = {}
    current_string = ""
    for char in q:
        if char not in char_count or char_count[char] == 0:
            if current_string:
                print(current_string)
            current_string = char
            char_count[char] = 1
        else:
            current_string += char
            char_count[char] += 1
    
    print(current_string)

if __name__ == "__main__":
    k = int(input())
    q = input().strip()
    generate_beautiful_sequence(k, q)
