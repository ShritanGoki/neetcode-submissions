class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for n in strs:
            result += str(len(n)) + "#" + n
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            j += 1
            i = j + length
            result.append(s[j:i])
        
        return result

