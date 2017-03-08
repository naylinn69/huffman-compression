from Queue import PriorityQueue
from copy import deepcopy

class FullBinaryTree(object):
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def merge(self, otherTree):
        self.left = deepcopy(self)
        self.freq += otherTree.freq
        self.char = None
        self.right = otherTree

    def getCodes(self):
        def helper(self, code):
            codes = []
            if self.left and self.right:
                leftCodes = helper(self.left, code+"0")
                rightCodes = helper(self.right, code+"1")
                codes += leftCodes + rightCodes
            else:
                codes += [(self.char, code)]
            return codes
        return {char: code for (char, code) in helper(self, "")}

def buildEncodingTree(char2Freq):
    pQueue = PriorityQueue()
    for char, freq in char2Freq.items():
        pQueue.put((freq, FullBinaryTree(char, freq)))
    while pQueue.qsize() > 1:
        lowestFreqTree = pQueue.get()[1]
        secLowestFreqTree = pQueue.get()[1]
        lowestFreqTree.merge(secLowestFreqTree)
        pQueue.put((lowestFreqTree.freq, lowestFreqTree))
    return pQueue.get()[1]

def countCharaters(text):
    charCount = {}
    for char in text:
        if char in charCount:
            charCount[char] += 1
        else:
            charCount[char] = 1
    return charCount
