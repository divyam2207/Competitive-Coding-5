"""
TC: O(N) {We traverse every node once}
SC: O(N) {We store the nodes of every level before traversing, and at worst we can have N/2 leaf nodes in the case of perfectly or near perfectly balanced binary tree}

Approach:

We start our level order traversal and at each level we assign the largest value to an arbitrary smallest possible value
and while accessing every node we check and update the largest value by comparing it to the previosuly assigned value.
After traversing the level completely, we have the largest value at that level, and we append that to our result array.

The problem ran successfully on Leetcode.
"""
# Definition for a binary tree node.
from collections import deque
from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        q = deque([root])
        res = []
        while q:
            largest = float('-inf')
            for _ in range(len(q)):

                node = q.popleft()
                largest = max(largest, node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(largest)
        
        return res