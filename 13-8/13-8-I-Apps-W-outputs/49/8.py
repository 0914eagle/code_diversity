
def get_min_number_of_sets(n, k):
    return int(n/2) + (n%2)

def get_max_number_of_students_with_favorite_drink(n, k, a):
    sets = get_min_number_of_sets(n, k)
    portions = [0] * k
    for i in range(n):
        portions[a[i]-1] += 1
    max_students = 0
    for i in range(k):
        if portions[i] > 0:
            max_students += portions[i]
    return max_students

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    print(get_max_number_of_students_with_favorite_drink(n, k, a))

if __name__ == '__main__':
    main()

