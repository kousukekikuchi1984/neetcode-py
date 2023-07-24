class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 0:
            return False
        already_visits = set()

        def sum_squared_digits(n: int) -> int:
            sum = 0
            while n:
                remaining = n % 10
                sum += remaining**2
                n = n // 10
            return sum

        while True:
            if n == 1:
                return True
            elif n in already_visits:
                return False

            already_visits.add(n)
            n = sum_squared_digits(n)
