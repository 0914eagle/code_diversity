
def get_maximum_students_with_favorite_drink(n, k, a):
    # Initialize variables
    max_students = 0
    current_students = 0
    current_sets = 0
    sets_needed = int(n / 2) + 1
    drinks_needed = [0] * (k + 1)
    drinks_given = [0] * (k + 1)

    # Loop through each student
    for i in range(n):
        # If the current student has a favorite drink that is not yet given, give it to them
        if drinks_needed[a[i]] > 0 and drinks_given[a[i]] == 0:
            drinks_given[a[i]] += 1
            current_students += 1
        # If the current student does not have a favorite drink or if all favorite drinks are given, give them a random drink
        else:
            current_students += 1

        # If the current student is the last student or if the current set is full, move to the next set
        if i == n - 1 or current_students == 2:
            current_students = 0
            current_sets += 1

        # If the current set is full, give the remaining students random drinks
        if current_students == 2:
            for j in range(k + 1):
                if drinks_needed[j] > 0 and drinks_given[j] == 0:
                    drinks_given[j] += 1
                    current_students -= 1

        # Update the maximum number of students with a favorite drink
        if current_sets == sets_needed:
            max_students = max(max_students, current_students)

    return max_students

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    print(get_maximum_students_with_favorite_drink(n, k, a))

if __name__ == '__main__':
    main()

