class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = {}
        freq = [[] for i in range(len(nums))]
        print(freq, len(freq))

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        print(count)
        for n, c in count.items():
            freq[c].append(n)
        print(freq)

        res = []
        for n in range(len(freq) - 1, 0, -1): #(5,0,-1)
            print(n)
            for i in freq[n]:
                print(i, freq[n])
                res.append(i)
                if len(res) == k:
                    return res

    
# test
obj = Solution()
nums = [1,1,1,2,2,3]
k = 2
result = obj.topKFrequent(nums, k)
print(result)