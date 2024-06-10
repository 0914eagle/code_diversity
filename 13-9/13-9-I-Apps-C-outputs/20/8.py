
def get_min_length(t, v):
    # Calculate the time it takes for each cheetah to cover the distance
    time_taken = [100000 / v[i] for i in range(len(v))]
    
    # Find the minimum time taken by any cheetah
    min_time = min(time_taken)
    
    # Calculate the minimum length of the pack
    min_length = min_time * min(v)
    
    return min_length

def main():
    n = int(input())
    t = []
    v = []
    for i in range(n):
        t_i, v_i = map(int, input().split())
        t.append(t_i)
        v.append(v_i)
    print(get_min_length(t, v))

if __name__ == '__main__':
    main()

