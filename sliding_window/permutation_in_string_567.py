class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #edge case:
        if len(s1) > len(s2):
            return False
        
        #create s1, s2 arrays of size 26
        s1Count = [0] * 26
        s2Count = [0] * 26

        #iterate s1 and count the characters
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1

        matches = 0

        for i in range(26):
            matches += (1 if s1Count[i] == s2Count[i] else 0)

        #window
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26: return True

            #right end (expanding)
            index = ord(s2[r]) - ord('a')
            s2Count[index] += 1

            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index]+1 == s2Count[index]:
                matches -= 1
            
            #left end (shrinking)
            index = ord(s2[l]) - ord('a')
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1
            l += 1
        return matches == 26


obj = Solution()
s1 = "ab"
s2 = "eidbaooo"
result = obj.checkInclusion(s1, s2)
print(result)