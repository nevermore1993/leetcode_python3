class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        t = text.split(" ")
        res = []
        for i in range(len(t)-2):
            if t[i] == first:
                if t[i+1] == second:
                    res.append(t[i+2])
        return res
        
        
        
        
class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        words = text.split()
        
        idx = []
        for i, word in enumerate(words):
            if word == first and i+1 < len(words) and words[i+1] == second:
                idx.append(i+2)
        
        return [words[i] for i in idx if i < len(words)]
