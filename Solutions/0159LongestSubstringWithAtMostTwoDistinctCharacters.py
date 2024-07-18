import collections


def lengthOfLongestSubstringTwoDistinct(s: str) -> int:
    i, j = 0, 0
    ans = 0
    m = collections.defaultdict(int)
    while j < len(s):
        cj = s[j]
        m[cj] += 1
        j += 1
        while len(m) > 2:
            ci = s[i]
            m[ci] -= 1
            i += 1
            if m[ci] == 0:
                del m[ci]
        ans = max(ans, j-i)
    return ans

def lengthOfLongestSubstringTwoDistinctOptimized(s: str) -> int:
    i, j = 0, 0
    ans = 0
    m = collections.defaultdict(int)
    while j < len(s):
        cj = s[j]
        m[cj] = j
        j += 1
        while len(m) > 2:
            i = min(m.values())
            ci = s[i]
            del m[ci]
            i += 1
        ans = max(ans, j - i)
    return ans

if __name__ == '__main__':
    print(lengthOfLongestSubstringTwoDistinct("eceba"))
    print(lengthOfLongestSubstringTwoDistinctOptimized("eceba"))