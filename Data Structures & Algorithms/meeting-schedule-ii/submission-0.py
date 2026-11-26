"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = [a.start for a in intervals]
        end = [a.end for a in intervals]
        start.sort()
        end.sort()

        s = 0
        e = 0
        res = 0
        count = 0
        while (e < len(end)):
           
            while (s < len(start) and start[s] < end[e]):
                s += 1
                count+=1
                print(count)
                res = max(res, count)
            e += 1
            count -= 1
            
            
        return res