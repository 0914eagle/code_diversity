
def get_max_distance(N, T_i, s_i, a_i):
    # Calculate the minimum radians needed to go from angle a_i to the x-axis
    dist = abs(a_i - 0)
    
    # Calculate the maximum distance that the spaceship can travel from star i
    max_dist = max(0, T_i - s_i * dist)
    
    return max_dist

def solve(N, T_i, s_i, a_i):
    # Calculate the maximum distance that the spaceship can travel from each star
    max_dist_list = [get_max_distance(N, T_i, s_i, a_i) for T_i, s_i, a_i in zip(T_i, s_i, a_i)]
    
    # Calculate the total distance that the spaceship can travel
    total_dist = sum(max_dist_list)
    
    return total_dist

if __name__ == '__main__':
    N = int(input())
    T_i = []
    s_i = []
    a_i = []
    
    for _ in range(N):
        T_i.append(float(input()))
        s_i.append(float(input()))
        a_i.append(float(input()))
    
    print(solve(N, T_i, s_i, a_i))

