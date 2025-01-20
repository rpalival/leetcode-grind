import tracemalloc

tracemalloc.start()
class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()
 
    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.word = True

    def search(self, word: str) -> bool:
        def dfs(j, root):
            cur = root

            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    for child in cur.children.values():
                        if dfs(i+1, child):
                            return True
                        return False
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
            return cur.word
        return dfs(0, self.root)


current, peak = tracemalloc.get_traced_memory()

print(f"Current Memory Usage: {current / 10**6:.2f} MB")
print(f"Peak Memory Usage: {peak / 10**6:.2f} MB")
# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

import unittest

class TestWordDictionary(unittest.TestCase):
    def setUp(self):
        self.wordDictionary = WordDictionary()

    def test_word_dictionary(self):
        self.wordDictionary.addWord("bad")
        self.wordDictionary.addWord("dad")
        self.wordDictionary.addWord("mad")
        
        self.assertFalse(self.wordDictionary.search("pad"))  # should return False
        self.assertTrue(self.wordDictionary.search("bad"))   # should return True
        self.assertTrue(self.wordDictionary.search(".ad"))   # should return True
        self.assertTrue(self.wordDictionary.search("b.."))   # should return True

if __name__ == '__main__':
    unittest.main()
tracemalloc.stop()