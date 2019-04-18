# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

//函数输出的是N个节点时所有的完全二叉树，那么我们就对左右节点分别考虑去掉根节点后还剩下N-1个节点，将他们分别赋给左右子树，
//则有range（1，N-1，2）种情况然后返回对应节点数目时所有的完全二叉树的列表。将所有匹配赋值给左右子树只有一个问题，我第一次得到的结果
//所有的树都相同，是因为我只用了一个root节点当我将root添加到result中，之后又对root进行了修改，已经添加到result中的也会被修改，得到的结果
//就是result中的所有元素都一样，因为他们本来就都是同一个root
class Solution(object):
    def allPossibleFBT(self, N):
        """
        :type N: int
        :rtype: List[TreeNode]
        """
        result = []
        root = TreeNode(0)
        if N == 1:
            result.append(root)
            return result
        if N == 3:
            root.left = TreeNode(0)
            root.right = TreeNode(0)
            result.append(root)
            return result
        for i in range(1,N-1,2):
            left = self.allPossibleFBT(i)
            right = self.allPossibleFBT(N-1-i)
            for l in left:
                for r in right:
                    root = TreeNode(0)
                    root.right = r
                    root.left = l
                    result.append(root)
        return result
        


//使用了动态规划，cache保存对应节点数时的完全二叉树列表，然后对新的节点数，通过在前面的cache中查找对应的左右子树节点
//数的可能性，得到结果。思想与我的方法一样，不过它使用的是动态规划，而不是像我一样使用递归调用。
//我的递归调用的问题在于，对于低节点数的完全二叉树要重复计算很多次，而动态规划方法会将已经计算过的节点保存下来，节省了时间。
class Solution(object):
    def allPossibleFBT(self, N):
        """
        :type N: int
        :rtype: List[TreeNode]
        """
        
        cache = {}
        
        if N %2 == 0:
            return []
        cache[1] = [TreeNode(0)]
        
        for i in range(3, N+1 ,2):
            cache[i] = []
            for left_size in range(1, i-1,2):
                right_size = i-left_size - 1
                left_list = cache[left_size]
                right_list = cache[right_size]
                for left in left_list:
                    for right in right_list:
                        node = TreeNode(0)
                        node.left = left
                        node.right = right
                        cache[i].append(node)
                        
        return cache[N]
