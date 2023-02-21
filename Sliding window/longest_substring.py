class Solution:
    def length_longest_substring(self, s):
        '''
        s: str
        return: length of longest substring without repeating characters
        rtype: int
        '''
        charset = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while (s[r] in charset):
                charset.remove(s[l]) # slide the window one character 
                l += 1
            charset.add(s[r])
            res = max(res, r - l + 1)
        return res