
def get_criminals_detected(n, a, t):
    # Initialize a list to store the number of criminals detected
    criminals_detected = []
    
    # Iterate over the input array
    for i in range(n):
        # Calculate the distance between the current city and Limak's city
        distance = abs(i - a)
        
        # If the distance is 0, there is only one criminal in the current city
        if distance == 0:
            criminals_detected.append(t[i])
        
        # If the distance is 1, there can be a criminal in either the previous or next city
        elif distance == 1:
            # If the current city is the first city, the criminal can be in the second city
            if i == 0:
                criminals_detected.append(t[i + 1])
            # If the current city is the last city, the criminal can be in the previous city
            elif i == n - 1:
                criminals_detected.append(t[i - 1])
            # If the current city is in the middle, the criminal can be in either the previous or next city
            else:
                criminals_detected.append(t[i - 1] + t[i + 1])
    
    # Return the number of criminals detected
    return sum(criminals_detected)

def main():
    # Read the input
    n, a = map(int, input().split())
    t = list(map(int, input().split()))
    
    # Call the function to get the number of criminals detected
    criminals_detected = get_criminals_detected(n, a, t)
    
    # Print the number of criminals detected
    print(criminals_detected)

if __name__ == '__main__':
    main()

