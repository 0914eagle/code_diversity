
def get_average_number_of_visitors(guests, table_length):
    # Calculate the total number of guests that can fit in the table
    total_guests = 0
    for guest in guests:
        if sum(guests) <= table_length:
            total_guests += 1
        else:
            break
    
    # Calculate the average number of visitors
    average_visitors = total_guests / len(guests)
    
    return average_visitors

def main():
    # Read input
    n = int(input())
    guests = [int(x) for x in input().split()]
    table_length = int(input())
    
    # Calculate the average number of visitors
    average_visitors = get_average_number_of_visitors(guests, table_length)
    
    # Print output
    print(average_visitors)

if __name__ == '__main__':
    main()

