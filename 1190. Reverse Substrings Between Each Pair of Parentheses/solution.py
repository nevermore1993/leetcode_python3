// 使用栈，顺序将字符串入栈，如果发现')'，就可以开始往前遍历，将与这个右括号匹配的左括号之间的所有字符串输出，逆序后再入栈。
// 一次这个操作就可以将最中间的括号中的字符串翻转。然后重复这个操作
class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for c in s:
            if c == '(':
                stack.append(c)
            elif c == ')':
                temp = []
                while stack:
                    c = stack.pop()
                    if c == '(':
                        break
                    else:
                        temp += c
                # temp = temp[::-1]
                stack += temp
            else:
                stack.append(c)
        return ''.join(stack)
