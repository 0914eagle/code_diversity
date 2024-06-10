
def get_maximum_number_of_students_with_favorite_drink(n, k, a):
    # Initialize variables
    max_number_of_students = 0
    sets_needed = ceil(n / 2)
    drink_types = [0] * (k + 1)

    # Populate the drink types
    for i in range(n):
        drink_types[a[i]] += 1

    # Iterate through all possible combinations of drink types
    for i in range(1, k + 1):
        for j in range(i, k + 1):
            # Check if the current combination of drink types is valid
            if drink_types[i] > 0 and drink_types[j] > 0:
                # Calculate the number of students who will get their favorite drink with the current combination
                number_of_students = 0
                for k in range(n):
                    if a[k] == i or a[k] == j:
                        number_of_students += 1

                # Update the maximum number of students if necessary
                if number_of_students > max_number_of_students:
                    max_number_of_students = number_of_students

    return max_number_of_students

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    print(get_maximum_number_of_students_with_favorite_drink(n, k, a))

if __name__ == '__main__':
    main()

