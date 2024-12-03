import unittest

class Solution:
    def sub_array_sum_equals_k(self, nums: list[int], k: int) -> int:
        result = 0
        current_sum = 0
        prefix_sums = {0: 1}

        for n in nums:
            current_sum += n
            diff = current_sum - k

            result += prefix_sums.get(diff, 0)
            prefix_sums[current_sum] = 1 + prefix_sums.get(current_sum, 0)
        
        return result


class TestSubArraySum(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_basic_case(self):
        nums = [1, 1, 1]
        k = 2
        expected = 2  # [1,1] appears twice
        result = self.solution.sub_array_sum_equals_k(nums, k)
        self.assertEqual(result, expected)

    def test_with_negative_numbers(self):
        nums = [1, -1, 0, 1]
        k = 0
        expected = 4  # [-1,0], [0], [1,-1,0] sum to 0
        result = self.solution.sub_array_sum_equals_k(nums, k)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()