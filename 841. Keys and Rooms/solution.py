// 简单的递归，res是全局变量，凡是找到了key，就将res[key]置为1，然后对rooms[key]进行同样的操作
// 注意对于已经访问过的房间要停止使用该房间的钥匙，否则可能会进入死循环，即两个房间的钥匙可以互相打开
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        res = [0] * len(rooms)
        res[0] = 1
        
        def visit(rooms, keys):
            for r in keys:
                if res[r] == 1:
                    continue
                else:
                    res[r] = 1
                    visit(rooms, rooms[r])
        
        visit(rooms, rooms[0])
        print(res)
        return collections.Counter(res)[1] == len(rooms)
        
// 深度遍历，跟我的方法没什么区别
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        if rooms is None or len(rooms) == 0:
            return False
        visited = [False] * len(rooms)
        self.dfs(rooms, 0, visited)
        return all(visited)
    def dfs(self, rooms, cur_room, visited):
        visited[cur_room] = True
        for key in rooms[cur_room]:
            if not visited[key]:
                self.dfs(rooms, key, visited)
                
// 使用堆，将待访问的房间的钥匙放在堆中，每次访问就pop，获得的新key就push
class Solution(object):
    def canVisitAllRooms(self, rooms):
        seen = [False] * len(rooms)
        seen[0] = True
        stack = [0]
        #At the beginning, we have a todo list "stack" of keys to use.
        #'seen' represents at some point we have entered this room.
        while stack:  #While we have keys...
            node = stack.pop() # get the next key 'node'
            for nei in rooms[node]: # For every key in room # 'node'...
                if not seen[nei]: # ... that hasn't been used yet
                    seen[nei] = True # mark that we've entered the room
                    stack.append(nei) # add the key to the todo list
        return all(seen) # Return true iff we've visited every room

