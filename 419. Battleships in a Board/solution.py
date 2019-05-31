// 如果发现了一个'X',当这个X不是这艘船的第一个X时，就不给总数加一。如何判断这个X是不是第一个X，只要它的左边和上边(如果存在的话)不是X，那么这个
// X就是第一个，反之这个就不是第一个X。
class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        res = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'X':
                    if i - 1 >= 0 and j - 1 >= 0:
                        if board[i-1][j] != 'X' and board[i][j-1] != 'X':
                            res += 1
                    elif i - 1 >= 0:
                        if board[i-1][j] != 'X':
                            res += 1
                    elif j - 1 >= 0:
                        if board[i][j-1] != 'X':
                            res += 1
                    else:
                        res += 1
        return res
        
// 判断这个X是不是这艘船的最后一个X，同理，这个X的右边或下面(如果存在的话)不是X，就说明这个X是最后一个X    
class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        ships = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'X':
                    if i+1 < len(board): # check for bounds
                        if board[i+1][j] == 'X': # If X is found, the ship is continued
                            continue
                    if j+1 < len(board[0]): # check for bounds
                        if board[i][j+1] == 'X': # If X is found, the ship is coninued
                            continue
                    ships += 1
        return ships
