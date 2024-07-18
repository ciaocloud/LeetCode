import collections


def lengthOfLongestSubstring_SlidingWindow(s: str) -> int:
    i, j, ans = 0, 0, 0
    m = collections.defaultdict(int)
    while j < len(s):
        cj = s[j]
        m[cj] += 1
        while m[cj] > 1 and i < j:
            ci = s[i]
            m[ci] -= 1
            i += 1
        j += 1
        ans = max(ans, j - i)

def lengthOfLongestSubstring(s: str) -> int:
    i, j, ans = 0, 0, 0
    m = dict()
    while j < len(s):
        c = s[j]
        if c in m:
            ans = max(ans, j - i)
            i = max(m[c]+1, i) ## jump to the right of previously repeating one
        m[c] = j
        j += 1
    ans = max(ans, j - i)
    return ans

if __name__ == '__main__':
    print(lengthOfLongestSubstring('abcabcbb'))
    print(lengthOfLongestSubstring('bbbbb'))
    print(lengthOfLongestSubstring('pwwkew'))
    print(lengthOfLongestSubstring('dvdwb'))
    print(lengthOfLongestSubstring('a'))