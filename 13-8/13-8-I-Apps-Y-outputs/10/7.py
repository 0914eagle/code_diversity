
def get_best_days(n, temperatures):
    # Find the two hiking days with the smallest maximum temperature
    hiking_days = []
    for i in range(n-2):
        if temperatures[i] <= temperatures[i+1] and temperatures[i] <= temperatures[i+2]:
            hiking_days.append(i)
    
    # Return the best day to start the trip and the maximum temperature during the hiking days
    if len(hiking_days) == 0:
        return -1, -1
    else:
        return hiking_days[0], temperatures[hiking_days[0] + 1]

def main():
    n = int(input())
    temperatures = list(map(int, input().split()))
    print(get_best_days(n, temperatures))

if __name__ == '__main__':
    main()

