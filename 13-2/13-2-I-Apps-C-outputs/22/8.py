
def solve(n, k):
    # Check if k is valid
    if k < 1 or k > n:
        return "NO"
    
    # Initialize the stations as a list of tuples (MS, ME) and (VS, VE)
    stations_mobi = [(i, i+1) for i in range(1, n, 2)]
    stations_vina = [(i+1, i) for i in range(2, n, 2)]
    
    # Check if the stations are valid
    for i in range(k):
        ms, me = stations_mobi[i]
        vs, ve = stations_vina[i]
        if ms >= ve or vs >= me:
            return "NO"
    
    # Check if the conditions are satisfied
    for i in range(k):
        ms, me = stations_mobi[i]
        vs, ve = stations_vina[i]
        for j in range(i+1, k):
            ms_j, me_j = stations_mobi[j]
            vs_j, ve_j = stations_vina[j]
            if ms < ms_j and me < me_j:
                return "NO"
            if vs < vs_j and ve < ve_j:
                return "NO"
    
    # If all conditions are satisfied, return the stations
    return "YES\n" + "\n".join([f"{ms} {me}" for ms, me in stations_mobi]) + "\n" + "\n".join([f"{vs} {ve}" for vs, ve in stations_vina])

