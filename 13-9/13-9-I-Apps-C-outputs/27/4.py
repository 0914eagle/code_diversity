
def get_minimum_chairs(n_guests, left_right_requirements):
    # Initialize variables
    min_chairs = 0
    current_chairs = 0
    guests_with_requirements = []

    # Loop through the input and find the guests with requirements
    for i in range(n_guests):
        left, right = left_right_requirements[i]
        if left > 0 or right > 0:
            guests_with_requirements.append((i, left, right))

    # Sort the guests by their left requirements in descending order
    guests_with_requirements.sort(key=lambda x: x[1], reverse=True)

    # Loop through the guests and assign chairs
    for i, left, right in guests_with_requirements:
        current_chairs += 1
        min_chairs = max(min_chairs, current_chairs)
        if left > 0:
            current_chairs += left
        if right > 0:
            current_chairs += right

    return min_chairs

def main():
    n_guests = int(input())
    left_right_requirements = []
    for i in range(n_guests):
        left, right = map(int, input().split())
        left_right_requirements.append((left, right))
    print(get_minimum_chairs(n_guests, left_right_requirements))

if __name__ == '__main__':
    main()

