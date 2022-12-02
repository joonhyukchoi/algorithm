from collections import defaultdict

class TrieNode:
    def __init__ (self):
        self.word_id = -1
        self.palindrome_word_ids = []
        self.children = defaultdict(TrieNode)

class Trie:
    def __init__ (self):
        self.root = TrieNode()

    @staticmethod
    def is_palindrome(word: str) -> bool:
        return word[::] == word[::-1]
    
    def insert(self, index: int, word: str) -> None:
        node = self.root
        for i, w in enumerate(reversed(word)):
            if self.is_palindrome(word[0 : len(word) - i]):
                node.palindrome_word_ids.append(index)
            node = node.children[w]
        node.word_id = index
    
    def search(self, index, word: str) -> List[List[int]]:
        result = []
        node = self.root
        
        while word:
            if node.word_id >= 0:
                if self.is_palindrome(word):
                    result.append([index, node.word_id])
            if not word[0] in node.children:
                return result
            node = node.children[word[0]]
            word = word[1:]
        
        if node.word_id >= 0 and node.word_id != index:
            result.append([index, node.word_id])
        
        for palindrome_word_id in node.palindrome_word_ids:
            result.append([index, palindrome_word_id])
        
        return result
    

class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        trie = Trie()

        for i, word in enumerate(words):
            trie.insert(i, word)
        
        results = []
        for i, word in enumerate(words):
            results.extend(trie.search(i, word))

        return results