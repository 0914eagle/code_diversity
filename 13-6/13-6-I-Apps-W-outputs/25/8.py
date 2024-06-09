
def get_maximum_danger(n, m, reactions):
    # Initialize the danger array with 1s
    danger = [1] * (n + 1)

    # Iterate over the reactions and update the danger array
    for x, y in reactions:
        danger[x] *= 2
        danger[y] *= 2

    # Return the maximum danger
    return max(danger)

def main():
    n, m = map(int, input().split())
    reactions = []
    for _ in range(m):
        x, y = map(int, input().split())
        reactions.append((x, y))
    print(get_maximum_danger(n, m, reactions))

if __name__ == '__main__':
    main()

