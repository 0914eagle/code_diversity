
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
        # If the current student has a favorite drink that is already given, give them the other drink from the set
        elif drinks_needed[a[i]] > 0 and drinks_given[a[i]] == 1:
            drinks_given[a[i]] += 1
            current_students += 1
        # If the current student does not have a favorite drink, give them the drink that is needed the most
        else:
            for j in range(1, k + 1):
                if drinks_needed[j] > 0 and drinks_given[j] == 0:
                    drinks_given[j] += 1
                    current_students += 1
                    break

        # If the current student is the last student, check if they got their favorite drink
        if i == n - 1:
            if current_students > max_students:
                max_students = current_students

    return max_students

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    print(get_maximum_students_with_favorite_drink(n, k, a))

if __name__ == '__main__':
    main()

