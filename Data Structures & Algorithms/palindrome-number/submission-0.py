class Solution:
    def isPalindrome(self, x: int) -> bool:

        if x < 0:
            return False
        num1 = []
        while x > 0:
            num1.append(x % 10)
            x = x // 10

        num2 = num1.copy()
        num2 = num2[::-1]

        for i, num in enumerate(num1):
            if num1[i] != num2[i]:
                return False
        
        return True
        