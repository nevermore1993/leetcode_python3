#import Queue
// 使用反向构造的方法。从最后排好序的结果往回放。首先是将第一张牌（最大的一张）放回牌组，然后每次将牌放回牌组之前
// 要将牌组最下面的一张牌先拿到最上面（因为正序是拿走第一张牌，然后将下面一张牌放到牌组的最下面）
// 我使用queue来构造要比使用list构造慢一倍
class Solution(object):
    
    def deckRevealedIncreasing(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        """
        deck.sort(reverse=True)
        #q = Queue.Queue()
        q = []
        for d in deck:
            if len(q) == 0:
                #q.put(d)
                q.insert(0,d)
            else:
                '''
                t = q.get()
                q.put(t)
                q.put(d)
                '''
                t = q.pop()
                q.insert(0,t)
                q.insert(0,d)
        '''
        result = [0] * len(deck)
        for i in range(len(result)-1,-1,-1):
            result[i] = q.get()
        return result
        '''
        return q
        
        
// 使用正向构造的方法。index代表原本牌组每张牌的顺序，然后对这个顺序进行题目所示的操作，拿出第一张牌，
// 也就是 index.popleft() ，那这张牌就对应排好序的牌组从下往上取的牌。然后将下一张牌放到最下面，
// 也就是 index.append(index.popleft()) 。
// 这种思想是，题目要求我构造出原本的牌组，那么我们不知道牌组的具体排列，但是按照题目要求的步骤，
// 我们能知道每次取出的是原本牌组的哪一个位置的牌，然后按照抽牌结果（顺序排序的牌组），
// 就能知道每次取出的对应位置的是哪一张牌，就得到了答案。
class Solution(object):
    def deckRevealedIncreasing(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        """
        """
        simulation. 
        pop [0, 1, 2.. ]   [0, 2, 4]
        then we know the smallest need to be at position
        """
        N = len(deck)
        index = collections.deque(range(N))
        ret = [None]*N
        for card in sorted(deck):
            ret[index.popleft()] = card
            if index:
                index.append(index.popleft())
        return ret
