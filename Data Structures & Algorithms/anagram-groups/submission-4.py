class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        subList = defaultdict(list)

        for i in strs:
            countS = [0] * 26
            for c in i:
                countS[ord(c) - ord('a')] += 1
            subList[tuple(countS)].append(i)
        
        return list(subList.values())
