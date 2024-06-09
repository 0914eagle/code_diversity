
def get_max_earnings(a):
    # Initialize variables
    n = len(a)
    smashed_gems = set()
    earnings = 0

    # Iterate through the gems and smash those with multiples of x
    for i in range(n):
        if i not in smashed_gems:
            x = i
            while x < n:
                x += i
                if x in smashed_gems:
                    break
                smashed_gems.add(x)

    # Calculate the earnings for each gem that remains unsmashed
    for i in range(n):
        if i not in smashed_gems:
            earnings += a[i]

    return earnings

def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(get_max_earnings(a))

if __name__ == '__main__':
    main()

