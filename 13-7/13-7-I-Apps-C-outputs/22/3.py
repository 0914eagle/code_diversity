
def get_toll_cost(entrance, exit):
    return abs(entrance - exit)

def get_least_toll_cost(tickets):
    toll_cost = 0
    for i in range(len(tickets)):
        for j in range(i+1, len(tickets)):
            entrance, exit = tickets[i]
            exit_2, entrance_2 = tickets[j]
            if entrance != entrance_2 and exit != exit_2:
                toll_cost += min(get_toll_cost(entrance, exit_2), get_toll_cost(entrance_2, exit))
    return toll_cost

def main():
    num_trucks = int(input())
    tickets = []
    for i in range(num_trucks):
        entrance, exit = map(int, input().split())
        tickets.append((entrance, exit))
    print(get_least_toll_cost(tickets))

if __name__ == '__main__':
    main()

