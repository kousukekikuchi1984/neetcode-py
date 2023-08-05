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
