class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        se = set(s)
        if len(se) != len(set(t)): return False

        for i in se:
            if s.count(i) != t.count(i):
                return False
        return True