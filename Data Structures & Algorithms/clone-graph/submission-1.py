"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None

        stk = [node]
        o_to_n = {}

        while stk:
            current = stk.pop()
            
            if current in o_to_n:
                continue

            o_to_n[current] = Node(current.val)

            for neighbor in current.neighbors: 
                if neighbor not in o_to_n:
                    stk.append(neighbor)

        for original in o_to_n:
            for neighbor in original.neighbors:
                o_to_n[original].neighbors.append(o_to_n[neighbor])

        return o_to_n[node]