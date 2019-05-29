// solve(node)返回的是从node到N-1的路径，从0开始的路径应该是0加上0的所有邻居节点到N-1的路径，递归得到。
class Solution(object):
    def allPathsSourceTarget(self, graph):
        N = len(graph)

        def solve(node):
            if node == N-1: return [[N-1]]
            ans = []
            for nei in graph[node]:
                for path in solve(nei):
                    ans.append([node] + path)
            return ans

        return solve(0)
