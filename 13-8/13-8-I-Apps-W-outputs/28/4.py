
def is_interval_exists(even_steps, odd_steps):
    # Initialize a list to store the steps
    steps = []
    
    # Iterate from 1 to infinity
    for i in range(1, 1000000000):
        # If the step is even, add it to the list
        if i % 2 == 0:
            steps.append(i)
        # If the step is odd, add it to the list
        else:
            steps.append(i)
        
        # If the list has at least `even_steps` even steps and at least `odd_steps` odd steps, return True
        if len(steps) - steps.count(0) >= even_steps and steps.count(0) >= odd_steps:
            return True
    
    # If the list has fewer than `even_steps` even steps and fewer than `odd_steps` odd steps, return False
    return False

def main():
    even_steps, odd_steps = map(int, input().split())
    print("YES") if is_interval_exists(even_steps, odd_steps) else print("NO")

if __name__ == '__main__':
    main()

