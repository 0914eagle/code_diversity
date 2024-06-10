
def get_min_snacks(a, b):
    # Find the smallest common multiple of a and b
    # that is greater than or equal to the largest of a and b
    max_val = max(a, b)
    for i in range(max_val, max_val * 2):
        if i % a == 0 and i % b == 0:
            return i

    # If no common multiple is found, return the largest of a and b
    return max_val

def main():
    a, b = map(int, input().split())
    print(get_min_snacks(a, b))

if __name__ == '__main__':
    main()

