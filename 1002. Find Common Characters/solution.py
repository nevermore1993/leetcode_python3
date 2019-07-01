// 统计每个词的字母的次数，遇到下一个词，比较其中是否有相同的字母，然后取最少的次数。不考虑新出现的字母。
from collections import Counter
class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        dic = Counter(A[0])
        for word in A[1:]:
            temp = Counter(word)
            for key in dic:
                dic[key] = min(dic[key], temp[key])
        res = []
        for item in dic.items():
            for i in range(item[1]):
                res.append(item[0])
        return res
        
        
// 先取出A中所有的字母，统计每个字母在每个词中出现的次数，取最小的次数。在某些词中没出现的就是次数0
class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        uniqueChars=set(''.join(A))
        common=[]
        for i in uniqueChars:
            count=min([x.count(i) for x in A])
            common=common+[i]*count
        return common
