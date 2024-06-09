
def get_criminals_detected(n, a, t):
    # Initialize a list to store the number of criminals detected at each distance
    criminals_detected = [0] * (n + 1)
    
    # Iterate over the t[i] for each city i
    for i in range(n):
        # If there is a criminal in city i, update the number of criminals detected at each distance
        if t[i] == 1:
            for j in range(i + 1):
                criminals_detected[j] += 1
    
    # Return the number of criminals detected at distance a
    return criminals_detected[a]

def main():
    # Read the input n, a, and t
    n, a = map(int, input().split())
    t = list(map(int, input().split()))
    
    # Call the get_criminals_detected function and print the result
    print(get_criminals_detected(n, a, t))

if __name__ == '__main__':
    main()

