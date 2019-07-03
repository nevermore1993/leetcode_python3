class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = []
        for i in range(1,n+1):
            if i%15==0:
                res.append('FizzBuzz')
            elif i%5==0:
                res.append('Buzz')
            elif i%3==0:
                res.append('Fizz')
            else:
                res.append(str(i))
        return res
        
        
        
// 每个循环只计算了两次求余，比上面的方法要快一些       
class Solution:
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # ans list
        ans = []
        for num in range(1,n+1):
            divisible_by_3 = (num % 3 == 0)
            divisible_by_5 = (num % 5 == 0)
            if divisible_by_3 and divisible_by_5:
                # Divides by both 3 and 5, add FizzBuzz
                ans.append("FizzBuzz")
            elif divisible_by_3:
                # Divides by 3, add Fizz
                ans.append("Fizz")
            elif divisible_by_5:
                # Divides by 5, add Buzz
                ans.append("Buzz")
            else:
                # Not divisible by 3 or 5, add the number
                ans.append(str(num))
        return ans
