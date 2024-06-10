
def get_chaos(n, p, perm):
    # Calculate the chaos in each coach
    chaos = [round(p_i/10)*10 for p_i in p]
    
    # Calculate the total chaos by summing the chaos of each coach
    total_chaos = sum(chaos)
    
    # If the permutation is given, calculate the maximum chaos by blowing up each coach in the order given
    if perm:
        perm = [int(i)-1 for i in perm.split()]
        max_chaos = 0
        for i in perm:
            max_chaos += chaos[i]
        return max_chaos
    
    # If the permutation is not given, return the total chaos
    else:
        return total_chaos

def main():
    n = int(input())
    p = list(map(int, input().split()))
    perm = input()
    print(get_chaos(n, p, perm))

if __name__ == '__main__':
    main()

