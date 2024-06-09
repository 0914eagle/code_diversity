
def get_arithmetic_progression(n, a):
    # Calculate the difference between the first two elements
    diff = a[1] - a[0]
    # Initialize a list to store the numbers that can be written on the card
    numbers = []
    # Loop through the sequence and check if the difference between each element and the previous element is equal to the first difference
    for i in range(1, n):
        if a[i] - a[i-1] == diff:
            numbers.append(a[i-1] + diff)
    # If the length of the list is 0, it means that no number can be written on the card to form an arithmetic progression
    if len(numbers) == 0:
        return -1
    # Otherwise, return the list of numbers
    return numbers

def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(get_arithmetic_progression(n, a))

if __name__ == '__main__':
    main()

