// 首先构建所有最基础的回文子串，即长度为1的和2的
// 然后在这些回文子串的基础上拓展，判断是否为回文。是的话就加入栈，下次用它为基础。
// 只要回文子串的中心点不同，那么这两个回文子串就不同。
class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        stack = []
        for i in range(len(s)):
            stack.append((i,i))
            if i+1 < len(s) and s[i] == s[i+1]:
                stack.append((i,i+1))
        
        while len(stack) > 0:
            i, j = stack.pop()
            res += 1
            if (i-1) >= 0 and (j+1) < len(s) and s[i-1] == s[j+1]:
                stack.append((i-1,j+1))
        return res
        
// 这题也可以用dp算法，dp矩阵保存所有子串的可能位置，如dp[i][j]保存s[i:j]是不是回文。然后利用dp[i+1][j-1]来判断dp[i][j]的值
// 最后得到所有子串是不是回文。但是我觉得这个方法不好，因为还判断了很多不是回文的子串。而我们从基础回文子串拓展，可以减少很多
// 不必要的判断。
// dp in java
class Solution {
    public int countSubstrings(String s) {
        int[][] is_pal = new int[s.length()][s.length()];
        char[] str = s.toCharArray();
        int total_palindromes = 0; 
        
        for(int end = 0; end < str.length; end++){
            for(int start = end; start >= 0; start--){
                is_pal[start][end] = substringIsPalindrome(start,end,str,is_pal);
                total_palindromes += is_pal[start][end];
            }
        }
        
        return total_palindromes; 
    }
    
    public int substringIsPalindrome(int start, int end, char[] s, int[][] is_pal){        
        boolean boundary_chars_differ = s[start] != s[end];
        boolean middle_not_palindrome = (s[start] == s[end]) && 
                                        (start+1) <= (end-1) &&
                                        is_pal[start+1][end-1] == 0; 
            
        return (boundary_chars_differ || middle_not_palindrome)? 0 : 1; 
    }
}
        
// 同样的思想，从长度1或者2的基础回文子串开始拓展。       
class Solution:
    def countSubstrings(self, s: str) -> int:
        
        if len(s) <= 1:
            return 1
        sLen = len(s)
        result = 0
        
        # for odd length of palindorms
        for i in range(sLen):
            # center is at i
            leftIndex = i -1
            rightIndex = i + 1
            # s[i] itself is a palindorm
            result += 1
            while leftIndex >=0 and rightIndex<sLen:
                if s[leftIndex] == s[rightIndex]:
                    result += 1
                    # update left and right index
                    leftIndex -= 1
                    rightIndex += 1
                else:
                    # if not equals, then don't need to search rest
                    break
        # for even length of palindorms
        for i in range(sLen):
            #i is the leftcenter
            leftCenter = i
            rightCenter = i+1
            while leftCenter >= 0 and rightCenter < sLen:
                if s[leftCenter] == s[rightCenter]:
                    result += 1
                    # update left and right center
                    leftCenter -= 1
                    rightCenter += 1
                else:
                    break
        return result
        
        
        
// 马拉车算法，还是不懂     
class Solution:
    def countSubstrings(self, s: str) -> int:
        def manachers(S):
            # A = '@#' + '#'.join(S) + '#$'
            t = "#".join('^{}$'.format(s))
            Z = [0] * len(t)
            c, r = 0,0
            for i in range(1, len(t) - 1):
                if i < r:
                    Z[i] = min(r - i, Z[2 * c - i])
                while t[i + Z[i] + 1] == t[i - Z[i] - 1]:
                    Z[i] += 1
                if i + Z[i] > 0:
                    c, r = i, i + Z[i]
            return Z

        return sum((v+1)//2 for v in manachers(s))
