
def get_earliest_delivery_time(A, B, C, D, E):
    # Calculate the delivery time for each dish
    delivery_time_abc_don = A
    delivery_time_arc_curry = B + delivery_time_abc_don
    delivery_time_agc_pasta = C + delivery_time_arc_curry
    delivery_time_atc_hanbagu = D + delivery_time_agc_pasta
    delivery_time_apc_ramen = E + delivery_time_atc_hanbagu

    # Return the earliest delivery time
    return min(delivery_time_apc_ramen, delivery_time_atc_hanbagu, delivery_time_agc_pasta, delivery_time_arc_curry, delivery_time_abc_don)

def main():
    A, B, C, D, E = map(int, input().split())
    print(get_earliest_delivery_time(A, B, C, D, E))

if __name__ == '__main__':
    main()

