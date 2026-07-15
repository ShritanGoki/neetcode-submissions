class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count1 = {}
        for i in range (len(s1)):
            count1[s1[i]] = 1 + count1.get(s1[i], 0)
        
        totalNeed = len(count1)

        for i in range (len(s2)):
            count2 = {}
            check = 0
            for j in range (i, len(s2)):
                count2[s2[j]] = 1 + count2.get(s2[j], 0)

                if count2.get(s2[j], 0) > count1.get(s2[j], 0):
                    break
                if count2.get(s2[j], 0) == count1.get(s2[j], 0):
                    check += 1
                if totalNeed == check:
                    return True 
        return False
