// 由于后面的元素需要与前面相邻的元素互动，并且还要记录删除后剩下的位置，那么自然想到使用 栈
// 每次添加新元素的时候就判断一下栈尾是否右k个重复的元素，是的话就删除，不是的话继续
// 一开始我想到使用collections.Counter()来判断栈尾是否k个重复的元素，但是这样太慢
// 然后想到在每次添加元素的时候就记录重复的次数，如果添加的元素与栈尾元素相同，则新添加的元素的重复次数就是栈尾元素重复次数+1
// 如果不同，则新添加元素的重复次数就是1，然后判断栈尾元素的重复次数是不是k

// 因为后添加的元素对之前添加的元素的出现次数没有影响，所以可以使用这样的方法来存储

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        import collections
        stack = []
        for i in s:
            # 如果是第一个元素，重复次数为1
            if len(stack) == 0:
                stack.append((i,1))
            # 否则判断该元素与栈尾元素是否相同
            else:
                # 如果相同，重复次数为栈尾的次数加1
                if i == stack[-1][0]:
                    stack.append((i,stack[-1][1]+1))
                # 不同，则为1
                else:
                    stack.append((i,1))
            # 去掉栈尾k个重复元素
            if stack[-1][1] == k:
                stack = stack[:-k]
        return ''.join([i[0] for i in stack])
