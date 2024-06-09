
def solve(A, B, C, D, E):
    # Calculate the time it takes to serve each dish
    time_ABC_Don = A
    time_ARC_Curry = B
    time_AGC_Pasta = C
    time_ATC_Hanbagu = D
    time_APC_Ramen = E
    
    # Calculate the earliest possible time for the last dish to be delivered
    earliest_time = time_ABC_Don + time_ARC_Curry + time_AGC_Pasta + time_ATC_Hanbagu + time_APC_Ramen
    
    return earliest_time

