// 通过栈来判断是不是构成了闭合的括号。然后将括号的端点坐标保存。保存时要考虑多种情况
// 1.之前没有闭合括号，直接保存
// 2.之前有闭合括号，但是不连续，直接保存
// 3.之前有闭合括号，且是连续的，拓宽之前括号的右端点
// 4.之前有闭合括号，且被当前新的括号包围，拓宽之前括号的左右端点
// 最后判断最大的括号的长度
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        maxL = []
        for i in range(len(s)):
            if not stack or s[i] == '(':
                stack.append(i)
            
            if s[i] == ')':
                if s[stack[-1]] == '(':
                    pre_index = stack.pop()
                    if len(maxL) == 0:
                        maxL.append([pre_index, i])
                    else:
                        if pre_index == maxL[-1][1] + 1:
                            maxL[-1][1] = i
                        elif pre_index == maxL[-1][0] - 1:
                            maxL[-1][0] -= 1
                            maxL[-1][1] += 1
                            if len(maxL) >= 2 and maxL[-2][1] == maxL[-1][0] - 1:
                                maxL[-2][1] = maxL[-1][1]
                                maxL.pop()
                        else:
                            maxL.append([pre_index, i])
                    continue
                else:
                    stack.append(i)
        res = lambda maxL : max((a[1] - a[0] + 1) for a in maxL) if len(maxL) != 0 else 0
        return res(maxL)


// 同样是利用栈来判断闭合。但是栈里存储的不是坐标，而是长度
// 当出现一个新的‘(’时，往栈里压入一个0，每一个0代表一个空闲的'(',当有')'出现，且有空闲的'('时，')'会与最近的空闲'('结合成一个2，
// 在这两个可以结合的'()'之间有之前已经结合了的'()'，可能是2，4，等等。将这个长度也加到刚刚合并的长度2上，得到新的长度。
// 并更新最大长度
// 单独的')'不考虑，即没有空闲的'('时出现的')'。
// 为什么要在最开始加入一个0。他这里在更新时，是将最后一个代表(的0去掉，将新合并的长度加到最后一个(之前的长度上去，并且之前的长度
// 要么是0，即之前相邻的不是一个完整的括号，要么就是2的倍数，即之前相邻的是一个完整的括号。加了一个0才能保证第一个完整的括号
// 能通过这种方法添加进栈中。
// 如果栈的长度为1，则说明之前出现的所有括号可以组成一个完整的括号，或者说之前没有出现空闲的'('。
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack=[0]
        longest=0
        for i in s:
            if i=='(':
                stack.append(0)
            else:
                if len(stack)>1:
                    val = stack.pop()
                    stack[-1]+=val+2
                    longest=max(longest,stack[-1])
                else:
                    stack=[0]
        return longest
