
import sys
input = sys.stdin.read().splitlines()

def get_danger_level(chambers, tunnels):
    danger_levels = [0] * len(chambers)
    for tunnel in tunnels:
        chamber1, chamber2, length = tunnel
        danger_levels[chamber1-1] += length
        danger_levels[chamber2-1] += length
    return danger_levels

def main():
    num_chambers, num_tunnels = map(int, input[0].split())
    chambers = list(range(1, num_chambers+1))
    tunnels = []
    for i in range(1, num_tunnels+1):
        tunnel = list(map(int, input[i].split()))
        tunnels.append(tunnel)
    danger_levels = get_danger_level(chambers, tunnels)
    print(*[d%(10**9+7) for d in danger_levels])

if __name__ == "__main__":
    main()

