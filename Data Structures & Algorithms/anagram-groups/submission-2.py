class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        subL = defaultdict(list)

        for word in strs:
            counts = [0] * 26
            for i in word:
                counts[ord(i) - ord('a')] += 1
            subL[tuple(counts)].append(word)
        
        return list(subL.values())
