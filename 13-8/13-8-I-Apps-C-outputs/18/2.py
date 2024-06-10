
def get_media_companies(n, k, c, a):
    # Initialize a list to store the media companies and their requirements
    media_companies = []
    
    # Iterate through the sectors and fans
    for i in range(n):
        # If the sector is not already filled by a media company
        if i not in [m[0] for m in media_companies]:
            # Find the next available sector that satisfies the requirements
            for j in range(i, n):
                # If the sector is not already filled by a media company and has at least K consecutive sectors with at least C distinct colors
                if j not in [m[0] for m in media_companies] and len(set(a[j:j+k])) >= c:
                    # Add the sector to the media company's list of sectors
                    media_companies.append([j, set()])
                    # Add the colors of the fans in the sector to the media company's set of colors
                    media_companies[-1][1].update(set(a[j:j+k]))
                    # Break out of the inner loop and continue with the next sector
                    break
    
    # Return the maximum number of media companies that can be sold broadcasting rights
    return len(media_companies)

def main():
    n, k, c = map(int, input().split())
    a = list(map(int, input().split()))
    print(get_media_companies(n, k, c, a))

if __name__ == '__main__':
    main()

