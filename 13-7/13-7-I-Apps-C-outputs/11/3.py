
def get_min_energy(n, q, a, k):
    # Initialize a dictionary to store the minimum energy released for each number of neutrons
    min_energy = {1: 0}
    for i in range(2, n+1):
        min_energy[i] = a[i-1]

    # Loop through each query and find the minimum energy released
    for i in range(q):
        # If the number of neutrons is less than or equal to the neutron threshold, return the energy released
        if k[i] <= n:
            print(min_energy[k[i]])
        # Otherwise, decompose the atom into two atoms and find the minimum energy released for each atom
        else:
            # Find the number of neutrons in each atom
            i, j = divmod(k[i], 2)
            # If the number of neutrons in each atom is less than or equal to the neutron threshold, return the energy released
            if i <= n and j <= n:
                print(min_energy[i] + min_energy[j])
            # Otherwise, recursively find the minimum energy released for each atom
            else:
                print(get_min_energy(n, 1, a, i) + get_min_energy(n, 1, a, j))

n, q = map(int, input().split())
a = list(map(int, input().split()))
k = list(map(int, input().split()))
get_min_energy(n, q, a, k)

