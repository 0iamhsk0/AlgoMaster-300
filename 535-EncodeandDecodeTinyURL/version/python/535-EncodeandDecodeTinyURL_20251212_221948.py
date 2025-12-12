# Last updated: 12/12/2025, 10:19:48 PM
1class Codec:
2    def __init__(self):
3        self.encodemap = {}
4        self.decodemap = {}
5        self.base = "https://tinyurl.com/"
6
7    def encode(self, longUrl: str) -> str:
8        """Encodes a URL to a shortened URL.
9        """
10        if longUrl not in self.encodemap:
11            shortUrl = self.base + str(len(self.encodemap) + 1)
12            self.encodemap[longUrl] = shortUrl
13            self.decodemap[shortUrl] = longUrl
14        return self.encodemap[longUrl]        
15
16    def decode(self, shortUrl: str) -> str:
17        """Decodes a shortened URL to its original URL.
18        """
19        return self.decodemap[shortUrl]
20
21        
22
23# Your Codec object will be instantiated and called as such:
24# codec = Codec()
25# codec.decode(codec.encode(url))