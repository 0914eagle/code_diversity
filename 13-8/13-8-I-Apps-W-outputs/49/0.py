
def get_maximum_students_with_favorite_drink(n, k, a):
    # Initialize variables
    max_students = 0
    current_students = 0
    current_sets = 0
    sets_used = []

    # Iterate through all possible sets
    for i in range(1, k + 1):
        for j in range(1, k + 1):
            if i != j:
                # Check if the current set is already used
                if (i, j) not in sets_used:
                    # Add the current set to the used sets
                    sets_used.append((i, j))
                    current_sets += 1

                    # Check if the current set gives a student his favorite drink
                    for student in a:
                        if student == i or student == j:
                            current_students += 1

                    # Check if the current configuration is the maximum
                    if current_students > max_students:
                        max_students = current_students

                    # Reset the current configuration
                    current_students = 0
                    current_sets = 0
                    sets_used = []

    return max_students

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    print(get_maximum_students_with_favorite_drink(n, k, a))

if __name__ == '__main__':
    main()

