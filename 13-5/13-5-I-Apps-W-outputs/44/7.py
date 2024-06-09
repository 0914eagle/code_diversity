
def get_maximal_bouquets(r, g, b):
    # Initialize the maximal number of bouquets to 0
    maximal_bouquets = 0
    
    # Loop through the possible number of red flowers
    for i in range(r + 1):
        # Loop through the possible number of green flowers
        for j in range(g + 1):
            # Loop through the possible number of blue flowers
            for k in range(b + 1):
                # Check if the current combination of flowers is valid
                if i + j + k > 0:
                    # Calculate the number of red bouquets that can be made with the current combination of flowers
                    red_bouquets = i // 3
                    # Calculate the number of green bouquets that can be made with the current combination of flowers
                    green_bouquets = j // 3
                    # Calculate the number of blue bouquets that can be made with the current combination of flowers
                    blue_bouquets = k // 3
                    # Calculate the number of mixing bouquets that can be made with the current combination of flowers
                    mixing_bouquets = (i % 3 + j % 3 + k % 3) // 3
                    # Calculate the total number of bouquets that can be made with the current combination of flowers
                    total_bouquets = red_bouquets + green_bouquets + blue_bouquets + mixing_bouquets
                    # Update the maximal number of bouquets if necessary
                    if total_bouquets > maximal_bouquets:
                        maximal_bouquets = total_bouquets
    
    # Return the maximal number of bouquets
    return maximal_bouquets

def main():
    # Read the number of red, green and blue flowers
    r, g, b = map(int, input().split())
    # Call the get_maximal_bouquets function and print the result
    print(get_maximal_bouquets(r, g, b))

if __name__ == '__main__':
    main()

