
def get_median(s, t, k):
    # Create a list of all strings between s and t
    strings = []
    for i in range(ord('a'), ord('a') + k):
        for j in range(ord('a') + 1, ord('a') + k + 1):
            if i < j:
                strings.append(chr(i) + chr(j))
    # Find the median of the list
    median = strings[len(strings) // 2]
    return median

def main():
    k = int(input())
    s = input()
    t = input()
    print(get_median(s, t, k))

if __name__ == '__main__':
    main()

