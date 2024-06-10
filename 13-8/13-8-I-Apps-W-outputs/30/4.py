
def get_maximum_number(v, a):
    # Initialize variables
    maximum_number = 0
    used_paint = 0
    digits = []

    # Sort the array in descending order
    a.sort(reverse=True)

    # Loop through the array and find the maximum number that can be written
    for i in range(len(a)):
        if used_paint + a[i] <= v:
            used_paint += a[i]
            digits.append(str(i+1))
            maximum_number = int("".join(digits))
        else:
            break

    # If the paint is not enough for any digit, return -1
    if used_paint < v:
        return -1

    # Return the maximum number that can be written
    return maximum_number

def main():
    v = int(input())
    a = list(map(int, input().split()))
    print(get_maximum_number(v, a))

if __name__ == '__main__':
    main()

