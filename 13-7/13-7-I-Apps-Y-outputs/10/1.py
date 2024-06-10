
def get_flight_times(p, q, r):
    return p, q, r

def get_min_sum_of_flight_times(p, q, r):
    flights = [(p, q), (q, r), (r, p)]
    min_sum = float('inf')
    for i in range(3):
        for j in range(i+1, 3):
            flight_time = flights[i][1] + flights[j][0]
            if flight_time < min_sum:
                min_sum = flight_time
    return min_sum

if __name__ == '__main__':
    p, q, r = map(int, input().split())
    print(get_min_sum_of_flight_times(p, q, r))

