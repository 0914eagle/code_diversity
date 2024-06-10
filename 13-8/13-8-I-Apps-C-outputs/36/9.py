
def get_min_pack_length(N, t, v):
    # Sort the cheetahs by their start time
    sorted_cheetahs = sorted(zip(t, v), key=lambda x: x[0])

    # Initialize the minimum pack length and the current position of the first cheetah
    min_pack_length = 0
    current_position = 0

    # Loop through each cheetah
    for i in range(N):
        # Calculate the position of the current cheetah based on its start time and velocity
        current_position += (sorted_cheetahs[i][0] * sorted_cheetahs[i][1])

        # If the current position is greater than the minimum pack length, update the minimum pack length
        if current_position > min_pack_length:
            min_pack_length = current_position

    return min_pack_length

def main():
    N = int(input())
    t = []
    v = []
    for i in range(N):
        t_i, v_i = map(int, input().split())
        t.append(t_i)
        v.append(v_i)
    min_pack_length = get_min_pack_length(N, t, v)
    print(f"{min_pack_length:.3f}")

if __name__ == '__main__':
    main()

