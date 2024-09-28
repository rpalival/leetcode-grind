from collections import defaultdict


def validAnagram(s, t):
    if len(s) != len(t):
        return False
    
    countS = defaultdict(int)
    countT = defaultdict(int)
    # countS = {}
    # countT = {}

    for i in range(len(s)):
        countS[s[i]] += 1
        countT[t[i]] += 1
        # countS[s[i]] = 1 + countS.get(s[i], 0)
        # countT[t[i]] = 1 + countT.get(t[i], 0)

    return countS == countT
    


# test
print(validAnagram("raj", "jar"))
# print(ord("😂"))