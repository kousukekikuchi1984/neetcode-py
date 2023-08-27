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

    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        stack = []
        num = x
        count = 0
        while num:
            num = int(num // 10)
            count += 1

        is_even = count % 2 == 0

        center = int(count / 2) if is_even else int((count - 1) / 2)
        for _ in range(center):
            stack.append(x % 10)
            x = int(x // 10)
        if not is_even:
            x = int(x // 10)
        while x:
            s = stack.pop()
            n = x % 10
            if s != n:
                return False
            x = int(x // 10)

        return True

    def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        while right >= left:
            mid = (left + right) // 2
            if mid * mid <= x:
                left = mid + 1
            else:
                right = mid - 1
        return right

    def countOdds(self, low: int, high: int) -> int:
        if low % 2 == 0:
            low += 1
        return len(range(low, high + 1, 2))
