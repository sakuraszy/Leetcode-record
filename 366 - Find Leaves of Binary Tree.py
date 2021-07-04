# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findLeaves(self, root):
        result= list()
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        def recur(level,node):
            if node.left==node.right == None:
                if len(result)== level:
                    result.append(list())
                result[level].append(node.val)
                return level+1
            else:
                level1=0
                level2=0
                if node.left != None:
                    level1 = recur(0,node.left)
                if node.right != None:
                    level2 = recur(0,node.right)
                level = max(level1,level2)
                if len(result)==level:
                    result.append(list())
                result[level].append(node.val)
                return level+1
        recur(0,root)
        return result
            
        
        