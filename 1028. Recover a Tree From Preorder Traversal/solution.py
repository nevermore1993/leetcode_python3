// 首先将原数组分为两个数组，一个代表每个节点的值，一个代表每个节点的层级。然后根据前序遍历的规律，将层级数组分为根节点，左子树和右子树
// 以此类推，递归调用得到结果
class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        if len(S) == 0:
            return None
        if len(S) == 1:
            return TreeNode((int)(S[0]))
        
        lvl = [0]
        val = []
        #start of dashes
        sd = 0
        #start of number
        sn = 0
        for i in range(1, len(S)):
            if (S[i] == '-' and S[i-1] != '-'):
                val.append((int)(S[sn:i]))
                sd = i
            elif S[i] != '-' and S[i-1] == '-':
                lvl.append(i-sd)
                sn = i
        val.append((int)(S[sn:]))

        print(lvl, val)
        
        def helper(lvl, val):
            if len(val) == 0:
                return None
            root = TreeNode(val[0])
            if len(val) == 1:
                return root
            right = len(lvl)
            for i in range(len(lvl)):
                if lvl[i] == lvl[0] + 1 and i != 1:
                    right = i
            root.left = helper(lvl[1:right], val[1:right])
            root.right = helper(lvl[right:], val[right:])
            return root
        return helper(lvl, val)
        
        
// 同样先将原数组解析，分成一个个节点和其深度的pair的二维数组
// 然后根据深度的增加，将节点入栈，默认为左儿子。这样栈里的节点的深度是逐渐增加的。当出现一个节点的深度小于或等于栈顶节点的深度，说明
// 我们遇到了一个节点，他可能是栈顶节点的兄弟，或者是先祖的兄弟，我们就依次弹出栈顶的节点，直至找到当前节点的父节点，也就是
// 深度比其还小1的节点，然后设置为其右儿子，重复步骤
// 又没有想到使用栈。我先想到的是需要记录下前面节点的深度，如果当前节点比最后一个节点深度小，我们需要追溯到最近的一个比当前
// 节点深度还小的节点。我考虑使用递归调用，但是没有成功，而其实可以简单的使用栈来解决这个问题。
class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        if not S:
            return None
        
        split = S.split('-')
        count = 0
        depths = []
        for s in split:
            if not s:
                count += 1
            else:
                depths.append([count+1, int(s)])
                count = 0
        
        myStack = [TreeNode(depths[0][1])]
        
        for i in depths[1:]:
            while len(myStack) > i[0]:
                myStack.pop()
            newNode = TreeNode(i[1])
            if myStack[-1].left is None:
                myStack[-1].left = newNode
            else:
                myStack[-1].right = newNode
            myStack.append(newNode)
            
        return myStack[0]
