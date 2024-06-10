
def get_maximum_students(n, k, a):
    # Find the maximum number of students who can get their favorite drink
    maximum = 0
    for i in range(1, k+1):
        # Count the number of students who prefer drink i
        count = 0
        for j in range(n):
            if a[j] == i:
                count += 1
        # Update the maximum number of students
        maximum = max(maximum, count)
    return maximum

def get_minimum_sets(n, k, a):
    # Find the minimum number of sets needed to give each student a drink
    sets = 0
    for i in range(1, k+1):
        # Count the number of students who prefer drink i
        count = 0
        for j in range(n):
            if a[j] == i:
                count += 1
        # Update the number of sets needed
        sets += count // 2 + count % 2
    return sets

def get_portions(n, k, a):
    # Find the number of portions needed to give each student a drink
    portions = 0
    for i in range(1, k+1):
        # Count the number of students who prefer drink i
        count = 0
        for j in range(n):
            if a[j] == i:
                count += 1
        # Update the number of portions needed
        portions += count
    return portions

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    maximum = get_maximum_students(n, k, a)
    minimum = get_minimum_sets(n, k, a)
    portions = get_portions(n, k, a)
    print(maximum)
    print(minimum)
    print(portions)

if __name__ == '__main__':
    main()

