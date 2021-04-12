class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
       intervals=sorted(intervals,key=lambda x:x[0])
       cur=[intervals[0]]
       for ele in intervals[1:]:
           if cur[-1][1]<ele[0]:
               cur.append(ele)
           else:
               cur[-1][1]=max(cur[-1][1],ele[1])
       return cur