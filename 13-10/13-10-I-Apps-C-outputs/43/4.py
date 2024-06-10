
def get_poll_results(n):
    # Read the poll results from stdin
    poll_results = []
    for _ in range(n):
        a, b, c = map(int, input().split())
        poll_results.append((a, b, c))
    return poll_results

def get_best_cluster_size(poll_results):
    # Sort the poll results by the measure a * S + b * T
    poll_results.sort(key=lambda x: x[0] * S + x[1] * T)
    
    # Find the indices of the first and last results with c = 1
    first_idx = 0
    for i in range(len(poll_results)):
        if poll_results[i][2] == 1:
            first_idx = i
            break
    last_idx = len(poll_results) - 1
    for i in range(len(poll_results) - 1, -1, -1):
        if poll_results[i][2] == 1:
            last_idx = i
            break
    
    # Return the cluster size as the minimum of the first and last indices
    return min(last_idx - first_idx + 1, len(poll_results) - first_idx)

def main():
    n = int(input())
    poll_results = get_poll_results(n)
    S = int(input())
    T = int(input())
    print(get_best_cluster_size(poll_results))

if __name__ == '__main__':
    main()

