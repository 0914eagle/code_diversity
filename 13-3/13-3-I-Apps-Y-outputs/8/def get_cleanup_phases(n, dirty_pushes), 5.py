
def get_cleanup_phases(n, dirty_pushes):
    dirtiness = 0
    cleanup_phases = 0
    for i in range(n):
        dirtiness += dirty_pushes[i]
        if dirtiness > 20:
            cleanup_phases += 1
            dirtiness = dirty_pushes[i]
    return cleanup_phases

