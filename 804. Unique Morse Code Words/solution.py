class Solution:
    def uniqueMorseRepresentations(self, words: 'List[str]') -> 'int':
        result = set()
        code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        for word in words:
            s = ""
            for i in word:
                s += code[ord(i) - ord("a")]
            result.add(s)
        return len(result)
            
