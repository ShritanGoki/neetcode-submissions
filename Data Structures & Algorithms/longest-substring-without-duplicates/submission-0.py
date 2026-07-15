class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        l = 0
        check = set()

        for i in range(len(s)):
            while s[i] in check:
                check.remove(s[l])
                l+=1
            check.add(s[i])
            longest = max(i-l+1, longest)
        return longest

        