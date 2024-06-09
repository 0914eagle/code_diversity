
def get_maximum_students_with_favorite_drink(n, k, a):
    # Calculate the minimum number of sets needed to give each student a drink
    min_sets = int(n / 2) + 1
    
    # Initialize a dictionary to store the number of students with each drink type
    drink_count = {i: 0 for i in range(1, k+1)}
    
    # Iterate over the students and increment the drink count for their favorite drink type
    for i in range(n):
        drink_count[a[i]] += 1
    
    # Initialize the maximum number of students with a favorite drink as 0
    max_students = 0
    
    # Iterate over the drink types and calculate the maximum number of students with that drink type
    for i in range(1, k+1):
        max_students = max(max_students, min_sets - drink_count[i] + 1)
    
    return max_students

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    print(get_maximum_students_with_favorite_drink(n, k, a))

if __name__ == '__main__':
    main()

