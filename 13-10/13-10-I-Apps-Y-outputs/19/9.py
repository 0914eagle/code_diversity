
def get_middle_string(s, t, k):
    strings = []
    for i in range(ord('a'), ord('a') + k):
        for j in range(ord('a'), ord('a') + k):
            if i != j and chr(i) != s and chr(j) != t:
                strings.append(chr(i) + chr(j))
    strings.sort()
    return strings[len(strings) // 2]

def get_input():
    k = int(input())
    s = input()
    t = input()
    return k, s, t

if __name__ == '__main__':
    k, s, t = get_input()
    print(get_middle_string(s, t, k))

