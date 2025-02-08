class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        stringToNumber = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        result=0
        for i in range(len(s)):
            if(i+1 < len(s) and stringToNumber[s[i]] < stringToNumber[s[i+1]]):
                result -= stringToNumber[s[i]]
            else:
                result += stringToNumber[s[i]]
        return result


print(Solution().romanToInt("I"))
print(Solution().romanToInt("IV"))
print(Solution().romanToInt("IX"))
print(Solution().romanToInt("LVIII"))
print(Solution().romanToInt("MCMXCIV"))
print(Solution().romanToInt("MMMCMXCIX"))
