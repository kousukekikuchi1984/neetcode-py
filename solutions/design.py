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


class UndergroundSystem:

    def __init__(self):
        self.ongoing = {}  # id: (station, checkin_time)
        self.stations = {}  # dict of from_station: {to_station: (sum of time, counter)}
        
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        assert id not in self.ongoing
        self.ongoing[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        assert id in self.ongoing
        src_station, src_t = self.ongoing[id]
        del self.ongoing[id]
        elapsed = t - src_t
        if not src_station in self.stations:
            self.stations[src_station] = {}
        if stationName in self.stations[src_station]:
            total_time, counter = self.stations[src_station][stationName]
            self.stations[src_station][stationName] = (total_time + elapsed, counter + 1)
        else:
            self.stations[src_station][stationName] = (elapsed, 1)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total_time, counter = self.stations[startStation][endStation]
        return total_time / counter
