// Let dp(i, j) be the largest score Alex can achieve where the piles remaining are piles[i], piles[i+1], ..., piles[j].
// When the piles remaining are piles[i], piles[i+1], ..., piles[j], the player who's turn it is has at most 2 moves.

// The person who's turn it is can be found by comparing j-i to N modulo 2.

// If the player is Alex, then she either takes piles[i] or piles[j], increasing her score by that amount. 
// Afterwards, the total score is either piles[i] + dp(i+1, j), or piles[j] + dp(i, j-1); and we want the maximum possible score.

// If the player is Lee, then he either takes piles[i] or piles[j], decreasing Alex's score by that amount. 
// Afterwards, the total score is either -piles[i] + dp(i+1, j), or -piles[j] + dp(i, j-1); and we want the minimum possible score.


from functools import lru_cache

class Solution:
    def stoneGame(self, piles):
        N = len(piles)

        @lru_cache(None)
        def dp(i, j):
            # The value of the game [piles[i], piles[i+1], ..., piles[j]].
            if i > j: return 0
            parity = (j - i - N) % 2
            if parity == 1:  # first player
                return max(piles[i] + dp(i+1,j), piles[j] + dp(i,j-1))
            else:
                return min(-piles[i] + dp(i+1,j), -piles[j] + dp(i,j-1))

        return dp(0, N - 1) > 0
        
        
        
//Alex clearly always wins the 2 pile game. With some effort, we can see that she always wins the 4 pile game.

//If Alex takes the first pile initially, she can always take the third pile. If she takes the fourth pile initially, 
//she can always take the second pile. At least one of first + third, second + fourth is larger, so she can always win.

//We can extend this idea to N piles. Say the first, third, fifth, seventh, etc. piles are white, and the second, 
//fourth, sixth, eighth, etc. piles are black. Alex can always take either all white piles or all black piles, 
//and one of the colors must have a sum number of stones larger than the other color.

class Solution:
    def stoneGame(self, piles):
        return True
