
def get_two_distinct_integers(l1, r1, l2, r2):
    # Find the smallest integer that is greater than or equal to the left endpoint of the first segment and less than or equal to the right endpoint of the first segment
    a = max(l1, int(l1))
    # Find the smallest integer that is greater than or equal to the left endpoint of the second segment and less than or equal to the right endpoint of the second segment
    b = max(l2, int(l2))
    # If a and b are not equal, return a and b
    if a != b:
        return a, b
    # If a and b are equal, find the next integer that is greater than a and less than or equal to the right endpoint of the first segment
    a = min(r1, a + 1)
    # Find the next integer that is greater than b and less than or equal to the right endpoint of the second segment
    b = min(r2, b + 1)
    # Return a and b
    return a, b

def main():
    q = int(input())
    for i in range(q):
        l1, r1, l2, r2 = map(int, input().split())
        a, b = get_two_distinct_integers(l1, r1, l2, r2)
        print(a, b)

if __name__ == '__main__':
    main()

