
def get_input():
    H, N, M = map(int, input().split())
    return H, N, M

def get_extra_bricks(H, N, M):
    # Initialize variables
    extra_2x2 = 0
    extra_4x2 = 0
    
    # Loop through each layer of the pyramid
    for i in range(1, H+1):
        # Calculate the width of the current layer
        width = 2*i
        
        # Check if the current layer requires extra bricks
        if width > N:
            extra_2x2 += width - N
        if width > M:
            extra_4x2 += width - M
    
    return extra_2x2, extra_4x2

def get_output(extra_2x2, extra_4x2):
    return str(extra_2x2) + " " + str(extra_4x2)

if __name__ == '__main__':
    H, N, M = get_input()
    extra_2x2, extra_4x2 = get_extra_bricks(H, N, M)
    print(get_output(extra_2x2, extra_4x2))

