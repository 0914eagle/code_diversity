
def get_max_students_with_favorite_drink(n, k, a):
    # Find the maximum number of students who can get their favorite drink
    max_students = 0
    for i in range(1, k+1):
        # Count the number of students who prefer drink i
        count = 0
        for j in range(n):
            if a[j] == i:
                count += 1
        # Update the maximum number of students who can get their favorite drink
        if count > max_students:
            max_students = count
    return max_students

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    print(get_max_students_with_favorite_drink(n, k, a))

if __name__ == '__main__':
    main()

