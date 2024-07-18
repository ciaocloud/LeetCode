import collections


def minWindow(s: str, t: str) -> str:
    tmap = collections.Counter(t)
    wmap = collections.defaultdict(int)
    ans = ""
    i, j, k = 0, 0, 0
    while j < len(s):
        cj = s[j]
        if cj in tmap:
            wmap[cj] += 1
            if wmap[cj] == tmap[cj]:
                k += 1
            while k == len(tmap):
                if ans == "" or j - i + 1 < len(ans):
                    ans = s[i:j+1]
                ci = s[i]
                i += 1
                if ci in tmap:
                    wmap[ci] -= 1
                    if wmap[ci] < tmap[ci]:
                        k -= 1
        j += 1
    return ans

def minWindowOptimized(s: str, t: str) -> str:
    tmap = collections.Counter(t)
    wmap = collections.defaultdict(int)

    filtered = []
    for i, c in enumerate(s):
        if c in tmap:
            filtered.append((i, c))
    i, j, k = 0, 0, 0
    ans = ""
    while j < len(filtered):
        cj = filtered[j][1]
        wmap[cj] += 1
        if wmap[cj] == tmap[cj]:
            k += 1
        while k == len(tmap):
            l, r = filtered[i][0], filtered[j][0]
            if ans == "" or r - l + 1 < len(ans):
                ans = s[l:r+1]
            ci = filtered[i][1]
            i += 1
            wmap[ci] -= 1
            if wmap[ci] < tmap[ci]:
                k -= 1
        j += 1
    return ans

if __name__ == '__main__':
    print("ans=", minWindowOptimized('abc', 'abc'))