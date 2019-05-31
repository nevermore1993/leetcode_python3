//There are 3 cases:
//    If root1 or root2 is null, then they are equivalent if and only if they are both null.
//    Else, if root1 and root2 have different values, they aren't equivalent.
//    Else, let's check whether the children of root1 are equivalent to the children of root2. 
//    There are two different ways to pair these children.

class Solution(object):
    def flipEquiv(self, root1, root2):
        if root1 is root2:
            return True
        if not root1 or not root2 or root1.val != root2.val:
            return False

        return (self.flipEquiv(root1.left, root2.left) and
                self.flipEquiv(root1.right, root2.right) or
                self.flipEquiv(root1.left, root2.right) and
                self.flipEquiv(root1.right, root2.left))
