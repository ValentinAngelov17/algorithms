"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution(object):
    def postorder(self, root: Node):
        """
        :type root: Node
        :rtype: List[int]
        """
        indexes = [0]
        output = []
        for i in range(len(root)):
            if root[i] is None:
                indexes.append(i)

        for x in root.children:
            pass

        last_index = len(root)
        for index in reversed(indexes):
            output.append(root[index + 1:last_index])
            last_index = index


        return


a = Solution()
print(a.postorder(root=[1, None, 3, 2, 4, None, 5, 6]))
