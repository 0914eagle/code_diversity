
def get_maximum_strength(n, m, p, c, d, k):
    # Initialize the maximum strength for each day
    max_strength = [0] * d

    # Loop through each day
    for i in range(d):
        # Get the students who left their club on the current day
        left_students = [j for j in range(n) if k[i] == j]

        # Get the students who are still in their clubs
        remaining_students = [j for j in range(n) if j not in left_students]

        # Get the clubs that still have members
        remaining_clubs = [j for j in range(m) if any(c[i] == j for i in remaining_students)]

        # Get the maximum possible strength for the current day
        max_strength[i] = max(p[i] for i in remaining_students if c[i] in remaining_clubs)

    return max_strength

def main():
    n, m = map(int, input().split())
    p = list(map(int, input().split()))
    c = list(map(int, input().split()))
    d = int(input())
    k = list(map(int, input().split()))
    max_strength = get_maximum_strength(n, m, p, c, d, k)
    for i in range(d):
        print(max_strength[i])

if __name__ == '__main__':
    main()

