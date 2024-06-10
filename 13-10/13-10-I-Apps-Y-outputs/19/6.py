
def get_strings_between(s, t, k):
    strings = []
    for i in range(ord('a'), ord('a') + k):
        for j in range(ord('a'), ord('a') + k):
            if s <= chr(i) + chr(j) <= t:
                strings.append(chr(i) + chr(j))
    return strings

def get_median(strings):
    middle_index = len(strings) // 2
    if len(strings) % 2 == 0:
        return strings[middle_index - 1]
    else:
        return strings[middle_index]

if __name__ == '__main__':
    k = int(input())
    s = input()
    t = input()
    strings = get_strings_between(s, t, k)
    print(get_median(strings))

