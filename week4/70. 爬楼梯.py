class Solution:
    def climbStairs(self, n: int) -> int:
        if n<3:
            return n
        pre=1
        cur=2
        tmp=0
        for i in range(3,n+1):
            tmp=pre+cur
            pre=cur
            cur=tmp
        return tmp