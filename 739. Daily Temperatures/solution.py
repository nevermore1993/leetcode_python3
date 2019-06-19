// 从最后一个开始遍历，记录下这个温度出现的索引。当我们遇到一个新的温度时，在比这个温度大的温度中找最小的索引。如果有比这个温度大的，
// 那么最小的索引就是最近的距离。如果没有，说明不能变暖。然后将新的温度的索引更新。可能会覆盖已经出现的温度，但是无所谓，因为我们要找的
// 是最近的距离。由于是从后往前遍历，那么所有出现过的温度就是所有可能的情况。
class Solution(object):
    def dailyTemperatures(self, T):
        nxt = [float('inf')] * 102
        ans = [0] * len(T)
        for i in xrange(len(T) - 1, -1, -1):
            #Use 102 so min(nxt[t]) has a default value
            warmer_index = min(nxt[t] for t in xrange(T[i]+1, 102))
            if warmer_index < float('inf'):
                ans[i] = warmer_index - i
            nxt[T[i]] = i
        return ans
        
        

// 如果栈是空的，将当前索引入栈；如果栈不是空的，如果当前温度比栈顶的温度高，则说明栈顶的温度可以变暖，pop，循环。
// 如果当前温度比栈顶温度低，说明这个温度不能让栈里的温度变暖，push
// 栈里存放的温度，从顶向低逐渐变高，且按照列表排列的顺序。是所有还没有变暖的温度。出现新的温度，与栈里所有的温度比较，就能够得到对应的
// 天数。
// 遍历时需要保存已经遍历了的天数的温度，并且新的温度需要跟之前的所有温度对比(其实并不需要与所有的温度对比，所有已经变暖的温度是不需要
// 存放在栈中的)
// 开始我没有考虑到使用栈，我想到的是保存第一个没有变暖的索引curr，遍历之后的温度，每遇到一个新的温度，需要将其与curr之后所有的温度比较。
// 我没有想到将变暖了的温度删除，这样就不用与所有的温度比较了，也没有这个必要。
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack = []
        ans = [0]*len(T)
        for i, temperature in enumerate(T):
            while stack and T[stack[-1]] < temperature:
                prev_t_idx = stack.pop() 
                ans[prev_t_idx] = i - prev_t_idx
            stack.append(i)
        return ans
