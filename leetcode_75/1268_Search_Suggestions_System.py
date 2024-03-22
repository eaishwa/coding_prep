"""
1268. Search Suggestions System
https://leetcode.com/problems/search-suggestions-system/description/?envType=study-plan-v2&envId=leetcode-75

What is the question?
Give autocomplete suggestions for words!

Final algorithm followed:
1. Use a Trie! As you insert words, store up to 3 words at each char node, this helps with serving the output
2. Sort products and add it Trie
3. Reach up to the prefix end char and append the words stored in that node.

Summary of common mistakes/tricks:
"""
# Solution with comments
class TrieNode:
    def __init__(self):
        self.children = {}
        self.words = []

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        r = self.root
        # insert char after char into trie
        for c in word:
            if c not in r.children:
                r.children[c] = TrieNode()
            r = r.children[c]
            # for each char, store upto 3 words with prefix until current char
            if len(r.words) < 3:
                r.words.append(word)
                
    def find_words(self, prefix):
        r = self.root
        for c in prefix:
            if c not in r.children:
                return ''
            r = r.children[c]
        # when you reach the end char of prefix, return the stored 3 words!
        return r.words

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        # sort first in order to meet the condition listed in the problem
        products.sort()
        trie = Trie()
        for p in products:
            trie.insert(p)
        print(trie.root.children)
        ans,curr = [],''
        for c in searchWord:
            curr+=c
            ans.append(trie.find_words(curr))
        return ans