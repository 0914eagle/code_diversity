
def paint_fence(r, b, k):
    # Initialize variables
    red_planks = 0
    blue_planks = 0
    consecutive_planks = 0

    # Loop through all planks
    for i in range(10**100):
        # Check if plank is divisible by r
        if i % r == 0:
            red_planks += 1
            consecutive_planks += 1
        # Check if plank is divisible by b
        elif i % b == 0:
            blue_planks += 1
            consecutive_planks += 1
        # Check if plank is divisible by both r and b
        elif i % (r * b) == 0:
            red_planks += 1
            blue_planks += 1
            consecutive_planks += 1
        # Check if plank is not divisible by r, b, or their product
        else:
            consecutive_planks = 0

        # Check if there are k consecutive planks of the same color
        if consecutive_planks == k:
            return "REBEL"

    # If we reach this point, we have painted all planks and there are no k consecutive planks of the same color
    return "OBEY"

def main():
    tests = int(input())
    for i in range(tests):
        r, b, k = map(int, input().split())
        print(paint_fence(r, b, k))

if __name__ == '__main__':
    main()

