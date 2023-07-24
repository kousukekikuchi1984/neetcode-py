class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        merged = []
        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                merged.append(newInterval)
                return merged + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                merged.append(intervals[i])
            else:
                newInterval = [
                    min(newInterval[0], intervals[i][0]),
                    max(newInterval[1], intervals[i][1]),
                ]
        merged.append(newInterval)
        return merged

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: x[0])
        start, end = intervals[0][0], intervals[0][1]
        merged = []
        for i in range(1, len(intervals)):
            if end < intervals[i][0]:
                merged.append([start, end])
                start, end = intervals[i][0], intervals[i][1]
                continue
            if end < intervals[i][1]:
                end = intervals[i][1]
        merged.append([start, end])
        return merged

    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda x: (x[0], x[1]))
        start, end = intervals[0][0], intervals[0][1]
        elased = 0
        for i in range(1, len(intervals)):
            if end <= intervals[i][0]:
                start, end = intervals[i][0], intervals[i][1]
            else:
                elased += 1
                end = min(end, intervals[i][1])
        return elased

    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        range_intervals = [[range(interval[0], interval[1] + 1), interval[1] - interval[0] + 1] for interval in intervals]
        range_intervals = sorted(range_intervals, key=lambda x: x[1])
        #
        results = []
        for query in queries:
            found = False
            for interval in range_intervals:
                if query in interval[0]:
                    results.append(interval[1])
                    found = True
                    break
            if not found:
                results.append(-1)
        return results

