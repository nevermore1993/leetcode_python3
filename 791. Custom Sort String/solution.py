// 将S中的字符按顺序提取出来作为字典的key，遍历T，如果是S中的字符就给对应key的value加1，如果是S中没有的字符，就添加到另外的一个字符串中
// 最后按照key的value，即这个key的出现次数重新构造字符串，再与没出现在S中的字符串组合就行了
class Solution:
    def customSortString(self, S: str, T: str) -> str:
        count = {}
        noShow = ''
        show = ''
        for c in S:
            count.update({c:0})
        for c in T:
            if c in count:
                count[c] += 1
            else:
                noShow += c
        for key in count:
            show += key * count[key]
        return show + noShow
