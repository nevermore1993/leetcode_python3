// 使用栈。如果是(就入栈，如果是第一个入栈的(,记录下其位置。如果是)就将栈顶弹出。弹出后，若栈为空，则说明遇到了一个完整的primitive
// 记录下这个终止位置，start和end中间的就是我们要的一个去掉头尾的结果
// 遍历整个字符串，可以找到所有的结果
class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        stack = []
        start, end = 0, 0
        res = ""
        for i in range(len(S)):
            if len(stack) == 0:
                start = i
                stack.append(S[i])
            else:
                if S[i] == '(':
                    stack.append(S[i])
                else:
                    stack.pop()
                    if len(stack) == 0:
                        end = i
                        res += S[start+1:end]
        return res
        
        
// 因为题目说了所有的括号都是合法的，所以不必使用栈的方式来判断什么时候组合成了一个合法的括号。只需要统计 ( 和 ) 的数量就可以知道什么时候
// 出现了一个完整的括号。省去了很多步骤。但是这种方法只适用于所有的括号都是合法的前提，否则")("这样的括号组合也会被识别。
class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        d = {}
        d["("] = 0
        d[")"] = 0
        A = ""
        r = ""
        for c in S:
            d[c] += 1
            A = A + c
            if d["("] == d[")"]:
                r = r + A[1:-1]
                A = ""
        return r
