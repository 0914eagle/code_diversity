
def get_criminal_count(n, a, t):
    # Initialize a list to store the number of criminals for each distance
    criminals = [0] * (n + 1)
    
    # Loop through the input array and update the number of criminals for each distance
    for i in range(n):
        distance = abs(a - i)
        criminals[distance] += t[i]
    
    # Return the total number of criminals
    return sum(criminals)

def main():
    n, a = map(int, input().split())
    t = list(map(int, input().split()))
    print(get_criminal_count(n, a, t))

if __name__ == '__main__':
    main()

