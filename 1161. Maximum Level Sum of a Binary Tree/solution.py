// 使用队列实现广度遍历。重点在于记录每一层的节点数目。每弹出一个节点时，先完成子节点的进队，然后要减小count，当count
// 变为0时，我们知道这一层已经遍历结束，更新各个变量，统计队列的大小，作为下一层的总count
// 直至队列为空，说明遍历完成
// 但是这个方法很耗时间，是因为队列操作太耗时间了吗？
from queue import Queue
class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        if not root:
            return 1
        max_sum = 0
        temp_sum = 0
        current_lvl = 1
        res = 1
        stack = Queue()
        stack.put(root)
        count = 1
        while not stack.empty():
            node = stack.get()
            if node.left:
                stack.put(node.left)
            if node.right:
                stack.put(node.right)
            count -= 1
            print(node.val)
            temp_sum += node.val
            if count == 0:
                if temp_sum > max_sum:
                    res = current_lvl
                    max_sum = temp_sum
                temp_sum = 0
                current_lvl += 1
                count = stack.qsize()
        return res
        
// 简单的使用一个列表，保存每一层的所有节点，遍历列表中的所有节点，将他们的子节点加入到新的列表中，依次循环    
class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        level = 1
        res, resLevel = 0, 1
        bfs = [root]
        while bfs:
            bfs2 = []
            cur = 0
            for node in bfs:
                if node.left: bfs2.append(node.left)
                if node.right: bfs2.append(node.right)
                cur += node.val
            if cur > res:
                res, resLevel = cur, level
            level += 1
            bfs = bfs2
        return resLevel
