
def get_maximum_number_of_students_with_favorite_drink(n, k, drinks):
    # Initialize a dictionary to store the count of each drink type
    drink_count = {}
    for drink in drinks:
        if drink in drink_count:
            drink_count[drink] += 1
        else:
            drink_count[drink] = 1

    # Sort the dictionary by value in descending order
    sorted_drink_count = sorted(drink_count.items(), key=lambda x: x[1], reverse=True)

    # Initialize the maximum number of students with favorite drink as 0
    max_students = 0

    # Iterate through the dictionary and find the maximum number of students with favorite drink
    for i in range(len(sorted_drink_count)):
        current_drink, current_count = sorted_drink_count[i]
        remaining_students = n - (i + 1)
        if current_count >= remaining_students:
            max_students += remaining_students
        else:
            max_students += current_count

    return max_students

def main():
    n, k = map(int, input().split())
    drinks = []
    for i in range(n):
        drinks.append(int(input()))
    print(get_maximum_number_of_students_with_favorite_drink(n, k, drinks))

if __name__ == '__main__':
    main()

