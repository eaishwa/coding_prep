"""
208. Implement Trie
https://leetcode.com/problems/implement-trie-prefix-tree/?envType=study-plan-v2&envId=leetcode-75

What is the question?
Create a Trie!

Final algorithm followed:
1. Use a new DS with hashmap of children and accompanying isendofword boolean.
2. The hashmap's key is character, value is its children's TrieNode object.
3. As you proceed child after child, you traverse the trie.

Summary of common mistakes/tricks:
"""
# Solution with comments
class TrieNode:
    # declare a class with hashmap for children
    # add a boolean flag to denote end of word
    def __init__(self):
        self.children = {}
        self.isendofword = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        r = self.root
        # for each char, if it is not in Trie
        for c in word:
            if c not in r.children:
                # create a child trie node
                r.children[c] = TrieNode()
            # update the next node
            r = r.children[c]
        r.isendofword = True

    def search(self, word: str) -> bool:
        r = self.root
        # search character by character in the Trie
        for c in word:
            if c not in r.children:
                return False
            r = r.children[c]
        if r.isendofword:
            return True
        return False
    
    def startsWith(self, prefix: str) -> bool:
        r = self.root
        for c in prefix:
            if c not in r.children:
                return False
            r = r.children[c]
        return True
        
# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)