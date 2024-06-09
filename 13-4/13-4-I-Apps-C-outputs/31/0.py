
def solve(n, g, d, e, links):
    # Initialize the minimum UW distance
    min_uw_distance = float('inf')
    
    # Loop through all possible pairs of star systems
    for i in range(n):
        for j in range(i+1, n):
            # If the two star systems are of different types, continue
            if d[i] != d[j]:
                continue
                
            # Calculate the UW distance between the two star systems
            uw_distance = calculate_uw_distance(g[i], g[j], links)
            
            # If the UW distance is less than the minimum, update the minimum
            if uw_distance < min_uw_distance:
                min_uw_distance = uw_distance
    
    # Return the minimum UW distance
    return min_uw_distance

def calculate_uw_distance(g1, g2, links):
    # Calculate the capacitance, potential, and inductance of the two star systems
    capacitance = g1 + g2
    potential = g1 - g2
    inductance = g1 * g2
    
    # Calculate the UW distance
    uw_distance = abs(potential * (capacitance * capacitance - inductance))
    
    # Return the UW distance
    return uw_distance

def main():
    # Read the input
    n, g, d, e, links = read_input()
    
    # Solve the problem
    min_uw_distance = solve(n, g, d, e, links)
    
    # Print the output
    print(min_uw_distance)

def read_input():
    # Read the number of star systems
    n = int(input())
    
    # Initialize the lists for the gravity values and types
    g = []
    d = []
    
    # Loop through the star systems
    for i in range(n):
        # Read the gravity value and type
        gi, di = input().split()
        g.append(int(gi))
        d.append(di)
    
    # Read the number of direct links
    e = int(input())
    
    # Initialize the list for the direct links
    links = []
    
    # Loop through the direct links
    for i in range(e):
        # Read the two star systems connected by the link
        si, ti = input().split()
        links.append((int(si), int(ti)))
    
    # Return the input
    return n, g, d, e, links

if __name__ == '__main__':
    main()

