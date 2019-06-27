class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = []
        def helper(i):
            temp = i
            while temp != 0:
                digit = temp % 10
                if digit == 0:
                    return False
                elif i%digit != 0:
                        return False
                else:
                    temp = temp // 10
            return True
        
        for i in range(left,right+1):
            if helper(i):
                res.append(i)
        return res
