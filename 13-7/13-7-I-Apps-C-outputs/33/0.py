
def find_best_flight_to_cancel(flights):
    # Find the flight with the most connections
    flight_count = {}
    for flight in flights:
        if flight[0] not in flight_count:
            flight_count[flight[0]] = 0
        if flight[1] not in flight_count:
            flight_count[flight[1]] = 0
        flight_count[flight[0]] += 1
        flight_count[flight[1]] += 1
    flight_to_cancel = max(flight_count, key=flight_count.get)
    return flight_to_cancel

def find_best_new_flight(flights, flight_to_cancel):
    # Find the pair of cities that minimizes the number of flight changes
    min_changes = float('inf')
    new_flight = None
    for i in range(len(flights)):
        for j in range(i+1, len(flights)):
            flight1 = flights[i]
            flight2 = flights[j]
            if flight1[0] == flight_to_cancel or flight1[1] == flight_to_cancel or flight2[0] == flight_to_cancel or flight2[1] == flight_to_cancel:
                continue
            changes = 0
            for flight in flights:
                if flight[0] == flight1[1] and flight[1] == flight2[0]:
                    changes += 1
                elif flight[0] == flight2[1] and flight[1] == flight1[0]:
                    changes += 1
            if changes < min_changes:
                min_changes = changes
                new_flight = (flight1[0], flight2[1])
    return new_flight

def main():
    n = int(input())
    flights = []
    for i in range(n-1):
        flights.append(tuple(map(int, input().split())))
    flight_to_cancel = find_best_flight_to_cancel(flights)
    new_flight = find_best_new_flight(flights, flight_to_cancel)
    print(flight_to_cancel)
    print(new_flight)

if __name__ == '__main__':
    main()

