
def solve(A, B, C, D, E):
    # Calculate the time it takes to serve each dish
    time_ABC_Don = A
    time_ARC_Curry = B
    time_AGC_Pasta = C
    time_ATC_Hanbagu = D
    time_APC_Ramen = E

    # Calculate the earliest possible time for each dish to be delivered
    earliest_time_ABC_Don = 0
    earliest_time_ARC_Curry = earliest_time_ABC_Don + time_ABC_Don
    earliest_time_AGC_Pasta = earliest_time_ARC_Curry + time_ARC_Curry
    earliest_time_ATC_Hanbagu = earliest_time_AGC_Pasta + time_AGC_Pasta
    earliest_time_APC_Ramen = earliest_time_ATC_Hanbagu + time_ATC_Hanbagu

    # Return the earliest possible time for the last dish to be delivered
    return earliest_time_APC_Ramen

