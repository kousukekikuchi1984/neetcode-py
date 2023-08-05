class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        s = s + s
        alt1 = alt2 = ""
        for i in range(len(s)):
            alt1 += "0" if i % 2 else "1"
            alt2 += "1" if i % 2 else "0"

        res = len(s)
        diff1 = diff2 = 0
        left = 0
        for right in range(len(s)):
            if s[right] != alt1[right]:
                diff1 += 1
            if s[right] != alt2[right]:
                diff2 += 1
            if (right - left + 1) > n:
                if s[left] != alt1[left]:
                    diff1 -= 1
                if s[left] != alt2[left]:
                    diff2 -= 1
                left += 1

            if (right - left + 1) == n:
                res = min(res, diff1, diff2)
        return res


class Codec:

    hashmap: dict = {}
    base_url: str = "http://tinyurl.com"

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        from uuid import uuid4
        hashid = str(uuid4).split("-")[0]
        self.hashmap[hashid] = longUrl
        return f"{base_url}/{hashid}"

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        hashid = shortUrl.split("/")[-1]
        return self.hashmap[hashid]
