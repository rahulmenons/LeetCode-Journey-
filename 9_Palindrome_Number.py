class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        
    """
        reversed_num=0
        n=x
        while x>0:
            last_digit=x%10
            reversed_num = reversed_num*10 + last_digit
            x = x//10
        
        return n==reversed_num

