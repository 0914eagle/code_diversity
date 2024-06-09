
import sys

def get_inconvenience(bridges, num_bridges):
    inconvenience = 0
    for i in range(num_bridges):
        bridge = bridges[i]
        for j in range(i+1, num_bridges):
            other_bridge = bridges[j]
            if bridge[0] == other_bridge[0] or bridge[0] == other_bridge[1] or bridge[1] == other_bridge[0] or bridge[1] == other_bridge[1]:
                inconvenience += 1
    return inconvenience

def main():
    num_islands, num_bridges = map(int, input().split())
    bridges = []
    for _ in range(num_bridges):
        a, b = map(int, input().split())
        bridges.append((a, b))
    for i in range(num_bridges):
        print(get_inconvenience(bridges[:i+1], num_bridges))

if __name__ == "__main__":
    main()

