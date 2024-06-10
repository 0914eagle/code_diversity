
def get_largest_number_of_destroyed_spaceships(n1, m1, y1, n2, m2, y2):
    # Find the largest number of spaceships that can be destroyed by positioning the small spaceships at x = 0
    destroyed_spaceships = 0
    for i in range(n1):
        for j in range(n2):
            if y1[i] == y2[j]:
                destroyed_spaceships += 1
    return destroyed_spaceships

def main():
    n1, m1 = map(int, input().split())
    y1 = list(map(int, input().split()))
    n2, m2 = map(int, input().split())
    y2 = list(map(int, input().split()))
    largest_number_of_destroyed_spaceships = get_largest_number_of_destroyed_spaceships(n1, m1, y1, n2, m2, y2)
    print(largest_number_of_destroyed_spaceships)

if __name__ == '__main__':
    main()

