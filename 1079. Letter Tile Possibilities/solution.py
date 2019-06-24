// 递归调用，每次添加一个新的字符，判断是否已经存在，最后统计数量，很慢
class Solution:
    res = set()
    def numTilePossibilities(self, tiles: str) -> int:
        self.res.clear()
        def helper(tiles, seq):
            for i in range(len(tiles)):
                nSeq = seq + tiles[i]
                self.res.add(nSeq)
                helper(tiles[:i]+tiles[i+1:], nSeq)
        helper(tiles,"")
        return len(self.res)
        
        
// 利用python内置的排列函数，并统计其中的不重复的数目。        
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        ans = 0
        for i in range(1,len(tiles)+1):
            a = itertools.permutations(tiles,i)
            ans += len(dict(collections.Counter(a)))
        return ans
       
       
// 还有一种纯数学方式
