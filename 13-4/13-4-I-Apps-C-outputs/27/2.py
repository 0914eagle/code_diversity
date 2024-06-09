
import heapq

def f1(customers):
    # Find the maximum distance between any two customers
    max_distance = 0
    for i in range(len(customers)):
        for j in range(i+1, len(customers)):
            distance = abs(customers[i][0] - customers[j][0]) + abs(customers[i][1] - customers[j][1])
            max_distance = max(max_distance, distance)
    
    # Divide the customers into two sets such that the maximum distance between any two customers in the same set is minimized
    set1 = []
    set2 = []
    for i in range(len(customers)):
        if i % 2 == 0:
            set1.append(customers[i])
        else:
            set2.append(customers[i])
    
    # Calculate the longest delivery time for each set
    longest_delivery_time1 = 0
    longest_delivery_time2 = 0
    for i in range(len(set1)):
        for j in range(i+1, len(set1)):
            distance = abs(set1[i][0] - set1[j][0]) + abs(set1[i][1] - set1[j][1])
            longest_delivery_time1 = max(longest_delivery_time1, distance)
    for i in range(len(set2)):
        for j in range(i+1, len(set2)):
            distance = abs(set2[i][0] - set2[j][0]) + abs(set2[i][1] - set2[j][1])
            longest_delivery_time2 = max(longest_delivery_time2, distance)
    
    return max(longest_delivery_time1, longest_delivery_time2)

def f2(customers):
    # Find the maximum distance between any two customers
    max_distance = 0
    for i in range(len(customers)):
        for j in range(i+1, len(customers)):
            distance = abs(customers[i][0] - customers[j][0]) + abs(customers[i][1] - customers[j][1])
            max_distance = max(max_distance, distance)
    
    # Divide the customers into two sets such that the maximum distance between any two customers in the same set is minimized
    set1 = []
    set2 = []
    for i in range(len(customers)):
        if i % 2 == 0:
            set1.append(customers[i])
        else:
            set2.append(customers[i])
    
    # Calculate the longest delivery time for each set
    longest_delivery_time1 = 0
    longest_delivery_time2 = 0
    for i in range(len(set1)):
        for j in range(i+1, len(set1)):
            distance = abs(set1[i][0] - set1[j][0]) + abs(set1[i][1] - set1[j][1])
            longest_delivery_time1 = max(longest_delivery_time1, distance)
    for i in range(len(set2)):
        for j in range(i+1, len(set2)):
            distance = abs(set2[i][0] - set2[j][0]) + abs(set2[i][1] - set2[j][1])
            longest_delivery_time2 = max(longest_delivery_time2, distance)
    
    return max(longest_delivery_time1, longest_delivery_time2)

if __name__ == '__main__':
    customers = []
    for _ in range(int(input())):
        customers.append(list(map(int, input().split())))
    print(f1(customers))
    print(f2(customers))

