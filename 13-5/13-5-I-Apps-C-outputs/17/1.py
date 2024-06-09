
def get_closest_handsome_number(N):
    N_str = str(N)
    N_len = len(N_str)
    for i in range(N_len):
        if N_str[i] == N_str[i-1]:
            continue
        else:
            if N_str[i] == "1" and N_str[i-1] == "0":
                return int(N_str[:i] + "1" + N_str[i+1:])
            elif N_str[i] == "0" and N_str[i-1] == "1":
                return int(N_str[:i] + "0" + N_str[i+1:])
    return -1

