// 这题我开始以为是用某种加密解密算法来加密。但是解法是将longURL和随机生成的shortURL作为字典保存在solution的类中，并不存在加解密算法，只有映射。
// 这种是用随机生成的6位字符串作为URL的映射
class Codec:

    alphabet = string.ascii_letters + '0123456789'
    
    def __init__(self):
        self.url2code = {}
        self.code2url = {}
        
    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        while longUrl not in self.url2code:
            code = ''.join(random.choice(Codec.alphabet) for _ in range(6))
            if code not in self.code2url:
                self.code2url[code] = longUrl
                self.url2code[longUrl] = code
        return 'http://tinyurl.com/' + self.url2code[longUrl]
        

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        return self.code2url[shortUrl[-6:]]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url)




// 这种是用URL添加的顺序来作为URL的映射，第一个添加的URL就是0，第二个就是1，以此类推，URL与顺序一一对应
class Codec:
    def __init__(self):
        self.dic = {}
        self.counter = 0

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        if longUrl not in self.dic:
            shortUrl="http://tinyurl.com/{}".format(str(self.counter))
            self.dic[longUrl] = shortUrl
            self.dic[shortUrl] = longUrl
            self.counter +=1
            return shortUrl
        else:
            self.dic[longUrl]
        
        

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        return self.dic[shortUrl]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))

