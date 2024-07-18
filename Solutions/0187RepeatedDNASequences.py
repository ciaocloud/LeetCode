import collections
from typing import List


def findRepeatedDnaSequences(s: str) -> List[str]:
    counts = collections.defaultdict(int)
    ans = []
    h = 0
    m = {'A': 0, 'T': 1, 'C': 2, 'G': 3}
    w = 10 ## window
    b = len(m) ## base

    j = 0
    while j < len(s):
        h = h * b + m[s[j]]
        j += 1
        if j < w:
            continue
        counts[h] += 1
        if counts[h] == 2:
            ans.append(s[j-10:j])
        h -= m[s[j-10]] * (b ** (w-1))
    return ans

    # for j in range(len(s)):
    #     if j < w:
    #         h = h * b + m[s[j]]
    #         if j == w - 1:
    #             counts[s[j]] += 1
    #     else:
    #         h = h * b + m[s[j]] - m[s[j-w]] * (b ** w)
    #         counts[h] += 1
    #         if counts[h] == 2:
    #             ans.append(s[j-w+1:j+1])
    # return ans

if __name__ == '__main__':
    print(findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))