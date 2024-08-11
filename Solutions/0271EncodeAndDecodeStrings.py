from typing import List


class Codec:
    def encode(self, strs: List[str]) -> str:
        '''Encodes a list of strings to a single string.
        '''
        sb = []
        for s in strs:
            sb.append(str(len(s)))
            sb.append(':')
            sb.append(s)
        return ''.join(sb)
    def decode(self, s: str) -> List[str]:
        '''Decodes a single string to a list of strings.'''
        strs = []
        i = 0
        while i < len(s):
            j = i
            while j < len(s) and s[j].isnumeric():
                j += 1
            l = int(s[i:j])
            word = s[j+1 : j + l +1]
            strs.append(word)
            i = j + l + 1
        return strs

if __name__ == '__main__':
    codec = Codec()
    print(codec.encode(['a', 'b', 'c']))