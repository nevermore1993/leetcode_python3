// 增加从0开始，每次加1，减少从N开始，每次减少一，这样增加的和减少的结果就不会相同。当前为I时，该位放start。如果下一位是D，放end
// 很明显，end永远大于start，因为一个从N开始减少，一个从0开始增加。如果下一位还是I，放start+1，start+1>start。同理，如果是D的话，
// 就放end
class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        start = 0
        end = len(S)
        arr = []

        for d in S:
            if d == 'I':
                arr.append(start)
                start += 1
            else:
                arr.append(end)
                end -= 1
        
        return arr + [start]
