
def solve(n, t, v):
    # Find the maximum start time and minimum velocity
    max_start_time = max(t)
    min_velocity = min(v)
    
    # Calculate the minimum length of the pack
    length = (max_start_time * min_velocity) / (min_velocity - 1)
    
    return length

def main():
    n = int(input())
    t = []
    v = []
    for i in range(n):
        t_i, v_i = map(int, input().split())
        t.append(t_i)
        v.append(v_i)
    length = solve(n, t, v)
    print(f"{length:.3f}")

if __name__ == '__main__':
    main()

