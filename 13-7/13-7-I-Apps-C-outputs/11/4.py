
def solve(n, q, a):
    # Initialize a dictionary to store the minimum energy released for each number of neutrons
    min_energy = {1: 0}
    for i in range(2, n+1):
        min_energy[i] = a[i-1]

    # Loop through each query and calculate the minimum energy released
    for k in range(1, q+1):
        # If the number of neutrons is less than or equal to the neutron threshold, return the energy released
        if k <= n:
            print(min_energy[k])
        # Otherwise, decompose the atom into two atoms and calculate the minimum energy released for each atom
        else:
            i = 1
            j = k-1
            while i + j == k and i >= 1 and j >= 1:
                min_energy[k] = min(min_energy[k], min_energy[i] + min_energy[j])
                i += 1
                j -= 1
            print(min_energy[k])

n, q = map(int, input().split())
a = list(map(int, input().split()))
solve(n, q, a)

