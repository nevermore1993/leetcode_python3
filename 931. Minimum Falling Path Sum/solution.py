// dp问题。要一层一层的考虑，dp[][]就是原数组的大小，每个位置代表当前位置能够达到的最小值。而这个最小值是由它上一层的相邻三个值决定的。
// 对于边界的点，只有两个相邻值。一层一层遍历下来，就能得到最后一层每个位置最小的值了。然后取出其中最小的。
// 题目要的是路径走到最后一层的时候，能够得到的最小值。那么这个可能的位置就有A的列长度个。其中每个位置的最小值都是由其上一层相邻节点的最小值决定的。
// 所以要这样设计dp矩阵。
// dp问题只要找到子问题是什么就好解决了。也就是如何设计dp矩阵，dp矩阵每个元素的含义。
class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        for i in range(1, len(A)):
            for j in range(len(A[0])):
                if j == 0:
                    A[i][j] += min(A[i-1][j],A[i-1][j+1])
                elif j == len(A[0]) - 1:
                    A[i][j] += min(A[i-1][j-1],A[i-1][j])
                else:
                    A[i][j] += min(A[i-1][j-1],A[i-1][j],A[i-1][j+1])
        return min(A[-1])
