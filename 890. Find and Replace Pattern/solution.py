class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        result = []
        
        for word in words:
            sw = string.ascii_letters
            sp = string.ascii_letters
            if len(word) == len(pattern):
                for i in range(len(word)):
                    index1 = sw.find(word[i])
                    index2 = sp.find(pattern[i])
                    print(index1,index2)
                    if index1 < 0 and index2 >= 0 or index1 >= 0 and index2 < 0:
                        break
                    else:
                        sw = sw.replace(word[i],'')
                        sp = sp.replace(pattern[i],'')
                        if i == len(word) - 1:
                            result.append(word)
        
        return result
