
def get_criminals_count(n, a, t):
    # Initialize a list to store the number of criminals for each distance
    criminals_count = [0] * (n + 1)
    
    # Loop through the input array and update the criminals count for each distance
    for i in range(n):
        distance = abs(a - i)
        criminals_count[distance] += t[i]
    
    # Return the total number of criminals that Limak will catch
    return sum(criminals_count)

def main():
    n, a = map(int, input().split())
    t = list(map(int, input().split()))
    print(get_criminals_count(n, a, t))

if __name__ == '__main__':
    main()

