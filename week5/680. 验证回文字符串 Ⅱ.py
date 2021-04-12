class Solution:
    def validPalindrome(self, s: str) -> bool:
        isright=lambda x: x==x[::-1]
        quchu_cur_x=lambda s,x: s[:x]+s[x+1:]
        left=0
        right=len(s)-1
        while left<right:
            if s[left]!=s[right]:
                return isright(quchu_cur_x(s,left)) or isright(quchu_cur_x(s,right))
            left+=1
            right-=1
        return True