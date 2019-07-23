// 遍历字符串，按照字母出现的顺序，将每个字母的起始和终止位置保存在字典中，再遍历字典，合并所有overlap的窗口。因为是按照字母出现的顺序的，所以如果
// 后面出现的字母的起始位置比上一个最大窗口的结束位置要大，则说明这个新的字母是新的窗口的开始。整体只用两次遍历，时间复杂度为O(n)

class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        charSet = set()
        charDict = dict()
        res = []
        for i in range(len(S)):
            if S[i] not in charSet:
                charSet.add(S[i])
                charDict[S[i]] = [i, i]
            else:
                charDict[S[i]][1] = i
        temp = [0, 0]
        for key in charDict:
            if charDict[key][0] <= temp[1]:
                temp[1] = max(charDict[key][1],temp[1])
            else:
                res.append(temp[1] - temp[0] + 1)
                temp = charDict[key]
        res.append(temp[1] - temp[0] + 1)
        return res

    
// 首先找出包含第一个字母的最小子串，然后对其中的所有字母遍历，逐渐拓展这个子串，直到无法拓展为止。然后重复这个步骤
class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        res = []
        
        maxCutOff = 0
        count = 0
        
        start = 0
        revS = S[::-1]
        lastPos = 0
        
        while start < len(S):
            currChar = S[start]
            lastPos = max(lastPos, len(S) - revS.index(currChar))
            newLastPos = False
            
            # Find max last index of substring
            subString = S[start:lastPos]
            charSet = set(subString)
            for character in charSet:                    
                if len(S) - revS.index(character) > lastPos:
                    lastPos = len(S) - revS.index(character)
                    newLastPos = True
                    break
                    
            if not newLastPos:
                res.append(len(subString))
                start = lastPos
        return res
