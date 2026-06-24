class TimeMap:

    def __init__(self):
        from collections import defaultdict
        self.mapping = defaultdict(dict) # key: {timestamp: value}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.mapping[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        times = list(self.mapping[key].keys())
        if not times or (times and times[0] > timestamp):
            return ""
        
        l, r = 0, len(times)-1
        '''ret = times[0]
        while l < r:
            m = (l+r)//2
            if times[m] == timestamp:
                ret = times[m]
                break
            elif times[m] < timestamp:
                ret = max(ret, times[m])
                l = m+1
            else:
                r = m-1
        '''

        ret = times[0]
        while l <= r:
            m = (l+r)//2
            if times[m] > timestamp:
                r = m-1
            else:
                ret = times[m]
                l = m+1

        return self.mapping[key][ret]




