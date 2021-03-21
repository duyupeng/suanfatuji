class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif n == 1:
            return x

        if n < 0:
            return 1 / self.myPow(x, -n)

        return self.myPow(x * x, n // 2) if n % 2 == 0 else x * self.myPow(x, n - 1)