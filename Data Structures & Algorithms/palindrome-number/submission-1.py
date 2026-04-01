class Solution:
    def isPalindrome(self, x: int) -> bool:

        if x < 0:
            return False
        num1 = []
        while x > 0:
            num1.append(x % 10)
            x = x // 10

 

        return num1 == num1[::-1]
        