// 将人按照身高从高到低排序，相同高度的人，对人数按从低到高排序。然后依次将人按照它的人数作为索引，插入到列表中。
// 因为我们是按照身高从高到低排序的，所以每次插入新的人时，列表中的所有人都会比新的人要高或相等。那么只需要按照它的人数插入到
// 对应的位置就可以了
class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        people = sorted(people, key = lambda x: (-x[0], x[1]))
        res = []
        for p in people:
            res.insert(p[1], p)
        return res
        
        
        
        
// 按照身高从低到高排序，人数从高到底排序。因为列表中已经存在的人肯定比新插入的人要矮或相等，我们需要在这个插入的位置前面留出k个空位。
// 因为之前已经有些位置被占据了，所以我们要计算的是空位。
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key = lambda x: [x[0], -x[1]])
        
        ans = [None] * len(people)
        
        for h, k in people:
            cnt = 0
            for i in range(len(people)):
                if ans[i] is None:
                    cnt += 1
                    
                    if cnt == k + 1:
                        ans[i] = [h, k]
                        break
                    
        return ans
