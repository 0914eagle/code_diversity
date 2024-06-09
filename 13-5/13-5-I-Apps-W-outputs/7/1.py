
def get_max_strength(n, m, p, c, d, k):
    # Initialize the maximum strength for each day
    max_strength = [0] * d

    # Loop through each day
    for i in range(d):
        # Get the students who left their club on that day
        left_students = [j for j in range(n) if k[i] == j]

        # Get the remaining students
        remaining_students = [j for j in range(n) if j not in left_students]

        # Get the clubs that have remaining students
        remaining_clubs = set([c[j] for j in remaining_students])

        # Get the maximum strength for the day
        max_strength[i] = max([max(p[j] for j in remaining_students if c[j] == club) for club in remaining_clubs])

    return max_strength

def main():
    n, m = map(int, input().split())
    p = list(map(int, input().split()))
    c = list(map(int, input().split()))
    d = int(input())
    k = list(map(int, input().split()))
    max_strength = get_max_strength(n, m, p, c, d, k)
    for i in range(d):
        print(max_strength[i])

if __name__ == '__main__':
    main()

