import heapq, unittest
from collections import Counter, deque
class Solution:
    def least_interval(self, tasks: list[int], n: int) -> int:
        count = Counter(tasks)
        max_heap = [-cnt for cnt in count.values()]
        heapq.heapify(max_heap)

        time = 0
        task_queue = deque() # [-cnt, idle time] pair

        while max_heap or task_queue:
            time += 1
            if max_heap:
                cnt = 1 + heapq.heappop(max_heap)
                if cnt:
                    task_queue.append([cnt, time+n])
            if task_queue and task_queue[0][1] == time:
                heapq.heappush(max_heap, task_queue.popleft()[0])
        return time
    

class TestTaskScheduler(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_least_interval(self):
        tasks = ["A", "A", "A", "B", "B", "B"]
        n = 2
        expected = 8  # A -> B -> idle -> A -> B -> idle -> A -> B
        result = self.solution.least_interval(tasks, n)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()