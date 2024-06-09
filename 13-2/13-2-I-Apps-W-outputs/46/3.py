
def get_max_orders(orders):
    orders.sort(key=lambda x: x[0])
    count = 0
    end_time = 0
    for order in orders:
        if order[0] >= end_time:
            count += 1
            end_time = order[1]
    return count

