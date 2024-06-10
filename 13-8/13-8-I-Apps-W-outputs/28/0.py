
def get_interval(even_steps, odd_steps):
    # Initialize a list to store the numbers of steps with even and odd numbers
    steps = [0] * 101
    
    # Populate the list with the number of steps with even and odd numbers
    for i in range(1, 101):
        if i % 2 == 0:
            steps[i] = even_steps
        else:
            steps[i] = odd_steps
    
    # Iterate through the list and check if there is an interval with the given number of steps
    for i in range(1, 100):
        for j in range(i+1, 101):
            if steps[i] == steps[j]:
                return "YES"
    
    return "NO"

def main():
    even_steps, odd_steps = map(int, input().split())
    print(get_interval(even_steps, odd_steps))

if __name__ == '__main__':
    main()

