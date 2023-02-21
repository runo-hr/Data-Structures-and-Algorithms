class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        n1, n2 = 0, 1
        for i in range(2, n + 1):
            temp = n1 + n2
            n1 = n2
            n2 = temp
        return n2

s = Solution()
print(s.fib(4))