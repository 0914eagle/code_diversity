
def get_maximum_distance(n, x, a, b):
    if x == 0:
        return abs(a - b)
    
    # Initialize the distance between the rivals
    distance = abs(a - b)
    
    # Loop through each swap
    for i in range(x):
        # Find the two adjacent students
        student1 = a - 1 if a - 1 >= 1 else n
        student2 = a + 1 if a + 1 <= n else 1
        
        # Check if the distance between the rivals is increased
        if abs(student1 - student2) > distance:
            distance = abs(student1 - student2)
    
    return distance

def main():
    t = int(input())
    for _ in range(t):
        n, x, a, b = map(int, input().split())
        print(get_maximum_distance(n, x, a, b))

if __name__ == '__main__':
    main()

