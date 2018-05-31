class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 1 and s[0] == ' ':
            return ''
        temp = s.split(' ')[::-1]
        while '' in temp:
            temp.remove('')
        return ' '.join(temp)
    
        