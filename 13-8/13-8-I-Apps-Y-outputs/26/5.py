
def get_earliest_delivery_time(A, B, C, D, E):
    # Calculate the delivery time for each dish
    delivery_time_ABC_Don = A
    delivery_time_ARC_Curry = A + B
    delivery_time_AGC_Pasta = delivery_time_ARC_Curry + C
    delivery_time_ATC_Hanbagu = delivery_time_AGC_Pasta + D
    delivery_time_APC_Ramen = delivery_time_ATC_Hanbagu + E
    
    # Return the earliest delivery time
    return min(delivery_time_ABC_Don, delivery_time_ARC_Curry, delivery_time_AGC_Pasta, delivery_time_ATC_Hanbagu, delivery_time_APC_Ramen)

def main():
    # Read input
    A, B, C, D, E = map(int, input().split())
    
    # Call the function to get the earliest delivery time
    earliest_delivery_time = get_earliest_delivery_time(A, B, C, D, E)
    
    # Print the output
    print(earliest_delivery_time)

if __name__ == '__main__':
    main()

