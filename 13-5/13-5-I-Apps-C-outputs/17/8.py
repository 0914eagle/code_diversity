
def get_closest_handsome_number(N):
    N_str = str(N)
    N_len = len(N_str)
    for i in range(N_len):
        if N_str[i] == N_str[i-1]:
            return int(N_str[:i] + str(int(N_str[i-1]) ^ 1) + N_str[i+1:])
    return int(N_str[:-1] + str(int(N_str[-1]) ^ 1))

