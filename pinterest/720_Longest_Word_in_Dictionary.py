"""
720. Longest Word in Dictonary
https://leetcode.com/problems/longest-word-in-dictionary/description/

What is the question?
Create a Trie! Insert words into it and keep track of the longest word with constraints met.

Final algorithm followed:
1. Create a Trie
2. Sort words, insert into trie
3. Keep track of longest valid word as you insert
4. Return answer after all words are ingested in

Summary of common mistakes/tricks:
"""
# Solution with comments
class TrieNode:
    def __init__(self):
        self.children = {}
        self.iseow = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.lw = ''

    def insert(self, word):
        r = self.root
        count = 0
        for c in word:
            if c not in r.children:
                r.children[c] = TrieNode()
            r = r.children[c]
            # if end of an existing word, increment count
            if r.iseow:
                count += 1
        r.iseow = True
        # if count+1 = len(word), then it means we could incrementally build the current word from existing words in the list
        if count+1 == len(word) and count+1 > len(self.lw):
            self.lw = word

    def findlw(self):
        return self.lw

class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        words.sort()
        trie = Trie()
        for word in words:
            trie.insert(word)
        return trie.findlw()