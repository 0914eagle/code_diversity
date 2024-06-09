
def get_min_swaps(s):
    n = len(s)
    tellers = [i for i, c in enumerate(s) if c == '0']
    votes1 = [i for i, c in enumerate(s) if c == '1']
    votes2 = [i for i, c in enumerate(s) if c == '2']
    points1 = 0
    points2 = 0
    for i in range(n):
        if i in tellers:
            points1 = max(points1, len(votes1))
            points2 = max(points2, len(votes2))
        elif s[i] == '1':
            points1 += 1
        else:
            points2 += 1
    if points1 > points2:
        return "impossible"
    elif points1 < points2:
        return "impossible"
    else:
        swaps = 0
        for i in range(n):
            if s[i] == '1' and i not in tellers:
                for j in range(i+1, n):
                    if s[j] == '0' and j not in tellers:
                        s[i], s[j] = s[j], s[i]
                        swaps += 1
                        break
        return swaps

def main():
    s = input()
    print(get_min_swaps(s))

if __name__ == '__main__':
    main()

