
def is_arithmetic_progression(b):
    if len(b) <= 2:
        return True
    else:
        difference = b[1] - b[0]
        for i in range(2, len(b)):
            if b[i] - b[i-1] != difference:
                return False
        return True

def make_arithmetic_progression(b):
    if len(b) == 1:
        return 0
    elif len(b) == 2:
        if b[0] == b[1]:
            return 0
        else:
            return 1
    else:
        # Find the smallest and largest number in the list
        smallest = min(b)
        largest = max(b)
        # Find the middle number
        middle = (smallest + largest) // 2
        # Count the number of elements that need to be changed
        count = 0
        for num in b:
            if num != middle:
                count += 1
        return count

def main():
    n = int(input())
    b = list(map(int, input().split()))
    if is_arithmetic_progression(b):
        print(0)
    else:
        print(make_arithmetic_progression(b))

if __name__ == "__main__":
    main()

