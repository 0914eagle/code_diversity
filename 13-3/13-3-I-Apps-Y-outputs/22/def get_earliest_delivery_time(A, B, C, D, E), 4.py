
def get_earliest_delivery_time(A, B, C, D, E):
    # Calculate the delivery time for each dish
    delivery_time_ABC_Don = A
    delivery_time_ARC_Curry = B + delivery_time_ABC_Don
    delivery_time_AGC_Pasta = C + delivery_time_ARC_Curry
    delivery_time_ATC_Hanbagu = D + delivery_time_AGC_Pasta
    delivery_time_APC_Ramen = E + delivery_time_ATC_Hanbagu

    # Return the earliest delivery time
    return min(delivery_time_APC_Ramen, delivery_time_ATC_Hanbagu, delivery_time_AGC_Pasta, delivery_time_ARC_Curry, delivery_time_ABC_Don)

