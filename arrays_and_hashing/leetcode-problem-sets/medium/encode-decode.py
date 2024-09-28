class Solution:

    def encode(self, strs: list[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> list[str]:
        res, i = [], 0
        # iterate the entire length of string
        while i < len(s):
            j = i
            # inner pointer to grab the length we encoded
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            res.append(s[j+1 : j+1+length])
            i = j + 1 + length
        return res
    
    # test
obj = Solution()
strs = ["raj","loves","coding","and","cunts"]
encString = obj.encode(strs)
decString = obj.decode(encString)
print(encString, decString)