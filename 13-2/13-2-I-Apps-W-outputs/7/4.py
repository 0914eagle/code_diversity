
def is_odd_subsegments(numbers):
    # Initialize variables
    subsegments = []
    current_subsegment = []
    previous_number = None

    # Iterate through the numbers
    for number in numbers:
        # If the current number is odd and different from the previous number, start a new subsegment
        if number % 2 == 1 and number != previous_number:
            current_subsegment = [number]
            subsegments.append(current_subsegment)
        # If the current number is even and different from the previous number, add it to the current subsegment
        elif number % 2 == 0 and number != previous_number:
            current_subsegment.append(number)
        # If the current number is the same as the previous number, do nothing
        else:
            pass
        # Update the previous number
        previous_number = number

    # Check if the subsegments have an odd length
    for subsegment in subsegments:
        if len(subsegment) % 2 == 1:
            return True
    return False

def main():
    n = int(input())
    numbers = list(map(int, input().split()))
    print("Yes") if is_odd_subsegments(numbers) else print("No")

if __name__ == '__main__':
    main()

