// 使用队列来保存所有的请求，先进先出
class RecentCounter:

    def __init__(self):
        self.call = collections.deque()
        self.size = 0

    def ping(self, t: int) -> int:
        self.call.append(t)
        self.size += 1
        while self.call[0] < t-3000:
            self.call.popleft()
            self.size -= 1
        return self.size


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
