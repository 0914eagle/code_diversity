
def get_input():
    n = int(input())
    attendees = [int(i) for i in input().split()]
    return n, attendees

def get_pairs(n, attendees):
    pairs = []
    for i in range(n):
        for j in range(i+1, n):
            if abs(i-j) == attendees[i] + attendees[j]:
                pairs.append([i, j])
    return pairs

def main():
    n, attendees = get_input()
    pairs = get_pairs(n, attendees)
    print(len(pairs))

if __name__ == '__main__':
    main()

