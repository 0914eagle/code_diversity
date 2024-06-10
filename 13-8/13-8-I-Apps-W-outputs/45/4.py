
def get_bacteria_growth(n):
    # Initialize variables
    bacteria = [1]
    days = 0
    nights = 0
    
    # Loop until the total mass of the bacteria is equal to n
    while sum(bacteria) != n:
        # Split the bacteria
        new_bacteria = []
        for mass in bacteria:
            if mass >= 2:
                new_bacteria.append(mass / 2)
                new_bacteria.append(mass / 2)
            else:
                new_bacteria.append(mass)
        bacteria = new_bacteria
        days += 1
        nights += 1
        
        # Increase the mass of the bacteria
        for i in range(len(bacteria)):
            bacteria[i] += 1
    
    # Return the number of days and nights needed
    return days, nights

def main():
    # Read the input
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        # Call the function to get the number of days and nights needed
        days, nights = get_bacteria_growth(n)
        
        # Print the output
        print(days)
        print(" ".join(str(night) for night in range(nights)))

if __name__ == '__main__':
    main()

