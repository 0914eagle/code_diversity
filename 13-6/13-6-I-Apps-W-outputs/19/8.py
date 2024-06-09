
def get_fruits(a, b, c):
    # Calculate the maximum total number of lemons, apples, and pears that can be used to make the compote
    total_lemons = a // 1
    total_apples = b // 2
    total_pears = c // 4
    
    # Return the maximum total number of fruits that can be used to make the compote
    return total_lemons + total_apples + total_pears

def main():
    # Read the input data from stdin
    a, b, c = map(int, input().split())
    
    # Call the get_fruits function and print the result
    print(get_fruits(a, b, c))

if __name__ == '__main__':
    main()

