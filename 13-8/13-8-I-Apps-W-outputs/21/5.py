
def get_optimal_solution(n, a, b):
    # Find the greatest common divisor of n and a
    gcd_na = gcd(n, a)
    # Find the greatest common divisor of n and b
    gcd_nb = gcd(n, b)
    # Calculate the minimum area that the room must have to accommodate n students
    min_area = 6 * n
    # Initialize the optimal solution
    optimal_solution = (0, 0, 0)
    # Iterate over all possible values of s, the side length of the square room
    for s in range(1, int(min_area ** 0.5) + 1):
        # Check if s is a divisor of both a and b
        if a % s == 0 and b % s == 0:
            # Calculate the area of the room
            area = s * s
            # Check if the area is greater than or equal to the minimum area
            if area >= min_area:
                # Calculate the number of students that can be accommodated in the room
                num_students = area // 6
                # Check if the number of students is equal to n
                if num_students == n:
                    # Update the optimal solution
                    optimal_solution = (s, a // s, b // s)
                    break
    return optimal_solution

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def main():
    n, a, b = map(int, input().split())
    optimal_solution = get_optimal_solution(n, a, b)
    print(optimal_solution[0] * optimal_solution[1] * optimal_solution[2])

if __name__ == '__main__':
    main()

